from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)
from .forms import ParameterForm
from .models import ParameterModel
from .completion_step import write_into

#Lookup Detail of Parameter Form
class ParameterDetail(DetailView):
	template_name = 'parameter_detail.html'
	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(ParameterModel,id = id_)
		return obj

# Create Parameter Form
class ParameterCreate(View):
	template_name = 'parameter_create.html'
	def get(self,request,*args,**kwargs):
		#Get method
		form = ParameterForm()
		context = {"form":form}
		return render(request,self.template_name,context)
	
	def post(self,request,*args,**kwargs):
		#grabbing request.post 
		form = ParameterForm(request.POST)
		if form.is_valid():
			#Forms only get a cleaned_data attribute when is_valid() has been called
			cleandata = form.cleaned_data
			write_into(cleandata)
			form.save()
			form = ParameterForm()
		context = {"object":cleandata}
		return render(request,'parameter_detail.html',context)

