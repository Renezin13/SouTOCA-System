from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_menu, name="SouTOCA"),
  path('login/', views.login, name="Login"),
  # path('register/', views.register, name="register"),


  # path('noticias/', views.noticias, name="noticias"),
  # path('noticias/<not_id>', views.noticia, name="noticia"),


  # path('eventos/', views.eventos, name="eventos"),
  # path('eventos/<eve_id>', views.evento, name="evento"),
  # path('eventos/<eve_id>/<par_id>', views.partida, name="partida"),

  # path('atletas/', views.atletas, name="atletas"),
  # path('atletas/<atle_id>', views.atleta, name="atleta"),

]