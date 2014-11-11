from django.shortcuts import render
from django.http import HttpResponse
from fb.models import UserPost

def index(request):
	if(request.method == 'GET'):
		posts = UserPost.objects.all()
		context ={
			'postari':posts,
		}
		return render(request, 'index.html', context)

# Create your views here.
