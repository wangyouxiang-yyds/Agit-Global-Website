from django.shortcuts import render
from mysite import models, approval
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


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

    return render(request, 'agitweb/index.html', locals())



def about(request):

    return render(request, 'about.html', locals())