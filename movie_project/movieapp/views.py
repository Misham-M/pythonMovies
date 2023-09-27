from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movie_list=Movie.objects.all()
    context={
        'movie':movie_list
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})
    # return HttpResponse("movie no is %s" %movie_id)

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']

        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'movie':movie,'form':form})

def delete(request,id):
    if request.method == "POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
