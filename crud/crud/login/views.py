from django.shortcuts import render
from .models import Feed, User


def index_page(request):
    feeds_to_render = Feed.objects.order_by('date')
    return render(request, 'login/index.html', {'feeds': feeds_to_render})
