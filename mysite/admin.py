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
admin.site.register(models.department_form)