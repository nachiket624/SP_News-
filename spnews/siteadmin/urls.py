from django.urls import path
from . import views

urlpatterns = [
    path('siteadmin', views.siteAdmin, name='siteadmin'),
    path('siteadmin/draft',views.siteDraft,name='draft'),
    path('siteadmin/approval',views.siteapproval,name='approval'),
    path('siteadmin/reject',views.sitereject,name='approval'),
]