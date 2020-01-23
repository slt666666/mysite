from django.shortcuts import render
from django.template import Context


def index(request):
    specie_list = Context({"specie_name": ["Tomato_v3_2", "Tomato_v2_4"]})
    return render(request, 'clusters/index.html', specie_list)

# def detail(request, specie_name):
#     return render(request, 'clusters/{}_cluster.html'.format(specie_name))
