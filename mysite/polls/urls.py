from django.urls import path
from . import views

# The next step is to point the root URLconf at the polls. urls module. In mysite/urls.py,add an import for django.urls include and insert an  include() in the urlpatterns list, so you have:
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # URL confの修正
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # 送信されたデータを処理するためのDjangoのビュー
    path('<int:question_id>/vote/', views.vote, name='vote'),
]