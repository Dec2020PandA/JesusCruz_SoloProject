from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def form(request):
    if request.method=='POST':
        return render(request, 'thanks.html')
    return render(request, 'contact.html')