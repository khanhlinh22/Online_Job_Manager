from django.contrib import admin
from django.contrib.sites import models

from .models import Category, Recruitment, New
from django.utils.html import  mark_safe
from django import forms
from ckeditor_uploader.widgets import   CKEditorUploadingWidget

# Register your models here.

class NewForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = New
        fields = '__all__'

class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date']
    search_fields =  ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['avatar']
    form =NewForm

    def avatar(self,new):
        return mark_safe(f"<img src='/static{new.image.name}' width='120'")

    class Media:
        css = {
            'all':('/static/css/style.css',)
        }


admin.site.register(Category)
admin.site.register(Recruitment)
admin.site.register(New,NewAdmin)
