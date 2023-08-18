from django import forms


class approval_form(forms.Form):
    department = [
        ['AD', '管理部'],
        ['RD', '開發部'],
        ['FN', '財務部'],
        ['PC', '採購部'],
        ['WH', '倉庫部'],
        ['PT', '現場']

    ]
    # 申請類別
    application_event = [
        [1, '開放USB存取權限'],
        [2, '通訊軟體使用權限(Line,wechat,whatapp)'],
        [3, '申請Agit Client VPN,以便協助我司進行Epicor的問題排除,測試及開發']

    ]

    user_name = forms.CharField(label='名字', max_length=50)
    user_department = forms.ChoiceField(label='部門', choices=department)
    user_email = forms.EmailField(label='電子信箱')
    user_application_event = forms.MultipleChoiceField(label='申請類別', choices=application_event,
                                                       widget=forms.CheckboxSelectMultiple(
                                                       attrs={'class': 'form-check-input'}))  # 申請類別
    user_message = forms.CharField(label='申請原因(詳細說明)', widget=forms.Textarea(attrs={'class': 'form-control'}))
