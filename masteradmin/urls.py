from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='spadmin'),
    path('eadmin/', views.eDastboard, name='eadmin'),
    path('edraft/', views.eDraft, name='eDraft'),
    path('logout/',views.logout,name="logout"),
    path('newdraft/',views.newDraft,name="nDraft")
]