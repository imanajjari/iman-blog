from django.shortcuts import render
from django.views import View
from .forms import contactForm
from django.contrib import messages
from .models import OurInformation

# Create your views here.

class index_view(View):
    def get(self, request):
        return render(request, 'website/index.html')


class contect_view(View):

    def get(self, request):
        form = contactForm()
        ourInformation = OurInformation.objects.last()
        content = {'form': form, 'ourInformation': ourInformation}
        return render(request, 'website/contact.html', content)

    def post(self, request):
        if request.method == 'POST':
            form = contactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'your ticket submited successfuly')
            else:
                messages.add_message(request, messages.ERROR, 'your ticket didnt submited ')
            form = contactForm()
            ourInformation = OurInformation.objects.last()
            content = {'form':form,'ourInformation':ourInformation }
            return render(request, 'website/contact.html', content)

