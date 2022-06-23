from django.views.generic import TemplateView
from django.shortcuts import render
from vega_datasets import data
import altair as alt

# Create your views here.

def main(request): #메인 화면
    return render(
    request, 
    'home.html', 
    {})

class IndexView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        source = data.cars()

        context['chart'] = alt.Chart(source).mark_circle().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin'
        ).interactive()
        return render(request, self.template_name, context)    