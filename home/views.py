from django.shortcuts import render
from .models import *
# Create your views here.
# from django.views import View
from django.views.generic import View
class Base(View):
    views = {}

class HomeView(Base):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['reviews'] = CustomerReview.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels='new')
        return render(request,'index.html',self.views)

class CategoryView(Base):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')

        return render(request,'category.html',self.views)


class BrandView(Base):
    def get(self,request,slug):
        brand_id = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = brand_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')

        return render(request,'brand.html',self.views)

class ProductDetail(Base):
    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug=slug)
        return render(request, 'product-detail.html',self.views)