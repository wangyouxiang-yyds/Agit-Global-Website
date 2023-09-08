from django.contrib import admin
from mysite import models

# Register your models here.
admin.site.register(models.article_category)
admin.site.register(models.article)
admin.site.register(models.author)
admin.site.register(models.manager)
admin.site.register(models.manager_category)
admin.site.register(models.banner_category)
admin.site.register(models.banner)
admin.site.register(models.project)
admin.site.register(models.department_form_category)



class department_form(admin.ModelAdmin):
    list_display = ('department_form_category', 'form_name', 'form_link', 'modify_date', 'modify_user')

admin.site.register(models.department_form, department_form)




class common_link(admin.ModelAdmin):
    list_display = ('link_title', 'link_href')

admin.site.register(models.common_link, common_link)