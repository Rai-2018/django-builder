from django.shortcuts import render

# Create your views here.
def home_page(request,*args,**kwargs):
	return render(request,"home_page.html",{})