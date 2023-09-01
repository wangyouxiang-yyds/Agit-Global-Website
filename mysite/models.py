'''
啟用admin管理介面
python manage.py createsuperuser

'''

from django.db import models


# Create your models here.

class article_category(models.Model):  # 文章類別
    article_category = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.article_category

class article(models.Model):  # 文章
    title = models.CharField(max_length=50, null=False)  # 標題
    small_title = models.CharField(max_length=100, null=False)  # 小標題
    content = models.TextField(blank=True)  # 內文
    author_name = models.CharField(max_length=10, null=False)  # 作者
    article_category = models.ForeignKey(article_category, on_delete=models.CASCADE)  # foreign key
    modify_date = models.DateTimeField(auto_now=True)   # 修改時間
    create_date = models.DateField(auto_now_add=True)   # 新增時間
    article_photo = models.ImageField(upload_to='article_photo', max_length=255)
    def __str__(self):
        return self.title

# class article_photo(models.Model): # 圖片
#     url = models.ForeignKey(article, on_delete=models.CASCADE)


class author(models.Model):
    name = models.ForeignKey(article, on_delete=models.CASCADE)
    department = models.CharField(max_length=10, null=False)
    position = models.CharField(max_length=10, null=False)


    def __str__(self):
        return self.name


class manager_category(models.Model):
    manager_category = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.manager_category
class manager(models.Model):
    manager_name = models.CharField(max_length=10, null=False)  # 作者
    position = models.CharField(max_length=10, null=False)  # 職稱
    manager_photo = models.ImageField(upload_to='manager_photo', max_length=255)    # 圖片
    manager_saying = models.CharField(max_length=50, null=False)    # 主管的話
    manager_category = models.ForeignKey(manager_category, on_delete=models.CASCADE)  # foreign key

    def __str__(self):
        return self.manager_name