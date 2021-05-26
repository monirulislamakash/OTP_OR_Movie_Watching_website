from django.shortcuts import render
from .models import Contant
# Create your views here.
def index(request):
    video=Contant.objects.all()
    sendvar={
        "video":video,
    }
    return render(request,"index.html",sendvar)
def video(request,id):
    play=Contant.objects.filter(id=id)
    sendvar={
        "play":play,
    }
    return render(request,"video.html",sendvar)
def search(request):
    get_query=request.POST.get("query")
    yourfilm=Contant.objects.filter(titel__icontains=get_query)
    print(get_query)
    print(yourfilm)
    sendvar={
    "yourfilm":yourfilm,
    }
    return render(request,"search.html",sendvar)