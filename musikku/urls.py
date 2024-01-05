from django.urls import path
from .views import musik_list, musik_recommender

urlpatterns = [
    path('', musik_list, name='musik_list'),
    path('list/', musik_list, name='musik_list'),
    path('list/musik_recommender/', musik_recommender, name='musik_recommender'),
]
