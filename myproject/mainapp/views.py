from django.http import HttpResponseRedirect
from django.shortcuts import render
from upload.forms import UploadFileForm
from upload.models import UploadFileModel
# Create your views here.

def home(request):
    ufl = UploadFileModel.objects
    return render(request, 'home.html',{'ufl':ufl})

