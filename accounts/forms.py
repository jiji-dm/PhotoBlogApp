from django.contrib.auth import forms
from .models import CustomUser

class CustomUserCreationform(forms.UserCreationForm):
    #UserCreationFormのクラスを継承し、オーバーライドする
    class Meta:
        model = CustomUser
        #連携するUserモデル

        fields = ('username', 'email', 'password1', 'password2',)
        #フォームで使用するフィールドを設定
        #ユーザー名、 メールアドレス、 パスワード、 パスワード（確認用）