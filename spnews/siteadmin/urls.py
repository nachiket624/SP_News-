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
    path('siteadmin/redraft/<int:id>/',views.siteReDraft,name='redraft'),
]