from django.urls import path
from . import views

urlpatterns = [
   path("",views.index.as_view(),name="index"),

   path('<pk>/',views.details.as_view(),name="details"),


]
