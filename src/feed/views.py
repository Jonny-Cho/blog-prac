from django.shortcuts import render

# Create your views here.
def index(request):
    name = "Jonny"
    return render(request, "index.html", {"name" : name})

def detail(request):
    pass

def about(request):
    pass
