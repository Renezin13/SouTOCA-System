from django.shortcuts import render

# Create your views here.

def main_menu(request):
    context = {
        'title': 'SouTOCA'
    }
    return render(request, 'mainmenu.html', context)

def login(request):
    context = {
        'title': 'SouTOCA'
    }
    return render(request, 'login.html', context)