# api_final 🚀
___

## Стек:
[![Python](https://img.shields.io/badge/-Python-grey)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-grey)](https://www.djangoproject.com/) [![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-grey)](https://www.django-rest-framework.org/) [![Pytest](https://img.shields.io/badge/-Pytest-grey)](https://docs.pytest.org/en/6.2.x/) [![Postman](https://img.shields.io/badge/-Postman-grey)](https://www.postman.com/) [![JWT + Djoser](https://img.shields.io/badge/-JWT%20%2B%20Djoser-grey)](https://djoser.readthedocs.io/en/latest/introduction.html)
___

## Описание проекта:
В данном проекте реализовано API для социальной сети **"YaTube"** (Совпадение с реально существующими социальным сетями случайны). В данной социальной сети можно: публиковать свои записи и фотографии, комментировать чужие, присоединяться к сообществам, строить империи, свергать монархов, устраивать новые крестовые походы, плести интриги! кхм-кхм... ну, может мы немного и преувеличили, но функционал широкий 😉.
___

## Возможности:
- любой пользователь, может запросить список всех публикаций и сообществ; 
- авторизованные пользователи могут смотреть подробности публикаций и получать информацию о сообществах;
- автор может создавать публикации, а другие авторизованные пользователи оставлять свои комментарии.
___

## Развёртывание проекта :
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AleksanderKarbyshev/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение (Windows/Bash):

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции на уровне проекта:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

5. Запустить проект:

```
python manage.py runserver
```