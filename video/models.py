from django.db import models

class Downloader(models.Model):
  name = models.CharField("Название", max_length=100)
  Dis = models.TextField("Описание", max_length=1000)
  file = models.FileField("Видео", upload_to='media/')
