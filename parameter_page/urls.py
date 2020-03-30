from django.urls import path
from .views import ParameterCreate,ParameterDetail

app_name = "parameter_page"

urlpatterns = [
	path('create/',ParameterCreate.as_view()),
	path('detail/<int:id>/',ParameterDetail.as_view())
]