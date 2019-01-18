from django.shortcuts import render
from .diabetes_forms import DiabetesForm
from .breastcancer_form import BreastCancerForm
from .ML_script_breastcancer import cancer_cal
from .ML_script_diabetes import diabetes_cal
from django.views.generic import TemplateView

# Create your views here.
posts=[
	{
		'title':'Diabetes Calculator',
		'content':" Diabetes is a condition that impairs the body's ability to process blood glucose, otherwise known as blood sugar.In the United States, the estimated number of people over 18 years of age with diagnosed and undiagnosed diabetes is 30.2 million. The figure represents between 27.9 and 32.7 percent of the population. Without ongoing, careful management, diabetes can lead to a buildup of sugars in the blood, which can increase the risk of dangerous complications, including stroke and heart disease.  ",
		'link': 'diabetes/'
	},
	{
		'title':'Breast Cancer Calculator',
		'content':"Cancer occurs when changes called mutations take place in genes that regulate cell growth. The mutations let the cells divide and multiply in an uncontrolled, chaotic way. The cells keep multiplying, producing copies that get progressively more abnormal. In most cases, the cell copies eventually form a tumor. ",
		'link': 'BreastCancer/'
	}
]
def home(request) :
	context={
		'key1': posts
	}
	return render(request, 'blog/home.html',context)

class diabetes(TemplateView) :
	template_name='blog/diabetes.html'

	def get(self, request):
		diabetes_form = DiabetesForm()
		return render(request,self.template_name,{'form':diabetes_form})
		
	def post(self, request):
		diabetes_form = DiabetesForm(request.POST)
		if diabetes_form.is_valid():
			data=[]
			data.append(diabetes_form.cleaned_data['prag'])
			data.append(diabetes_form.cleaned_data['plas'])
			data.append(diabetes_form.cleaned_data['bldprs'])
			data.append(diabetes_form.cleaned_data['skin'])
			data.append(diabetes_form.cleaned_data['serum'])
			data.append(diabetes_form.cleaned_data['BMI'])
			data.append(diabetes_form.cleaned_data['pedigree'])
			data.append(diabetes_form.cleaned_data['age'])

			print("#########"+str(diabetes_cal().accuracy())+"#########")
			result_dtree,result_knn=diabetes_cal().result(data)
			accuracy_dtree,accuracy_knn=diabetes_cal().accuracy()
			return render(request,self.template_name,{'form':diabetes_form,'Rdtree':result_dtree,'Rknn':result_knn,'Adtree':accuracy_dtree,'Aknn':accuracy_knn})

	
	
class BreastCancer(TemplateView) : 
	template_name='blog/BreastCancer.html'

	def get(self, request):
		BreastCancer_form = BreastCancerForm()
		return render(request,self.template_name,{'form':BreastCancer_form})

	def post(self, request):
		BreastCancer_form = BreastCancerForm(request.POST)
		if BreastCancer_form.is_valid():
			data=[]
			data.append(BreastCancer_form.cleaned_data['rad'])
			data.append(BreastCancer_form.cleaned_data['tex'])
			data.append(BreastCancer_form.cleaned_data['per'])
			data.append(BreastCancer_form.cleaned_data['area'])
			data.append(BreastCancer_form.cleaned_data['smo'])
			data.append(BreastCancer_form.cleaned_data['com'])
			data.append(BreastCancer_form.cleaned_data['conc'])
			data.append(BreastCancer_form.cleaned_data['conpt'])
			data.append(BreastCancer_form.cleaned_data['sym'])
			data.append(BreastCancer_form.cleaned_data['frac'])


			result_dtree,result_knn=diabetes_cal().result(data)
			accuracy_dtree,accuracy_knn=diabetes_cal().accuracy()
			return render(request,self.template_name,{'form':BreastCancer_form,'text':result})



def about(request) :
	return render(request, 'blog/about.html',{'title':'about'})