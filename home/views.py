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
        return render(request,'index.html',self.views)
