from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from functools import partial  # Importar partial

# Validador de tamanho de imagem
def validate_image_size(image, max_size_mb): # Tamanho máximo permitido (em MB)
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"O tamanho máximo permitido é {max_size_mb} MB.")

# Usar partial para configurar o validador com o valor predefinido de max_size_mb
validate_image_size_2mb = partial(validate_image_size, max_size_mb=2)
validate_image_size_10mb = partial(validate_image_size, max_size_mb=10)

class tb_usuarios(models.Model):
    usr_user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_id = models.AutoField(primary_key=True)
    usr_nome = models.CharField(max_length=255)
    usr_email = models.EmailField(max_length=255)
    usr_senha = models.CharField(max_length=255)  # Campo para armazenar a senha hasheada
    usr_imagem = models.ImageField(
        upload_to="SouTOCA/static/user_images/", 
        blank=True, 
        validators=[validate_image_size_2mb]
    )

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

class tb_docentes(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_matricula = models.CharField(max_length=255)
    doc_usr_id = models.OneToOneField(tb_usuarios, on_delete=models.CASCADE) 


class tb_esportes(models.Model):
    esp_id = models.AutoField(primary_key=True)
    esp_nome = models.CharField(max_length=255)
    esp_img = models.ImageField(
        upload_to="SouTOCA/static/sport_images/", 
        blank=True, 
        validators=[validate_image_size_10mb]
    )


class tb_atletas(models.Model):
    atl_id = models.AutoField(primary_key=True)
    atl_turma = models.CharField(max_length=255)
    atl_idade = models.IntegerField()
    atl_bio = models.TextField()
    atl_usr_id = models.OneToOneField(tb_usuarios, on_delete=models.CASCADE)
    atl_esp_id = models.OneToOneField(tb_esportes, on_delete=models.CASCADE)


class tb_imagens(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_conteudo = models.ImageField(upload_to="SouTOCA/static/images/")
    img_alt = models.TextField(blank=True)


class tb_noticias(models.Model):
    not_id = models.AutoField(primary_key=True)
    not_titulo = models.CharField(max_length=255)
    not_conteudo = models.TextField()
    not_publishDate = models.DateField()
    not_image = models.ImageField(
        upload_to="SouTOCA/static/sport_images/", 
        blank=True, 
        validators=[validate_image_size_10mb]
    )
    not_usr_id = models.OneToOneField(tb_usuarios, on_delete=models.CASCADE)
    not_esp_id = models.OneToOneField(tb_esportes, on_delete=models.CASCADE)
    not_img_id = models.OneToOneField(tb_imagens, on_delete=models.CASCADE)


class tb_comentarios(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_conteudo = models.TextField(max_length=255)
    com_publishDate = models.DateField()
    com_usr_id = models.OneToOneField(tb_usuarios, on_delete=models.CASCADE)
    com_not_id = models.OneToOneField(tb_noticias, on_delete=models.CASCADE)
