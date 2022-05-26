from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import AddDateForm
from . models import *
from pexels_api import API

""" Отображение заглавной страницы """
def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'constructor/index.html', context)


""" Отображение формы заполнения данных """
class Add_date(CreateView):
    form_class = AddDateForm
    template_name = 'constructor/add_date.html'

""" API функция для фото """
def pexels_api(constructor):
    PEXELS_API_KEY = '563492ad6f917000010000013b93d4d2b2f0471b88e907d5edccb327'
    api = API(PEXELS_API_KEY)
    api.search(constructor.keywords)
    photos = api.get_entries()
    photo_stream = []
        # заполнение списка ссылками на фото
    for photo in photos:
        if len(photo_stream) < 4:
            photo_stream.append(photo.original)
        else:
            photo_stream.append(photo.medium)
    return (photo_stream)


""" Отображение после заполнения формы  """
class ConstructorView(DetailView):
    model = Constructor
    template_name = 'constructor/inn.html'
    context_object_name = 'inn'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ConstructorView, self).get_context_data(**kwargs)
        constructor = self.get_object()
        context['photo_stream'] = pexels_api(constructor)[4:]
        context['photos_slider'] = pexels_api(constructor)[:4]
        context['city'] = constructor.city
        context['key'] = 'AIzaSyDCRttepmyi8qYqFtBkrzYC2cRzx62zew4'
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
