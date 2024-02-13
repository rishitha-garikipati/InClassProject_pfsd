from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class User:
    pass


class Users(models.Model):
    user_id = models.ForiegnKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_lenght=10)
    gender = models.CharField(max_lenght=10)
    img = models.ImageField(upload_to="")

    class Meta:
        db_table = "users"