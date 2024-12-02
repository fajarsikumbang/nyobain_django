# shop/views.py
from django.shortcuts import render, redirect
import requests

def product_list(request):
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = product_response.json()

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'title': product['title'],
            'price': product['price'],
            'image': product['image'],
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('product_list')

def cart_detail(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'shop/cart_detail.html', {'cart': cart, 'total': total})
