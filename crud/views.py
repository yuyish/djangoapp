from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
# Create your views here.
def homepage(request):
    blog = Blog.objects.all()
    print(blog)
    # return HttpResponse("Helllo all!. This is Mr.Yuyish first project")
    return render(request,"crud/index.html",{"blogs":blog})

def create(request):
    forms = BlogForm(request.POST or None)
    
    if(forms.is_valid()):
        forms.save()
        return redirect("Home")
    
    return render(request,"crud/create.html",{"forms":forms})
                  