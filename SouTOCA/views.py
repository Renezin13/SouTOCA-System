from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import tb_usuarios
from django.contrib import messages


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

def register(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if nome and email and password:  # Verifique se todos os campos estão preenchidos
            # Crie o usuário do Django
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()

            # Agora crie o objeto tb_usuarios
            usuario = tb_usuarios(
                usr_user=user,
                usr_nome=nome,
                usr_email=email,
                usr_senha=password  # Ou pode deixar a senha como `None` se você já a hashear
            )
            usuario.save()
            
            # Mensagem de sucesso
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login/')  # Ajuste o redirecionamento conforme necessário
        else:
            messages.error(request, 'Preencha todos os campos.')

    return render(request, 'register.html')