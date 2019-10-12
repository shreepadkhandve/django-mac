from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

import PyPDF2
import tabula
import slate3k as slate
import os
from os import listdir
from os.path import isfile, join
# Create your views here.

def index(request):
    products = Product.objects.all() 
    
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))

    # params = {'no_of_slides':nslides,'range':range(1,nslides), 'product':products}
    allProds = [[products,range(1,nslides),nslides],
               [products,range(1,nslides),nslides]]
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse('We are at contact')

def tracker(request):
    return HttpResponse('We are at tracker')

def search(request):
    return HttpResponse('We are at search')

def prodview(request):
    return HttpResponse('We are at prodview')

def checkout(request):
    return HttpResponse('We are at checkout')


def pdf(request):
    for i in os.listdir('C:\pdf_to_text'):

        if i.endswith('pdf'):
            object1 = PyPDF2.PdfFileReader(f'C:\pdf_to_text\{i}')
        
            NumPages = object1.getNumPages()
            with open(i,'rb') as f:
                extracted_text = slate.PDF(f)
    
                for j in range(NumPages):
    
                    if "BALANCE SHEET AS AT 31ST MARCH" in extracted_text[j]:
                        df=tabula.read_pdf(i,pages=j+1,area=[110,50,540,800])
                        df.to_excel(f"C:\pdf_to_text\{i}.xlsx")
                        
                    elif "Balance Sheet As At 31st March" in extracted_text[j]:
                        df=tabula.read_pdf(i,pages=j+1,area=[110,50,540,800])
                        df.to_excel(f"C:\pdf_to_text\{i}.xlsx")
                    if "Balance Sheet As at 31st March" in extracted_text[j]:
                        df=tabula.read_pdf(i,pages=j+1,area=[110,40,540,800])
                        df.to_excel(f"C:\pdf_to_text\{i}.xlsx")
                    elif "Consolidated Balance Sheet As At 31st March" in extracted_text[j]:
                        df=tabula.read_pdf(i,pages=j+1,area=[110,50,540,800])
                        df.to_excel(f"C:\pdf_to_text\Consolidated{i}.xlsx")
                    elif "Consolidated Balance Sheet As at 31st March" in extracted_text[j]:
                        df=tabula.read_pdf(i,pages=j+1,area=[110,40,540,800])
                        df.to_excel(f"C:\pdf_to_text\Consolidated{i}.xlsx")
                    else:
                        pass
    

print("git Demo")


print('git git git git')

