from django.conf.urls import url
from dfileuploads.views import fileuploadview



urlpatterns = [
    url(r'^fupload/$', fileuploadview, name='file_upload_view'),
]