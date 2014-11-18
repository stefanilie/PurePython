from django.shortcuts import render
from django.http import HttpResponse
from fb.models import UserPost
from fb.forms import UserPostForm

def index(request):
	if(request.method == 'GET'):
		posts = UserPost.objects.all()
		form = UserPostForm()
		context ={
			'postari':posts,
			'forms':forms,
		}
		return render(request, 'index.html', context)

# Create your views here.
