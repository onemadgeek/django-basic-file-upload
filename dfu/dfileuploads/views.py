# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import *
from django.shortcuts import render

from .forms import FileUploadForm
# Create your views here.



def fileuploadview(request):
    """Dummmy File Upload View Improve"""
    if request.method == 'POST' and request.FILES['file']:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES['file']
            #Handle the file save and redirect to success url.
            #return HttpResponseRedirect('/')
    else:
        form = FileUploadForm()
    return render(request, 'dfileuploads/fileupload_edit.html', {'form' : form})