from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.forms import CategoryForm

def index(request):
    #query for all categories currently stored
    #order in descending order
    #retrieve the top five
    #place in context dictionary
    #then pass to template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    
    return render(request,'rango/index.html',context=context_dict)

# Create your views here.

from rango.models import Page

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict["pages"] = pages

        context_dict["category"] = category
    except Category.DoesNotExist:
        context_dict["category"] = None
        context_dict["category"] = None

    return render(request, "rango/category.html",  context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)

        else:
            print(form.errors)
    return render(request, "rango/add_category.html", {"form": form})

def about(request):
    aboutString = "Rango says here is the about page"
    context_dict = {"aboutString" : aboutString,
                    "indexLink" : "../"}
    return render(request, "rango/about.html", context_dict)
