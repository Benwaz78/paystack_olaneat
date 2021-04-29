from django.shortcuts import render, redirect, get_object_or_404
from pypaystack import Transaction, Customer, Plan
from django.conf import settings
from payapp.models import *
from django.http import JsonResponse
import requests
import random

# Create your views here.

def index(request):
	books = Book.objects.all()
	return render(request, 'theme/index.html', {'book':books, 'public':settings.PAYSTACK_PUBLIC_KEY})

def book_detail(request, book_id):
	book_detail = Book.objects.get(id=book_id)
	return render(request, 'theme/detail.html', {'detail':book_detail})

def checkout_pay(request, book_id):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		book_obj = Book.objects.get(id=book_id)
		amount = book_obj.price
		Payment.objects.create(first_name=first_name, last_name=last_name, email=email, book=book_obj)
		print('Success')
		return render(request, 'theme/payment.html', {'detail':book_detail, 'public':settings.PAYSTACK_PUBLIC_KEY, 'email':email, 'amount':amount})
	return render(request, 'theme/payment.html')

def verify(request, pid):
	transaction = Transaction(authorization_key=settings.PAYSTACK_SCRET_KEY)
	response=transaction.verify(pid)
	book = get_object_or_404(Book, id=pid)
	return redirect('book_download', pk=book.pk)

def book_download(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	return render(request, 'theme/download.html', {'book':book})





# def index(request):
# 	transaction = Transaction(authorization_key=settings.PAYSTACK_SCRET_KEY)
# 	return render(request, 'theme/index.html', {'public':settings.PAYSTACK_PUBLIC_KEY})

# def post_data(request):
# 	return render(request, 'theme/post.html')

# def verify(request, pid, prod_id=None):
# 	transaction = Transaction(authorization_key=settings.PAYSTACK_SCRET_KEY)
# 	response=transaction.verify(pid)
# 	product = get_object_or_404(MyData, id=prod_id)
# 	return redirect('payment', pk=product.pk)

	

