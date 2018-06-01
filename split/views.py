from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import *

@login_required(login_url='/split/login/')
def profile(request):

	user = request.user
	print user.username
	print UserProfile.objects.all()
	return HttpResponse("Hello, world. You're at the polls index.")