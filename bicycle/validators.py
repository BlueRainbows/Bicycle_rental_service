from datetime import datetime, timedelta

from rest_framework.serializers import ValidationError


class DateValidator:

    def __init__(self, rent_date):
        self.rent_date = rent_date

    def __call__(self, value):
        get_rent_date = dict(value).get(self.rent_date)

        if get_rent_date < datetime.now().date():
            raise ValidationError(
                "Вы не можете арендовать велосипед задним числом"
            )
        if datetime.now().date() <= get_rent_date > datetime.now().date() + timedelta(days=30):
            raise ValidationError(
                "Вы не можете арендовать велосипед более чем на 30 дней"
            )
