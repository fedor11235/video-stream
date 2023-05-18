from django.db import models

class Video(models.Model):
  title       = models.CharField     ('Заголовок', max_length   = 100)
  description = models.TextField     ('Описание' ,  max_length  = 1000)
  image       = models.ImageField    ('Превью'   , upload_to    = 'media/image/')
  file        = models.FileField     ('Видео'    , upload_to    = 'media/video/')
  create_at   = models.DateTimeField ('Дата'     , auto_now_add = True)

  def __str__(self):
    return self.title

