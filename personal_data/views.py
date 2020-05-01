from django.shortcuts import render
from .models import project
# Create your views here.
def firsttitle(request):
    projects=project.objects.all()
    return render(request,'allfold/fisttitle.html',{'projects':projects})
def firsttitle2(request):
    return render(request,'allfold/fisttitle2.html')
