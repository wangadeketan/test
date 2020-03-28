from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .forms import UploadFileForm, UploadZipFileForm
from .models import Image, Batch
from zipfile import *

# Create your views here.

class Listing(SingleObjectMixin, ListView):
	paginate_by = 1
	template_name = "file_upload/form_data.html"

	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Image.objects.all())
		return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['image'] = self.object
		return context

	def get_queryset(self):
		return self.object.book_set.all()

def listing(request):
    image_name = Image.objects.all()
    paginator = Paginator(image_name, 1) # Show 1 Image per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'form_data.html', {'page_obj': page_obj})

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
    		return render(request, 'form_data.html')
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


