from django.shortcuts import render,get_object_or_404
from adminpage.models import draft,herosection,herosectionnews
# Create your views here.
def index(request):
    return render(request,"index.html",{"newnews":draft.objects.all(),"hero":herosection.objects.order_by('newstime')[0],"NHero":herosectionnews.objects.all()})

def news(request,id) :
    show = get_object_or_404(draft, pk=id)
    return render(request, 'news.html',{'show':draft.objects.filter(id=id)})

def bigcard(request,id):
    show = get_object_or_404(draft, pk=id)
    return render(request, 'herosectionnews.html',{'hnews':herosection.objects.filter(id=id)})
def herosectionnewscard(request,id):
    show = get_object_or_404(draft, pk=id)
    return render(request, 'livepage.html',{'hnewscard':herosectionnews.objects.filter(id=id)})

def commingsoon(request):
    return render(request,'commingsoon.html')