import datetime

from django.db import models


# Create your models here

"""
Тут лежат модели для админки после рефакторинга нужно прописать команды
py manage.py makemigrations
py manage.py migrate

Если будут ошибки то нужно удалить все из папки migtations (кроме init)

Если это гне помогло то удали db.sqlite3
затем введи две верхние команды + py manage.py createsuperuser
там имя пароль (ты не будешь его видеть когда вбиваешь) 
"""



class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text = models.TextField('Текст', default=None)
    image = models.ImageField(
        'img', default=None,
        upload_to='home'
    )


class Demand(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='demand'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Заголовок', default=None)
    table = models.TextField('Таблица', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='geography'
    )

class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Текст', default=None)
