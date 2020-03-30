from django import forms
from .models import ParameterModel

class ParameterForm(forms.ModelForm):
	class Meta:
		model = ParameterModel
		fields = [
			'First_Parameter',
			'Second_Parameter',
			'Third_Parameter'
		]