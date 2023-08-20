from django.contrib import admin
from mysite import models

# Register your models here.
admin.site.register(models.article_category)
admin.site.register(models.article)
admin.site.register(models.author)

