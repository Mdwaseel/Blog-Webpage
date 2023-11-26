from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name="blog-home"),
    path('myblogs/',views.myblogs,name="blog-myblogs"),
    path('post/<int:pk>/',views.post_detail,name="blog-post"),
    # path('login/',views.login,name="login"),
    # path('profile/<str:username>/', views.profile, name='profile'),

]