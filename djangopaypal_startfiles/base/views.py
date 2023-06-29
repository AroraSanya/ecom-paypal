# from django.shortcuts import render
# from django.http import JsonResponse
# import json
# from .models import Product

# # Create your views here.

# def simpleCheckout(request):
# 	return render(request, 'base/simple_checkout.html')

# def store(request):
# 	products = Product.objects.all()
# 	context = {'products':products}
# 	return render(request, 'base/store.html', context)

# def checkout(request, pk):
# 	product = Product.objects.get(id=pk)
# 	context = {'product':product}
# 	return render(request, 'base/checkout.html', context)

# def paymentComplete(request):
# 	body = json.loads(request.body)
# 	print('BODY:', body)
# 	return JsonResponse('Payment completed!', safe=False)


import braintree

from django.shortcuts import render, redirect

def checkout(request):
    if request.method == 'POST':
        # Get the payment nonce from the request
        payment_nonce = request.POST.get('payment_nonce')

        # Create a Braintree transaction
        result = braintree.Transaction.sale({
            'amount': '10.00',
            'payment_method_nonce': payment_nonce,
            'options': {
                'submit_for_settlement': True
            }
        })

        # Process the transaction result
        if result.is_success:
            # Payment successful
            transaction_id = result.transaction.id
            # Perform further actions, such as storing the transaction ID and updating the order status
            return redirect('success')
        else:
            # Payment failed
            error_message = result.message
            # Handle the error appropriately, such as displaying an error message to the user
            return redirect('failure')

    # Render the checkout form template
    return render(request,'custom.html')
# def success(request):
#     # Handle successful payment
#     return render(request, 'success.html')

# def failure(request):
#     # Handle failed payment
#     return render(request, 'failure.html')
