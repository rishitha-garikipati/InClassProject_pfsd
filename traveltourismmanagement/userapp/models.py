from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField(blank=False,primary_key=True,auto_created=True)
    username = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    is_active = models.BooleanField(max_length=10,blank=False)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)

    class Meta:
        db_table = "users"