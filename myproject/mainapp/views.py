from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from upload.forms import UploadFileForm
from upload.models import UploadFileModel
from .models import category
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    ufl = UploadFileModel.objects
    categorys = category.objects 
    

    #상품 4개를 한 페이지에 출력
    product_list = UploadFileModel.objects.all()
    paginator = Paginator(product_list, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
  

    return render(request, 'home.html',{'ufl':ufl, 'posts':posts,'categorys':categorys})



def choice(request,category_id): 
    if category_id:
        selectedcategory = get_object_or_404(category,pk=category_id)
        ufl = UploadFileModel.objects.filter(pbrand = selectedcategory.brand)
    else:
        selectedcategory = None
        ufl = UploadFileModel.objects   

    paginator = Paginator(ufl, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    categorys = category.objects


    return render(request,'home.html',{'selectedcategory':selectedcategory,'ufl':ufl, 'posts':posts,'categorys':categorys})


def detail(request, product_id):
    details = get_object_or_404(UploadFileModel, pk=product_id)
    return render(request,'detail.html',{'details':details})


