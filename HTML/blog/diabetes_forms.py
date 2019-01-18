from django import forms


class DiabetesForm(forms.Form):
	prag =forms.FloatField(label='Number of times pregnent:')
	plas = forms.FloatField(label='Plasma glucose concentration')
	bldprs = forms.FloatField(label='Diastolic blood pressure:')
	skin = forms.FloatField(label='Triceps skin fold thickness:')
	serum = forms.FloatField(label='2-Hour serum insulin:')
	BMI = forms.FloatField(label='Body mass index: ')
	pedigree = forms.FloatField(label='Diabetes pedigree function: ')
	age = forms.FloatField(label='Age: ')

