from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

# Validador de tamanho de imagem
def validate_image_size(image):
    max_size_mb = 2  # Tamanho máximo permitido (em MB)
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"O tamanho máximo permitido é {max_size_mb} MB.")

class tb_usuarios(models.Model):
    usr_user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_id = models.AutoField(primary_key=True)
    usr_nome = models.CharField(max_length=255)
    usr_email = models.EmailField(max_length=255)
    usr_senha = models.CharField(max_length=255)  # Campo para armazenar a senha hasheada
    usr_imagem = models.ImageField(upload_to="SouTOCA/static/user_imagens", blank=True, validators=[validate_image_size])

    def save(self, *args, **kwargs):
        # Garante que a senha seja hasheada antes de salvar
        if not self.pk:  # Apenas hasheia se o usuário for novo
            self.usr_senha = self.hash_password(self.usr_senha)
        super().save(*args, **kwargs)
    
    def hash_password(self, raw_password):
        # Método para hashear a senha
        return make_password(raw_password)

    def __str__(self):
        return self.usr_nome