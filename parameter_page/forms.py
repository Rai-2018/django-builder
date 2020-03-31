from django import forms
from .models import ParameterModel

Choice_Of_Day = [
	(1,'Monday'),
	(2,'Tuesday'),
	(3,'Wednesday'),
	(4,'Thursday'),
	(5,'Friday'),
	(6,'Saturday'),
	(7,'Sunday')
]

class ParameterForm(forms.ModelForm):
	Third_Parameter = forms.ChoiceField(choices= Choice_Of_Day)

	class Meta:
		model = ParameterModel
		fields = [
			'First_Parameter',
			'Second_Parameter',
			'Third_Parameter'
		]
