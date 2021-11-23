from django.db import models

from accounts.models import CustomUser

class Category1(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        
        return self.title
    
class PhotoPost1(models.Model):
    
    #CustomUserモデルのuser_idとPhotoPostを1対多で結びつける。
    #CustomUserが親でPhotoPostが子の関係になる。
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE,
    )
    #CategoryモデルのtitleとPhotoPostを1対多で結びつける
    #Categoryが親でPhotoPostが子の関係になる。
    category = models.ForeignKey(
        Category1,
        verbose_name='カテゴリ',
        #カテゴリに関連付けられた投稿データが存在する場合はそのカテゴリが削除されないようにする
        on_delete=models.PROTECT,
    )
    
    #title用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200, #最大文字数は200文字
    )
    
    #コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',
    )
    
    #イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'photos' #MEDIA_ROOT以下のphotosにファイル保存
    )
    
    #イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to = 'photos',   #MEDIA_ROOT以下のphotosにファイル保存
        blank = True,   #フィールド値の設定は必須ではない
        null = True     #データベースにnullが保存されることを許容
    )
    
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True   #日時を自動追加
    )
    
    def __str__(self):
        #オブジェクトを文字列に変換して返す
        return self.title