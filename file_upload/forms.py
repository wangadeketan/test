from django import forms

class UploadFileForm(forms.Form):
	"""docstring for ClassName"""
	title = forms.CharField(max_length=100)
	file = forms.FileField()

class UploadZipFileForm(forms.Form):
	file = forms.FileField()