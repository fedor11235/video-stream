from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DownloadForm

def index(request):
  return render(request, 'index.html')

# def download(request):
#   return render(request, 'download.html')

def download(request):
  if request.method == 'POST':
    form = DownloadForm(request.POST, request.FILES)
    print(request.POST, request.FILES, form)
    if form.is_valid():
      form.save()
    else:
      return render(request, 'download.html', {'form': form})
  else:
      form = DownloadForm()
      return render(request, 'download.html', {'form': form})
  return HttpResponseRedirect('/video/download/')
