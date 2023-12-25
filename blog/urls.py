from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name="blog-home"),
    path('category/', views.blog_category, name='blog-category'),
    path('category/tech', views.tech, name='blog-tech'),
    path('category/science', views.science, name='blog-science'),
    path('category/reviews', views.movie, name='blog-reviews'),
    path('category/parenting', views.parent, name='blog-parenting'),
    path('category/life', views.life, name='blog-life'),
    path('category/finance', views.finance, name='blog-finance'),
    path('category/entru', views.entru, name='blog-entru'),
    path('category/education', views.edu, name='blog-education'),
    path('category/cook', views.cook, name='blog-cook'),
    path('category/art', views.art, name='blog-art'),
    path('post/<int:pk>/',views.post_detail,name="blog-post"),
    # path('login/',views.login,name="login"),
    # path('profile/<str:username>/', views.profile, name='profile'),

]