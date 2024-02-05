Описание:
API для социальной сети, который позволяет пользователям, публиковать записи, комментировать записи, подписываться на авторов.

Стек:
Python
Django REST Framework
Djoser

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/kise2k/api_final_yatube.git

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

Примеры ответа

GET запрос
/api/v1/posts/

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
POST запрос
/api/v1/posts/


{
  "text": "string",
  "image": "string",
  "group": 0
}
Пример ответа.


{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}

После запуска проекта, документация будет доступна по адресу:
http://localhost:port/redoc/

Автор: Седякин Кирилл Игоревич 
Ссылка на github: https://github.com/kise2k
