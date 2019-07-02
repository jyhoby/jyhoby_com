from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class 普通会员表(models.Model):
	用户= models.OneToOneField(User, on_delete=models.CASCADE)
	昵称=models.CharField(blank=True,max_length=50)
	生日=models.DateField(blank=True,null=True)
	# 用户头像 = models.ImageField(default='default.png', upload_to='images/')

	class Meta:
		verbose_name_plural = "普通会员表"
		

		