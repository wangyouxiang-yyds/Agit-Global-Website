from django.shortcuts import render, get_object_or_404
from mysite import models, approval
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .models import article, banner, banner_category, department_form_category, department_form, common_link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def approval_view(request):
    if request.method == 'POST':
        form = approval.approval_form(request.POST)
        if form.is_valid():
            message = "信件已送出"
            user_name = form.cleaned_data['user_name']
            user_department = form.cleaned_data['user_department']
            user_email = form.cleaned_data['user_email']
            user_application_event = form.cleaned_data['user_application_event']
            user_message = form.cleaned_data['user_message']

            context = {
                'user_name': user_name,
                'user_department': user_department,
                'user_email': user_email,
                'user_application_event': user_application_event,
                'user_message': user_message
            }
            # 建構簽核連結
            current_site = get_current_site(request)
            sign_url = reverse('sign_approval', args=[user_name])  # 假設這個 URL 名稱是 "sign_approval"

            mail_body = render_to_string('approval_reject_mail.html', context)

            email = EmailMessage('來自Agit簽核',
                                 mail_body,
                                 user_email,
                                 ['ex07@agit-global.com'])
            email.content_subtype = 'html'  # 設置郵件類型為 HTML
            email.send()


    else:

        form = approval.approval_form()

    return render(request, 'approval.html', locals())




def index(request):
    current_url = request.path_info
    index_url = reverse('index')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='index')       # 首頁打開第一個banner
    banner_sec_part = banner.objects.filter(banner_category__banner_category='index_sec')   # 下滑第二個banner
    banner_third_part = banner.objects.filter(banner_category__banner_category='index_thir')    # 第三個banner
    article_news_three = models.article.objects.all().order_by('-pk', 'create_date')[:3]  # -pk為降序 這邊說明為依照建立時間去排序 限制三筆
    return render(request, 'index.html', locals())


def about(request):
    current_url = request.path_info
    about_url = reverse('about')  # 顯示顏色的
    about_detail = models.manager.objects.all()
    banners = banner.objects.filter(banner_category__banner_category='about')

    return render(request, 'about.html', locals())


def pricing(request):
    current_url = request.path_info
    pricing_url = reverse('pricing')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='pricing')

    return render(request, 'pricing.html', locals())


def service(request):
    current_url = request.path_info
    service_url = reverse('service')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='service')
    categories = department_form_category.objects.all()

    department_forms_by_category = {}
    for category in categories:
        forms = department_form.objects.filter(department_form_category=category)
        department_forms_by_category[category] = forms


    com_link = common_link.objects.all()
    return render(request, 'service.html', locals())


def project(request):
    current_url = request.path_info
    project_url = reverse('project')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='project')# 挑選banner
    award = models.project.objects.all().order_by('pk', 'create_date')
    return render(request, 'project.html', locals())


def blog_grid(request):

    article = models.article.objects.all().order_by('-pk', 'create_date')  # -pk為降序 這邊說明為依照建立時間去排序
    current_url = request.path_info
    blog_grid_url = reverse('blog_grid')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='blog')

    limit = 4  # 每筆4則就文章分頁
    page = request.GET.get('page', 1)
    paginator = Paginator(article, limit)

    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article= paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)

    return render(request, 'blog-grid.html', locals())


def blog_sidebar(request):
    article = models.article.objects.all().order_by('-pk', 'create_date')  # -pk為降序 這邊說明為依照建立時間去排序

    current_url = request.path_info
    blog_sidebar_url = reverse('blog_sidebar')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='blog') # 挑選banner
    article_news_three = models.article.objects.all().order_by('-pk', 'create_date')[:3]  # -pk為降序 這邊說明為依照建立時間去排序 限制三筆

    limit = 4  # 每筆4則就文章分頁
    page = request.GET.get('page', 1)
    paginator = Paginator(article, limit)

    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article= paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)

    return render(request, 'blog-sidebar.html', locals())


def blog_single(request, article_id):
    article = models.article.objects.all().order_by('-pk', 'create_date')  # -pk為降序 這邊說明為依照建立時間去排序
    current_article = get_object_or_404(models.article, pk=article_id)
    previous_article = models.article.objects.filter(pk__lt=article_id).order_by('-pk').first()
    next_article = models.article.objects.filter(pk__gt=article_id).order_by('pk').first()
    article_obj = get_object_or_404(article, pk=article_id)
    current_url = request.path_info
    article_news_three = models.article.objects.all().order_by('-pk', 'create_date')[:3]        # -pk為降序 這邊說明為依照建立時間去排序 限制三筆
    banners = banner.objects.filter(banner_category__banner_category='blog')
    return render(request, 'blog-single.html', locals())


def contact(request):
    current_url = request.path_info
    contact_url = reverse('contact')  # 顯示顏色的
    banners = banner.objects.filter(banner_category__banner_category='contact')
    return render(request, 'contact.html', locals())


