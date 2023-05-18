from django import forms
from .models import Downloader

class DownloadForm(forms.ModelForm):
  class Meta:
    model = Downloader
    fields = ['name', 'Dis', 'file']