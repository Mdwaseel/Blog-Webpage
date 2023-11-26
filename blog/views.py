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
     form = PostModelForm
     if request.method == 'POST':
         form = PostModelForm(request.POST)
         if form.is_valid():
             instance = form.save(commit=False)
             instance.author = request.user
             instance.save()
     else: 
         form = PostModelForm()
         
     content = {
          'posts':Post.objects.all(),
            'form': form

     }
     return render(request,'blog/home.html',content)

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