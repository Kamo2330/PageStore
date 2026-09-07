from django.contrib import messages
from django.shortcuts import redirect, render

from .catalog import PRODUCTS, filter_products, get_product


def index(request):
    arrivals = [p for p in PRODUCTS if p.get("badge") == "New"][:4]
    sale = [p for p in PRODUCTS if p.get("compare_at")][:4]
    return render(
        request,
        "store/index.html",
        {
            "arrivals": arrivals,
            "sale_items": sale,
        },
    )


def shop(request):
    products = filter_products(request.GET)
    return render(
        request,
        "store/shop.html",
        {
            "products": products,
            "result_count": len(products),
        },
    )


def product_detail(request, product_id):
    product = get_product(product_id)
    if not product:
        return redirect("shop")
    related = [
        p
        for p in PRODUCTS
        if p["category"] == product["category"] and p["id"] != product["id"]
    ][:4]
    return render(
        request,
        "store/product.html",
        {
            "product": product,
            "related": related,
        },
    )


def about(request):
    return render(request, "store/about.html")


def contact(request):
    if request.method == "POST":
        messages.success(
            request,
            "Thanks — your message is in. We’ll reply within one business day.",
        )
        return redirect("contact")
    return render(request, "store/contact.html")


def cart(request):
    return render(request, "store/cart.html")
