from django.db import models
from django.contrib.auth.models import User

class UsuarioPersonalizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Otros campos necesarios para tu modelo

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_type = models.CharField(max_length=30)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_creation_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core_posts')

class PostReply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    reply_content = models.TextField()
    reply_creation_date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User_Role(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Votes(models.Model):
    votes_id = models.AutoField(primary_key=True)
    votes_type = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
