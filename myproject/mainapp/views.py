from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from upload.forms import UploadFileForm
from upload.models import UploadFileModel
from .models import category,brand_for_category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    ufl = UploadFileModel.objects
    brand_for_categorys = brand_for_category.objects
    sort = request.GET.get('sort','')

    if sort == 'lowprice':
        ufl = UploadFileModel.objects.all().order_by('lowerlimit')
    elif sort == 'date':
        ufl = UploadFileModel.objects.all().order_by('pub_date')
    elif sort == 'highprice':
        ufl = UploadFileModel.objects.all().order_by('-lowerlimit')
    else:
        ufl =  ufl = UploadFileModel.objects.all()

    product_list = ufl
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
  
    return render(request, 'home.html',{'ufl':ufl, 'posts':posts,'brand_for_categorys':brand_for_categorys})



def choice(request,category_id): #브랜드별 선택
    if category_id:
        selectedcategory = get_object_or_404(brand_for_category,pk=category_id)
        ufl = UploadFileModel.objects.filter(pbrand = selectedcategory.brandname)
    else:
        selectedcategory = None
        ufl = UploadFileModel.objects   

    paginator = Paginator(ufl, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    brand_for_categorys = brand_for_category.objects

    return render(request,'home.html',{'selectedcategory':selectedcategory,'ufl':ufl, 'posts':posts,'brand_for_categorys':brand_for_categorys})




def choice2(request,saletype_id): #판매방식 선택
    pass





def detail(request, product_id):
    details = get_object_or_404(UploadFileModel, pk=product_id)
    return render(request,'detail.html',{'details':details})


@csrf_exempt
@login_required
def auction(request,product_id):

    details = UploadFileModel.objects.get( pk=product_id)
    bidprice = request.POST.get('bidprice', '오류')
    if int(bidprice) < details.lowerlimit and int(bidprice)<= details.bidprice:
        print('하한가, 현재입찰가보다 낮은 가격으로 입찰할 수 없음  이라는 메시지 띄워야함')
        return render(request,'detail.html',{'details':details})
    else:
        details.bidprice = bidprice
        details.biduser = request.user.username
        details.save()
    return render(request,'detail.html',{'details':details})



@login_required
def mypage(request):
    ufl = UploadFileModel.objects.filter(user_id = request.user.username)
    return render(request, 'mypage.html',{'ufl':ufl})

@login_required
def buy(request, product_id):
    productbuy = get_object_or_404(UploadFileModel ,pk=product_id)
    return render(request,'buy.html',{'productbuy':productbuy})
    
@login_required
def pay(request, product_id):
    productpay = get_object_or_404(UploadFileModel ,pk=product_id)
    return render(request,'pay.html',{'productpay':productpay})