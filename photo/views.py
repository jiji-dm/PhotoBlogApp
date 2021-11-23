from django.core import paginator
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import PhotoPost1Form
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from .models import PhotoPost1

class IndexView(generic.ListView):
    template_name = 'index.html'
    queryset = PhotoPost1.objects.order_by('-posted_at')
    paginate_by = 9

#デコレーターユーザーにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
#ログイン状態でなければsetting.pyのLOGIN_URLにリダイレクトされる

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(generic.CreateView):
    #写真投稿ページのビュー
    form_class = PhotoPost1Form #モデルとフォームが登録されたフォームクラス
    template_name = 'photo_post.html'
    success_url = reverse_lazy('photo:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(generic.TemplateView):
    template_name = 'post_success.html'
    
class CategoryView(generic.ListView):
    template_name = "index.html"
    paginate_by = 9
    
    def get_queryset(self):  
        #CategoryViewでオーバーライドした際は、CategoryViewオブジェクトが取得される
        #インスタンス変数kwargs(django.views.generic.Viewクラスで定義)
        #クエリを実行する
        #self.kwargs()で取得が必要なため、クラス変数querysetではなく、
            #get_queryset()のオーバーライドによりクエリを実行する
        
        category_id = self.kwargs['category']
        #self.kwargsでキーの値(Categorysテーブルのid)を取得
        
        categories = PhotoPost1.objects.filter(
            category=category_id).order_by('-posted_at')
        #filter(フィールド名＝id)で絞り込む
        return categories

class UserView(generic.ListView):
    template_name = 'index.html'
    paginator = 9
    
    def get_queryset(self):
        
        user_id = self.kwargs['user']
        user_list = PhotoPost1.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = PhotoPost1
    
class MypageView(generic.ListView):
    template_name = 'mypage.html'
    paginator = 9
    
    def get_queryset(self):
        queryset = PhotoPost1.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(generic.DeleteView):
    model = PhotoPost1
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)