from django.shortcuts import redirect, render

from .models import Product

# Create your views here.
def all_products(request):
    products = request.user.get_products()
    
    if request.method == 'POST':
        from random import randint
        name = 'Produto %d' % (len(products) + 1)
        price = randint(500, 5000)
        request.user.set_product(name, price)
        return redirect('Product:all')
    
    return render(request, 'Product/all.html', {'products': products})


def product_delete(request, id):
    product = request.user.get_product(id=id)
    product.delete()
    return redirect('Product:all')
        
        
