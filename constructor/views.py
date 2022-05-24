from urllib import response
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
import requests
from .forms import AddDateForm
from . models import *

from pexels_api import API

def index(request):
    
    PEXELS_API_KEY = '563492ad6f917000010000013b93d4d2b2f0471b88e907d5edccb327'
    api = API(PEXELS_API_KEY)
    api.search('kitten', page=1, results_per_page=5)
    photos = api.get_entries()
    somelist = []
    for photo in photos:
        somelist.append(photo.medium)

    context = {
        'title': 'Главная страница',
        'somelist': somelist,
    }

    return render(request, 'constructor/index.html', context)


class Add_date(CreateView):
    form_class = AddDateForm
    template_name = 'constructor/add_date.html'

class ConstructorView(DetailView):
    model = Constructor
    template_name = 'constructor/inn.html'
    context_object_name = 'inn'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ConstructorView, self).get_context_data(**kwargs)
        # Object is accessible through self.object or self.get_object()
        constructor = self.get_object()
        #getting photos by API
        PEXELS_API_KEY = '563492ad6f917000010000013b93d4d2b2f0471b88e907d5edccb327'
        api = API(PEXELS_API_KEY)
        api.search(constructor.keywords, page=1, results_per_page=5)
        photos = api.get_entries()
        photo_url_list = []
        for photo in photos:
            photo_url_list.append(photo.medium)

        context['photo_list'] = photo_url_list
        return context




# def add_date(request):
#     if request.method=='POST':
#         form = AddDateForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:        
#         form = AddDateForm()
#     context = {
#         'form': form,
#         'title': 'Добавление информации',
#     }
#     return render(request, 'constructor/add_date.html', context)
