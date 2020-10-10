from django.shortcuts import render, redirect, reverse
from .models import Product
from django.conf import settings
import requests
import json
from .forms import ProductForm
import os
from django.core.files.base import ContentFile


def all_products(request):
    response = requests.get(
        settings.BASE_URL + settings.COUNTRY_DATA_WORLDMETERS)

    if response.status_code == 200:
        all_data = json.loads(response.content.decode("utf-8"))
        country_data = []
        for country in all_data:
            try:
                country_name = country["country"]
                country_code = country["countryInfo"]["iso2"]
                country_cases = country["cases"]
                country_todayCases = country["todayCases"]
                country_deaths = country["deaths"]
                country_recovered = country["recovered"]
                casesPerOneMillion = country["casesPerOneMillion"]
                deathsPerOneMillion = country["deathsPerOneMillion"]
                country_population = country["population"]
                country_data_set = {
                    "country": country_name,
                    "code": country_code,
                    "cases": country_cases,
                    "todayCases": country_todayCases,
                    "deaths": country_deaths,
                    "recovered": country_recovered,
                    "population": country_population,
                    "casesPerOneMillion": casesPerOneMillion,
                    "deathsPerOneMillion": deathsPerOneMillion,
                }
                country_data.append(country_data_set)

            except Exception as e:
                print("Exception:", e)

    products = Product.objects.all().order_by("-number_in_stock")
    context = {
        "products": products,
        "country_data": country_data
    }
    return render(request, "products/all_products.html", context)


def create_product(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(reverse("products"))

    context = {
        "form": form,
    }

    return render(request, "products/products_form.html", context)



def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse("products"))
    else:
        form = ProductForm(request.POST or None, instance=product)

    
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/products_form.html", context)


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        print(product)
        product.delete()
        return redirect(reverse("products"))