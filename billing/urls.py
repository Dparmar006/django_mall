from django.urls import path
from . import views

urlpatterns = [
    path("AddCustomer/", views.AddCustomer, name="Adding Customer")
]
