from django.db import models
from django.contrib.auth.models import User

from django.db import models
# Create your models here.
# class bool_model(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     true_false=models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.true_false)

class profile_img(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField()
    
    def __str__(self):
        return f"{self.user.username}'s profile_img"

class bool_model(models.Model):
    PAYMENT_CHOICES = [
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='Not Paid')

    def __str__(self):
        return f"{self.user.username}'s bool_model"
    
    
    
    
# models.py

class Update_Profile(models.Model):
	profile_pic = models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name



