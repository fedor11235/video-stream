from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from .forms import UploadForm
from helpers import print_red

def index(request):
  return render(request, 'index.html')

def get_list_video(request):
  print_red(Video.objects.all())
  return render(request, 'index.html', {'video_list': Video.objects.all()})

# def get_video(request, pk: int):
#     _video = get_object_or_404(Video, id=pk)
#     return render(request, "video_hosting/video.html", {"video": _video})


# def get_streaming_video(request, pk: int):
#     file, status_code, content_length, content_range = open_file(request, pk)
#     response = StreamingHttpResponse(file, status=status_code, content_type='video/*')

#     response['Accept-Ranges'] = 'bytes'
#     response['Content-Length'] = str(content_length)
#     response['Cache-Control'] = 'no-cache'
#     response['Content-Range'] = content_range
#     return response

def download(request):
  if request.method == 'POST':
    form = UploadForm(request.POST, request.FILES)
    print(request.POST, request.FILES, form)
    if form.is_valid():
      form.save()
    else:
      return HttpResponseRedirect('/video/download/')
  else:
      form = UploadForm()
      return render(request, 'download.html', {'form': form})
  return HttpResponseRedirect('/video/')
