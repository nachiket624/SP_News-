from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:id>/',views.news,name="news"),
    path('hilight/<int:id>/',views.bigcard,name='herosection'),
    path('Bnews/<int:id>',views.herosectionnewscard,name='herosectioncard'),
    path('page',views.commingsoon,name='commingsoon'),
]