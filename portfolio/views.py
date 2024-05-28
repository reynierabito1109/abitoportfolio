from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import docx
import os

def home (request):
    return render (request, "portfolio/home.html")

def about (request):
    return render (request, "portfolio/about.html")

def contact (request):
    return render (request, "portfolio/contact.html")

def biodata (request):
    return render (request, "portfolio/biodata.html")

def page2(request):
    return render (request, "portfolio/page2.html")

def biodata(request):
    docx_file_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'biodata.docx')
    doc = docx.Document(docx_file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return render(request, 'portfolio/biodata.html', {'biodata': text})