from django.urls import path, include
from .views import *

extra_patterns = [
    path('inn/<int:pk>/', ConstructorView.as_view(), name='inn'),
]

urlpatterns = [
    path('', index, name='home'),
    path('constructor/', Add_date.as_view(), name='add_date'),
    path('constructor/', include(extra_patterns))
]