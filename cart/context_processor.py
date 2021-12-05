def cart_total(request):

    total=0

    if 'cart' in request.session:

        for key,value in request.session['cart'].items():
            total=total+(float(value['price']))

    return({'total_cart':total})