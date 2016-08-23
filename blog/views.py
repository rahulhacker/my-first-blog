from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


# Create your views here.
#this is my first page
def home(request):
    return render(request, 'blog/index_2.html', {})


def post_list(request):
    return render(request, 'blog/post_list.html', {})

# this function will return the list of data which is there in django list
def list(request):
    queryset=Profile.objects.all()
    context={
     "object_list" :queryset,
     "title":"list"
    }
    return render(request,'blog/list1.html',context)



def save(request):

    instance = Profile(name=request.POST["name"],email=request.POST["email"],resume=request.FILES['resume'])
    instance.save()
    return render(request, 'blog/post_list.html')

# this function will be there for to fill a form to the model
