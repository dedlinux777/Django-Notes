from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#dummy data for testing
# posts = [
#     {
#         'title': 'First Post',
#         'content': 'This is the content of the first post.',
#         'author': 'John Doe',
#         'date_posted': 'June 1, 2024'
#     },
#     {
#         'title': 'Second Post',
#         'content': 'This is the content of the second post.',
#         'author': 'Jane Smith',
#         'date_posted': 'June 2, 2024'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})