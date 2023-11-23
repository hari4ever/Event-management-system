from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('login/', views.loginpage,name = 'login'),
    path('signup/', views.signuppage,name = 'signup'),
    path('final', views.final,name = 'final'),
    path('data', views.data, name='data'),
    # path('shome', views.shome, name='shome'),

]
