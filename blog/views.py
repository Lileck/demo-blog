from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
     from .models import Post, Category

     def post_list(request):
         posts = Post.objects.all()
         return render(request, 'blog/post_list.html', {'posts': posts})

     def post_detail(request, category_slug, slug):
         post = get_object_or_404(Post, slug=slug, category__slug=category_slug)
         return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
