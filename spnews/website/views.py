from django.shortcuts import render,get_object_or_404
from siteadmin.models import ChoiseListCategory,rebine
from .models import MainNews

def index(request):

    return render(request,"index.html",{'Category':ChoiseListCategory.objects.all()[:4],'categorydrop':ChoiseListCategory.objects.all()[4:],'redin':rebine.objects.all(),'indexse1': MainNews.objects.filter(section = "Main Page Hero Horizontal").order_by('-date')[:1],'indexse2':MainNews.objects.filter(section = 'Main Page Hero slide 1').order_by('-date')[:1],'indexse3':MainNews.objects.filter(section = 'Main Page Hero slide 2').order_by('-date')[:1],'indexse4':MainNews.objects.filter(section = 'Main Page Hadding News').order_by('-date'),'indexse5':MainNews.objects.filter(section = 'Main Page Sport News').order_by('-date'),'indexse6':MainNews.objects.filter(section = 'Main Page Polites News').order_by('-date')})

def detail(request,id):
    return render(request,'detail.html',{'Category':ChoiseListCategory.objects.all()[:4],'categorydrop':ChoiseListCategory.objects.all()[4:],'showD':MainNews.objects.filter(id=id)})