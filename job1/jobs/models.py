from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from cloudinary.models import CloudinaryField


# Create your models here.

class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recruitment(BaseModel):
    subject = models.CharField(max_length=255)
    scription = models.TextField(null=True)
    # image =models.ImageField(upload_to='recruitment/%Y/%m/')
    image = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # kieu khong cho xoa

    def __str__(self):
        return self.subject



    def get_scription(self):
        return mark_safe(self.scription)


class New(BaseModel):  # kieu bang tin dang tuyen dung
    subject = models.CharField(max_length=255)
    content = RichTextField()
    # image =models.ImageField(upload_to='new/%Y/%m/')
    image = CloudinaryField()
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE)  # o tren xoa o duoi xoa theo
    tags = models.ManyToManyField('Tag')

    # de trong nhay de khi xuong duoi no moi co the hieu
    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new = models.ForeignKey(New, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.CharField(max_length=255, null=False)


class Like(Interaction):
    class Meta:
        unique_together = ('user', 'new')


# phan nay moi them
class UserProfile(BaseModel):
    user = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE)  # Sử dụng `CASCADE` để xóa UserProfile khi User bị xóa
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = CloudinaryField()

    # vi mot profile co nhieu skill va nguoc lai 1 skill co nhieu nguoi co
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        # return self.first_name
        return f"{self.first_name} {self.last_name}"


# kieu la chon skill minh co nhu tieng anh hoac tin hoc....
class Skill(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name