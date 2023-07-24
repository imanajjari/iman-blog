from django.shortcuts import render
from django.views import View


# Create your views here.

class index_view(View):
    def get(self, request):
        return render(request, 'website/index.html')


def contect_view(request):
   return render(request, 'website/contact.html')
