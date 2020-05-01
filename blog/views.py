from django.shortcuts import render, get_object_or_404
from .models import project1
# Create your views here.
def all_fold(request):
    projects= project1.objects.all()
    return render(request,'blog/all_fold.html',{'projects':projects})


def detail(request, blog_id):
    blogs=get_object_or_404(project1, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogs})
