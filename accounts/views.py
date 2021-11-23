from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationform


class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationform
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        #CreatViewクラスのform_validメソッドをオーバーライドする

        user = form.save()
        self.objects = user
         #form.save()としフォームの入力データをCustomUserモデルのデータベースに登録する。

        return super().form_valid(form)
        

class SignUpSuccessView(generic.TemplateView):
    template_name = 'signup_success.html'
    

