from django.forms import ModelForm
from .models import PhotoPost1

class PhotoPost1Form(ModelForm):
    #ModelFormのサブクラス
    
    class Meta:
        model = PhotoPost1
        fields = ['category', 'title', 'comment', 'image1', 'image2']
        
#ModelFormクラスはインナークラスのMetaでモデルフィールドを指定するようになってるので
#これをオーバーライドしてモデルPhotopost1とそのフィールドを指定する

#このmodelsをviewsで読み込むようにすれば写真登録ページのテンプレート(フォーム)で入力されたデータを反映することができる。
