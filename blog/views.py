from django.shortcuts import render

# Create your views here.
#this is my first page
def post_list(request):
    return render(request, 'blog/index_2.html', {})

# this function will return the list of data which is there in django list
def list(request):
    return render(request,'blog/list1.html', {})

# this function will be there for to fill a form to the model
