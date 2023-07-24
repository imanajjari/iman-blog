from django.shortcuts import render
from django.views import View


# Create your views here.

class index_view(View):
    template_name = ''
    def get(self, request):
        form = self.form_class
        return render(request, 'website/index.html' , {'form':form})
