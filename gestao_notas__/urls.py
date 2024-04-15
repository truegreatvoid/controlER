from django.urls import path
from .views import PersonListView

app_name = 'gestao_notas'

urlpatterns = [
    path('', PersonListView.as_view(), name='person_list'),
    # Adicione mais padrões de URL aqui
]
