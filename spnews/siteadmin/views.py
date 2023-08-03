from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import News,ChoiseListCategory,ChoiseListSection
from .forms import DraftNews, ReDraftNews
from django.utils.timezone import now
from website.models import MainNews

""" initCatSec() setup application of initial use 
this function insert default value in database """ 

def initCatSec():
    CatobjCount = ChoiseListCategory.objects.count()
    SecObjCount = ChoiseListSection.objects.count()
    Sec = ['Main Page Hero Horizontal','Main Page Hero slide 1','Main Page Hero slide 2','Main Page Hadding News','Main Page Sport News','Main Page Polites News']
    SecValue = ['Main Page Hero Horizontal','Main Page Hero slide 1','Main Main Page Hero slide 2 ','Main Page Hadding News','Main Page Sport News','Main Page Polites News']
    Cat = ['Sport','Education']
    CatValue = ['Sport','Education']
    if CatobjCount <= 0:
        for i in range(len(Cat)):
            intiCat = ChoiseListCategory(category = Cat[i],categoryvalue = CatValue[i])
            intiCat.save()
    if SecObjCount <= 0:
        for i in range(len(Sec)):
            initSec = ChoiseListSection(section = Sec[i],sectionvalue = SecValue[i])
            initSec.save()
            
def reporterLogin(request):
    if request.user.is_authenticated:
        return redirect('siteadmin')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


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
            current_user = request.user
            obj = form.save(commit=False)
            obj.status = "APPROVAL"
            obj.author = str(current_user)
            obj.save()
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
    current_user = request.user
    return render(request, "adminreject.html", {"rejectitem": News.objects.filter(status="REJECT", author=current_user).order_by('date')})


@login_required
def siteRejectDelecte(request, id):
    DelRejectRequest = News.objects.get(id=id)
    DelRejectRequest.delete()
    return redirect('reject')


@login_required
def siteApproval(request):
    current_user = request.user
    return render(request, "admininapproval.html", {"aprovalitem": News.objects.filter(status="APPROVAL", author=current_user).order_by('-date')})


@login_required
def siteApprovalDelete(request, id):
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


# ! Main Admin Views start from here

def mreporterLogin(request):
    if request.user.is_authenticated:
        return redirect('msiteadmin')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def reporteLogout(request):
    logout(request)
    return redirect('msite')

@login_required
def msiteAdmin(request):    
    return render(request, "madminindex.html", {"madminrequest": News.objects.filter(status="APPROVAL").order_by('-date')})


@login_required
@csrf_exempt
def madminscaleN(request,id):
    pres = MainNews()
    news = News.objects.get(id=id)
    if 'rejectform' in request.POST:
       reject = request.POST.get('Rejectrep')
       news.rejectreason = reject
       news.status = "REJECT"
       news.save()
       return redirect('msiteadmin')
    if 'acceptform' in request.POST:
        pres.headding = news.headding
        pres.para1 = news.para1
        pres.para2 = news.para2
        pres.img = news.img
        pres.tag = news.tag
        pres.location = news.location
        pres.date = news.date
        pres.author = news.author
        section = request.POST.get('topage')
        category = request.POST.get('tocat')
        pres.section = section
        pres.category = category
        pres.save()
        news.status = "APPROVE"
        news.save()
        return redirect('msiteadmin')
    return render(request, "madminscalmailn.html",{"scalen": News.objects.filter(pk=id),'sectiondrop':ChoiseListSection.objects.all(),'categoriesdrop':ChoiseListCategory.objects.all()})

@login_required
@csrf_exempt
def utilites(request):
    if 'btn_categories' in request.POST:
        ctor = request.POST.get('inputcategories')
        choise = ChoiseListCategory()
        choise.category = ctor
        choise.categoryvalue = ctor
        choise.save()
        return redirect('utilites')
    if 'btn_Section' in request.POST:
        sec = request.POST.get('inputsection')
        choise = ChoiseListSection()
        choise.section = sec
        choise.sectionvalue = sec
        choise.save()
        Catchoise = ChoiseListCategory()
        Catchoise.category = sec
        Catchoise.categoryvalue = sec
        Catchoise.save() 
        return redirect('utilites')
    return render(request,"utilites.html",{'categorieslist':ChoiseListCategory.objects.all(),'sectionlist':ChoiseListSection.objects.all()})




initCatSec()