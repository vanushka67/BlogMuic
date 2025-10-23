from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок мероприятия', max_length=100)
    description = models.TextField('Тект записи')
    date = models.DateField('Дата публикации')
    img = models.ImageField('Обложка альбомы', upload_to='img')
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title