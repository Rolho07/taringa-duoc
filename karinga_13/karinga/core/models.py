from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_type = models.CharField(max_length=30)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_names = models.CharField(max_length=100)
    user_lastnames = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=255)
    user_username = models.CharField(max_length=50)
    user_password = models.CharField(max_length=255)
    user_description = models.TextField(blank=True, null=True)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_creation_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
