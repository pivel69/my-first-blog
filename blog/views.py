from django.shortcuts import render
from django.utils import timezone
from .models import Clanky

def post_list(request):
    posts = Clanky.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
