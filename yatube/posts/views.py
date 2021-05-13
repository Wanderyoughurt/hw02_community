from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post, User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "index.html", {"page": page})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"groups": group, "page": page})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = user.posts.all()
    post_count = user_posts.count()
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "profile.html", {"user": user,
                  "post_count": post_count, "page": page}
                  )


def post_view(request, username, post_id):
    user = get_object_or_404(User, username=username)
    user_posts = user.posts.all()
    post_count = user_posts.count()
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"post": post,
                  "user": user, "post_count": post_count}
                  )
