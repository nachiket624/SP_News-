from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from website.views import index
from adminpage.models import draft
import datetime


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "masteradmin/login.html", context)
        login(request, user)
        return redirect('masteradmin/login.html')
    return render(request, "masteradmin/login.html")


@login_required(login_url='spadmin')
def eDastboard(request):
    return render(request, "masteradmin/editorDashboard.html")


@login_required(login_url='spadmin')
def eDraft(request):
    return render(request, "masteradmin/editordraft.html",)


def logout(request):
    auth.logout(request)
    return render(request, "index.html")


@login_required(login_url='spadmin')
def newDraft(request):
    # return render(request, "masteradmin/editorDashboard.html")
    print("Function Called")
    if request.method == "POSt":
        ToPage = request.POST.get("typepage")
        Thumbnail = request.POST.get("myfile")
        NewsTitle = request.POST.get("newstitle")
        NewsTitlePara1 = request.POST.get("para1")
        NewsTitlePara2 = request.POST.get("para2")
        newstime = datetime.datetime.now()
        newsauthor = "News Author"
        status = "Draft"
        print(ToPage,Thumbnail,NewsTitle,NewsTitlePara1,NewsTitlePara2)
        post = draft(newspage=ToPage,newsthumbnail=Thumbnail,newstitle=NewsTitle,newspara1=NewsTitlePara1,newspara2=NewsTitlePara2,newstime=newstime,newsauthor=newsauthor,status=status)
        post.save()
        return render(request, "masteradmin/editorDashboard.html")
    else:
        print("something went worng")