import logging
from datetime import datetime, timedelta
from celery import shared_task

from bicycle.models import Refunds, Rental


logger = logging.getLogger(__name__)


@shared_task()
def get_amount():
    rental_data = Rental.objects.filter(rent_date__lte=datetime.now().date())
    for rental in rental_data:
        if Refunds.objects.filter(rental__pk=rental.pk).exists():
            for refund in Refunds.objects.filter(rental__pk=rental.pk, rent_status=True, refund_date__isnull=True):
                if refund.amount == 0:
                    refund.amount = rental.bicycle.price
                    refund.last_recall = datetime.now().date()
                    refund.save()
                    logger.info(f'Пересчёт суммы для {rental}')
                else:
                    if refund.last_recall < datetime.now().date():
                        refund.amount += rental.bicycle.price
                        refund.last_recall = datetime.now().date()
                        refund.save()
                        logger.info(f'Пересчёт суммы для {rental}')
        else:
            if rental.rent_date == datetime.now().date():
                Refunds.objects.create(
                    rental=rental
                )
                logger.info(f'Создан объект возврата аренды {rental}')
