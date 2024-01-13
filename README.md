Описание:
API для социальной сети, который позволяет пользователям, публиковать записи, комментировать записи, подписываться на авторов.

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/IlianL/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/scripts/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

cd yatube_api
python manage.py migrate
Запустить проект:

python3 manage.py runserver
Пример работы API для неавторизованного пользователя:
Неавторизованные пользователи могут только читать контент, они не могут создавать или менять что-то. Для неавторизованных пользователей недоступен эндпоинт follow.

