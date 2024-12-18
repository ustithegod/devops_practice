from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404
from .models import Post, Category
# Create your views here.


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )[:5]

    return render(request, template, {'post_list': post_list})


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=post_id, pub_date__lte=timezone.now(),
        is_published=True, category__is_published=True
    )

    return render(request, template, {'post': post})


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug, is_published=True
    )
    post_list = Post.objects.all().filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category,
    )

    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
