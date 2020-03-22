from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect

from .forms import UploadFileForm, UploadZipFileForm
from .models import Image
from zipfile import *

# Create your views here.

def upload_single_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/success/url/')
	else:
		form = UploadFileForm()
	return render(request, 'form.html', {'form': form})

def upload_multiple_file(request):
	return HttpResponse("Multiple Files")

def upload_zip_file(request):
    if request.method == 'POST':
    	form = UploadZipFileForm(request.POST, request.FILES)
    	if form.is_valid():
    		handlezipfile(request.FILES['file'])
    		return HttpResponseRedirect('/upload_successful')
    else:
    	form = UploadZipFileForm()
    	return render(request, 'form.html', {'form': form})

def handlezipfile(zipfile):
	file_name = zipfile
	with ZipFile(file_name, 'r') as zip:
		# printing all the contents of the zip file
		zip.printdir()
		namelist = zip.namelist()
		for filename in namelist:
			file = Image()
			file.name = filename
			file.save()
		# extracting all the files
		print('Extracting all the files now...')
		zip.extractall() 
		print('Done!') 

	# for filename,content in fileiterator(zipfile):
	# 	tf = TextFile()
	# 	tf.content = c
	# 	tf.filename = filename
	# 	tf.save()