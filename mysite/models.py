'''
啟用admin管理介面
python manage.py createsuperuser

'''


from django.db import models

# Create your models here.
class about_table(models.Model):
    about_banner = models.ImageField(upload_to='about_banner', max_length=255) # about的banner圖
    content_photo = models.ImageField(upload_to='content_photo', max_length=255) # about的banner圖
    content_small_title = models.CharField(max_length=200, null=False)
    content_big_title = models.CharField(max_length=200, null=False)
    create_date  = models.DateField(auto_now_add=True) # 創建時間
class about_manager_photo(models.Model):
    manger_photo = models.ImageField(upload_to='manger_photo', max_length=255)