from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse

from .models import Category, Recruitment, New, Tag, Comment, User
from django.utils.html import  mark_safe
from django import forms
from ckeditor_uploader.widgets import   CKEditorUploadingWidget
from django.urls import path



class MyRecruitmentAdmin(admin.AdminSite):
    site_header = 'Orange Company eJob'

    def get_urls(self):
        return [path('recruitment-stats/', self.stats)] + super().get_urls()

    def stats(self, request):
        stats = Category.objects.annotate(count=Count('recruitment__id')).values('id', 'name', 'count')
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': stats
        })
# Register your models here.


# class RecruitmentForm(forms.ModelForm):
#     scription = forms.CharField(widget=CKEditorUploadingWidget)
#     class Meta:
#         model = New
#         fields = '__all__'
#
# class RecruitmentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'subject', 'active','scription', 'created_date']
#     search_fields =  ['subject']
#     list_filter = ['id', 'subject', 'created_date']
#     readonly_fields = ['avatar']
#     form =RecruitmentForm
#
#     def avatar(self,new):
#         return mark_safe(f"<img src='/static{new.image.name}' width='120'")
#
#     # class Media:
#     #     css = {
#     #         'all':('/static/css/style.css',)
#     #     }




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

    def avatar(self, new):
        if new.image:
            return mark_safe(f"<img src='{new.image.url}' width='120' />")
        return "No image"

    # class Media:
    #     css = {
    #         'all':('/static/css/style.css',)
    #     }

admin_site = MyRecruitmentAdmin(name='eJob')

admin_site.register(Category)
admin_site.register(Recruitment)
admin_site.register(Tag)
admin_site.register(User)
admin_site.register(Comment)
admin_site.register(New,NewAdmin)


