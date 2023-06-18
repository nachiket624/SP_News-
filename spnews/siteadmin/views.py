from django.shortcuts import render, HttpResponse
from .models import News
from .forms import DraftNews


def siteAdmin(request):
    return render(request, "adminindex.html")


def siteDraft(request):
    if request.method == 'POST':
        form = DraftNews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your review has been taken')
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

def siteapproval(request):
    return render(request,"admininapproval.html")

def sitereject(request):
    return render(request,"adminreject.html")
