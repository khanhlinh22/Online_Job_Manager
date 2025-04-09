from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    pass


class  BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
class Recruitment(BaseModel):
    subject = models.CharField(max_length=255)
    scription = models.TextField(null=True)
    image =models.ImageField(upload_to='recruitment/%Y/%m/')
    category =models.ForeignKey(Category, on_delete=models.PROTECT) #kieu khong cho xoa

    def __str__(self):
        return self.subject

class New(BaseModel): #kieu bang tin dang tuyen dung
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image =models.ImageField(upload_to='new/%Y/%m/')
    recruitment = models.ForeignKey(Recruitment,on_delete=models.CASCADE) #o tren xoa o duoi xoa theo

    def __str__(self):
        return self.subject