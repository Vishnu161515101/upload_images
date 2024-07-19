from django.urls import path,include
from . import views

urlpatterns = [

    path('upload_image',views.upload_image,name='upload_image'),
    
]
