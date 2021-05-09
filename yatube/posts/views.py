import datetime as dt

from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:12]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.groups.all()[:12]
    return render(request, "group.html", {"groups": group, "posts": posts})


def year(request):
    years = {"year": dt.datetime.today().year}
    template = "footer.html"
    return render(request, template, years)
