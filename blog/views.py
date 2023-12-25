from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_user
from .models import Post,User
from django.contrib import messages
from .forms import PostModelForm
from django.views.generic import DetailView 
# Create your views here.


def home(request):
     tech = Post.objects.filter(category='Technology').order_by('-date_uploaded')
     edu = Post.objects.filter(category='Education').order_by('-date_uploaded')
     life = Post.objects.filter(category='Lifestyle').order_by('-date_uploaded')
     finance = Post.objects.filter(category='Finance').order_by('-date_uploaded')
    
     content = {
          'tech':tech,
          'edu':edu,
          'life':life,
          'finance':finance,
            

     }
     return render(request,'blog/home.html',content)


def blog_category(request):
    # Your view logic goes here
    return render(request, 'blog/category.html')

def tech(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/tech.html')

def science(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/science.html')

def parent(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/parent.html')

def life(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/life.html')

def finance(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/finance.html')

def entru(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/entru.html')

def edu(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/edu.html')

def cook(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/cook.html')

def art(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/art.html')

def movie(request):
    # Your view logic goes here
    return render(request, 'blog/catogery/reviews.html')



@login_required
def myblogs(request):
      if request.user.is_authenticated:
          user_posts = Post.objects.filter(author=request.user).order_by('-date_uploaded')
          Posts = {
              'user_posts' : user_posts,
          }
          return render(request,'blog/myblog.html',Posts )

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         print(f'Attempting login with username: {username} and password: {password}')
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             auth_user(request,user)
#             print(f'Authenticated user: {user}')
#             messages.success(request,'login Succesfull')
#             return redirect('blog-home')
#         else:
#             messages.error(request, 'Invalid login credentials.')
    

#     return render(request,'blog/login.html')





@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # Handle the case where the requested user does not exist
        # You can return a 404 page or a custom error message
        return render(request, 'blog/error.html')

    return render(request, 'blog/profile.html', {'user': user})

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request,'blog/blog.html',context)