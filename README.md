# :page_facing_up:  ИНСТРУКЦИЯ ПО ЗАПУСКУ ПРОЕКТА ЧЕРЕЗ DOCKER

- Соберите образ и запустите проект при помощи команды:

**docker-compose build**<br>
**docker-compose up -d**<br>
Создайте администратора:<br>
**docker-compose exec app python manage.py csu**<br>
Создание группы пользователей:<br>
**docker-compose exec app python manage.py group**<br>
Запустите celery:<br>
**docker-compose exec app celery -A config worker -l INFO**
**docker-compose exec app celery -A config beat -l INFO -S django**
