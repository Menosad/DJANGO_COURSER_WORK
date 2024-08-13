MAILING
вэб приложение для создания рассылок, управления ими и сбора статистики.
1. Создаем пользователя;
2. Добавляем вручную или загружаем пользователей добавлением excel файла (1 книга, 1 лист в следующем формате:
название компании | имя контактоного лица (если есть) | электронная почта);
3. Выбираем характеристики рассылки, и запускаем в работу.

Приятного пользования!

Инструкции для разработчиков:
Перед началом работы обязательно настройте конфигурацию в файле /settings.py, добавив файл .env
а в нем прописать:
SECRET_KEY='тут секретный ключ джанго'
DEBUG=True

#DATABASE
DATABASE_NAME='имя вашей базы данных'
DATABASE_USER='имя пользователя базы данных'
DATABASE_PASSWORD='пароль к базе данных'


#EMAIL HOST
EMAIL_HOST ='ваш хост рассылки'
EMAIL_PORT ='порт хоста'
EMAIL_HOST_USER='созданный вами хост'
EMAIL_HOST_PASSWORD='пароль для внешнего приложения'

команда для создания админа: python manage.py csu
команда для создания SECRET_KEY: python manage.py cskey
команда для загрузки базы данных: python manage.py dataload