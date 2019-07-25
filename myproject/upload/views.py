from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadFileModel
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import mainapp.views
import mainapp.models


#originalprice만 변경하면 된다. 내가 등록한 물건에서 가져오기

@login_required
def upload_file(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.username
            post.originalprice = 9999
            post.productimg_name = str(post.pbrand)+''+str(post.pitem)
            post.save()
            ufl = UploadFileModel.objects
            return render(request, 'home.html', {'ufl': ufl})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
