import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import tb_usuarios
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def register(request):
    context = {
        'title': 'SouTOCA - Registro'
    }
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            # Lógica para criar o usuário...
            user = tb_usuarios(
                usr_nome=name,
                usr_email=email,
                usr_senha=password
            )
            user.save()
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Erro ao decodificar JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # Se não for uma requisição POST, renderize o template
    return render(request, 'register.html', context)