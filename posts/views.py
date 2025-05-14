from django.shortcuts import render
from .models import Post
# Create your views here.
def postView(request):
    posts = Post.objects.all()
    return render(request, 'posts/assignment.html', {'posts': posts})
