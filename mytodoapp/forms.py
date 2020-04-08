from django import forms

class Todoform(forms.Form):
	taskname=forms.CharField(label='Taskname',max_length=100)
	taskdescp=forms.CharField(label='Taskdescp',max_length=600)
	targetdate=forms.DateField(label='Targetdate')


