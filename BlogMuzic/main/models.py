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
