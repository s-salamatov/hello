from django.db import models


class Feedback(models.Model):
    name = models.CharField('Как к вам обращаться?', max_length=512)
    email = models.EmailField('Ваш email')
    message = models.TextField('Сообщение')


class CommonCV(models.Model):
    uploaded = models.DateTimeField('Дата и время загрузки на сайт', auto_now_add=True)
    doc = models.FileField('Файл', upload_to='docs/', blank=False)

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return str(self.uploaded)
