from django.urls import path
from .import views

urlpatterns = [

    path('<int:id>',views.details, name = "detail"),
    path('rooms.html',views.full_Detail, name='full_Detail'),
    path('new',views.new, name="new")





]
