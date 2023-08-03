from django.urls import path
from . import views

urlpatterns = [
    path('spnews/', views.reporterLogin, name='login'),
    path('logout/', views.reporteLogout, name='logout'),
    path('siteadmin/', views.siteAdmin, name='siteadmin'),
    path('siteadmin/draft',views.siteDraft,name='draft'),
    path('siteadmin/approval',views.siteApproval,name='approval'),
    path('siteadmin/siteApprovalDelete/<int:id>/',views.siteApprovalDelete,name='delapproval'),
    path('siteadmin/reject',views.siteReject,name='reject'),
    path('siteadmin/siteRejectDelecte/<int:id>/',views.siteRejectDelecte,name='delreject'),
    path('siteadmin/redraft/<int:id>/',views.siteReDraft,name='redraft'),

    path('msite/',views.mreporterLogin,name='msite'),
    path('msitelogout/',views.reporteLogout,name='msitelogout'),
    path('msiteadmin/', views.msiteAdmin, name='msiteadmin'),
    path('msiteadmin/madminscalen/<int:id>/', views.madminscaleN, name='scalen'),
    path('msiteadmin/utilites', views.utilites, name='utilites'),
]