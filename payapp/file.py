from django.shortcuts import render
import requests

# Create your views here.

def index(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		amount = request.POST.get('amount')
		reference = '213rYWo0ppaa45'
		SECRET_KEY = 'sk_test_69d976993d868a70852628ff1067b7d9949dd195'
		headers = {
		    'Content-Type': "application/json",
		    "Authorization": "Bearer " + SECRET_KEY
		}
		payload = {
		    "reference": reference,
		    "amount": amount,
		    "email": email
		}
		paystack_response = requests.post('https://api.paystack.co/transaction/initialize',
		                                  json=payload, headers=headers).json()
		print(paystack_response)
	return render(request, 'theme/index.html')
