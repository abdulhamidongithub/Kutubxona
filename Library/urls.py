from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('man/', man),
    path('loyiha/', loyiha),
    path('', asosiy),
    path('kitoblar/', kitoblar),
    path('mualliflar/', mualliflar),
    path('muallif-t/<int:pk>/', muallif_edit),
    path('kitob/<int:son>/', kitob_ochir),
    path('record/', records),
    path('record_edit/<int:pk>/', record_edit),
    path('kitob_edit/<int:a>/', kitob_edit),
    path('studentlar/', studentlar),
]

