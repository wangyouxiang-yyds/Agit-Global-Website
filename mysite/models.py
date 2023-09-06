'''
啟用admin管理介面
python manage.py createsuperuser

'''

from django.db import models


# Create your models here.

class article_category(models.Model):  # 文章類別
    article_category = models.CharField('文章類別', max_length=10, null=False)
    def __str__(self):
        return self.article_category

class article(models.Model):  # 文章
    title = models.CharField("標題", max_length=50, null=False)  # 標題
    small_title = models.CharField("小標題", max_length=100, null=False)  # 小標題
    content = models.TextField("文案", blank=True)  # 內文
    author_name = models.CharField("作者", max_length=10, null=False)  # 作者
    article_category = models.ForeignKey(article_category, on_delete=models.CASCADE)  # foreign key
    modify_date = models.DateTimeField(auto_now=True)   # 修改時間
    create_date = models.DateField(auto_now_add=True)   # 新增時間
    article_photo = models.ImageField("文章圖片", upload_to='article_photo', max_length=255)
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
    manager_category = models.CharField( max_length=10, null=False)
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


class banner_category(models.Model):
    banner_category = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.banner_category
class banner(models.Model):
    banner_photo = models.ImageField(upload_to='banner_photo', max_length=255)  # 圖片
    modify_date = models.DateTimeField(auto_now=True)  # 修改時間
    create_date = models.DateField(auto_now_add=True)  # 新增時間
    banner_category = models.ForeignKey(banner_category, on_delete=models.CASCADE)  # foreign key

class project(models.Model):
    project_photo = models.ImageField(upload_to='project_photo', max_length=255)  # 圖片
    big_title = models.CharField(max_length=50, null=False)  # 大標題
    little_title = models.CharField(max_length=50, null=False)  # 小標題
    modify_date = models.DateTimeField(auto_now=True)  # 修改時間
    create_date = models.DateField(auto_now_add=True)  # 新增時間
    def __str__(self):
        return self.big_title



class department_form_category(models.Model):
    department_form_category = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.department_form_category


class department_form(models.Model):
    form_name = models.CharField(max_length=50, null=False)  # 表單名稱
    form_link = models.CharField(max_length=100, null=False)  # 表單連結
    department_form_category = models.ForeignKey(department_form_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.form_name