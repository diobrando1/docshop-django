"""
pdfshop views
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from magic import from_buffer
import fitz

from docshop.settings import BASE_DIR
from pdfshop.forms import SignUpForm
from .forms import UploadFileForm
from .models import PDF



@login_required
def home(request):
    """
    Represents home view
    Returns render with home template
    """
    return render(request, 'pdfshop/home.html')

def signup(request):
    """
    Represents signup view
    When request.method == 'POST':
        * validates the signup form,
        * registers new user,
        * returns redirect to home page
    Otherwise: redirects to the signup form, returns to render with signup template
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'pdfshop/signup.html', {'form': form})

@login_required
def upload(request):
    """
    Represents PDF upload view; works only if the user is logged in
    When request.method == 'POST':
        * validates the upload form,
        * uploads new document,
        * returns redirect to home page
    Otherwise: redirects to the PDF upload form, returns render to upload page
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if mime_type(request.FILES['file']) != 'application/pdf':
                from django.forms.utils import ErrorList
                errors = form._errors.setdefault("file", ErrorList())
                errors.append(u"Must be a PDF file.")
            else:
                pdf = PDF(name=request.POST['title'], path=request.FILES['file'])
                pdf.save()
                img_filename = BASE_DIR+"/pdfshop/static/pdfshop/images/watermark.png"
                print(img_filename)
                img_rect = fitz.Rect(100, 100, 500, 1000)
                print(request.FILES['file'])
                document = fitz.open(BASE_DIR+"/pdf/"+str(request.FILES['file']))
                for _, page in enumerate(document):
                    page.insertImage(img_rect, filename=img_filename)
                document.save(BASE_DIR+"/pdf/watermark/"+str(request.FILES['file']))
                document.close()
                return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'pdfshop/upload.html', {'form': form})

def mime_type(fs_path):
    """
    Check mime type
    :param fs_path:
    :return:
    """
    return from_buffer(fs_path.read(), mime=True)
