from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import tb_usuarios
from django.contrib import messages

# Create your views here.

def main_menu(request):
    context = {
        'title': 'SouTOCA'
    }
    return render(request, 'mainmenu.html', context)

def login_view(request):  # Renomeado para evitar conflito com a função 'login'
    if request.method == 'POST':
        username = request.POST.get('username')  # Ajustado para 'username'
        password = request.POST.get('password')

        if username and password:
            # Autenticar o usuário
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Login bem-sucedido
                auth_login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('main_menu')  # Redireciona para o menu principal
            else:
                # Credenciais inválidas
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            messages.error(request, 'Preencha todos os campos.')

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
            # Verifique se o usuário ou email já existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado.')
            else:
                # Crie o usuário do Django
                user = User.objects.create_user(username=nome, email=email, password=password)
                user.save()

                # Agora crie o objeto tb_usuarios
                usuario = tb_usuarios(
                    usr_user=user,
                    usr_nome=nome,
                    usr_email=email,
                    usr_senha=password  # De preferência, armazene a senha de forma segura
                )
                usuario.save()
                
                # Mensagem de sucesso
                messages.success(request, 'Usuário registrado com sucesso!')
                return redirect('login')  # Redireciona para a view de login
        else:
            messages.error(request, 'Preencha todos os campos.')

    return render(request, 'register.html')
