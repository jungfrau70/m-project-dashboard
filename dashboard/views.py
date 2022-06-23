from django.views.generic import TemplateView
from django.shortcuts import render
from vega_datasets import data
import altair as alt

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        source = data.cars()

        context['chart'] = alt.Chart(source).mark_circle().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin'
        ).interactive()
        return render(request, self.template_name, context)    