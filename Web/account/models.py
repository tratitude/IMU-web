from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_detail(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone=models.CharField(max_length=13)
	# 需要加 address
