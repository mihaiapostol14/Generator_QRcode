from django.urls import path
from . import views

app_name = 'generator' # 👈 THIS IS THE NAMESPACE

urlpatterns = [
    path('', views.QRCodeCreateView.as_view(), name='generator'),
]