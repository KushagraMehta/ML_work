from django import forms


class BreastCancerForm(forms.Form):
	rad = forms.FloatField(label="Mean Radius:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	tex = forms.FloatField(label="Mean Texture:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	per = forms.FloatField(label="Mean Perimeter:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	area = forms.FloatField(label="Mean Area: ", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	smo = forms.FloatField(label="Mean Smoothness:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	com = forms.FloatField(label="Mean Compactness:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	conc = forms.FloatField(label="Mean Concavity:",widget=forms.TextInput(attrs={'placeholder': 'Search'}) )
	conpt = forms.FloatField(label="Mean Concave points:",widget=forms.TextInput(attrs={'placeholder': 'Search'}) )
	sym = forms.FloatField(label="Mean Symmetry:",widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	frac = forms.FloatField(label="Mean Fractal Dimension: ",widget=forms.TextInput(attrs={'placeholder': 'Search'}))