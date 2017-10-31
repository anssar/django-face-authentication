# django-face-authentication

## Установка
1) В файле settings.py добавить приложение face_authentication в INSTALLED_APPS
2) Настроить media (см. документацию django)
3) В консоле выполнить
   manage.py createsuperuser
   manage.py collectstatic
   manage.py makemigrations
   manage.py migrate

## Использование
1) Добавить пользователей в базу данных (модель FAUser в админке)
2) В файле views.py вашего приложения
   from face_authentication.decorators import FARequired
3) Для представлений вашего приложения, для которых требуется авторизация используйте декоратор FARequired

Пример использования можно посмотреть в репозитории
https://github.com/anssar/django-face-authentication
