from django.views.generic import ListView
from django.shortcuts import render
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'  # Este é o template principal.
    context_object_name = 'people'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '')
        birth_date = self.request.GET.get('birth_date', '')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if birth_date:
            queryset = queryset.filter(birth_date=birth_date)
        return queryset

    # def get_template_names(self):
    #     print(self.request.headers)  # Isso vai imprimir todos os cabeçalhos recebidos.
    #     if 'hx-request' in self.request.headers or 'x-hx-request' in self.request.headers:
    #         print("Request via HTMX detected.")
    #         return ['_person_list_body.html']
    #     return [self.template_name]
    def get_template_names(self):
        if self.request.GET.get('htmx'):
            print("htmx")
            return ['_person_list_body.html']
        return [self.template_name]

