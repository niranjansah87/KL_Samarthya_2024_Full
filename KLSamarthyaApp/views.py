from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def events(request):
    return render(request, 'carousel.html')

def team(request):
    return render(request, 'team.html')

