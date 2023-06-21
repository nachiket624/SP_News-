from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import News
from .forms import DraftNews, ReDraftNews


def reporterLogin(request):
    if request.user.is_authenticated:
        return redirect('siteadmin')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def reporteLogout(request):
    logout(request)
    return redirect('login')
    

@login_required
def siteAdmin(request):
    return render(request, "adminindex.html")

@login_required
def siteDraft(request):
    if request.method == 'POST':
        form = DraftNews(request.POST, request.FILES)
        if form.is_valid():
            news.status = "APPROVAL"
            form.save()
            return redirect('approval')
    else:
        form = DraftNews()
        context = {
            'form': form,
        }
        return render(request, "admindraft.html", context)
    context = {
        'form': form,
    }
    return render(request, "admindraft.html", context)

@login_required
def siteReject(request):
    return render(request, "adminreject.html", {"rejectitem": News.objects.filter(status="REJECT")})

@login_required
def siteApproval(request):
    return render(request, "admininapproval.html", {"aprovalitem": News.objects.filter(status="APPROVAL")})

@login_required
def  siteApprovalDelete(request, id):
    DelApprovalRequest = News.objects.get(id=id)
    DelApprovalRequest.delete()
    return redirect('approval')

@login_required
def siteReDraft(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        form = ReDraftNews(request.POST, instance=news)
        if form.is_valid():
            news.status = "APPROVAL"
            form.save()
            return redirect('reject')
    else:
        form = ReDraftNews(instance=news)

    return render(request,
                  'adminredraft.html',
                  {'form': form})
