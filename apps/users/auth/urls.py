from django.urls import include, path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('test/', views.TestAPIView.as_view(), name='test'),

]