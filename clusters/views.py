from django.shortcuts import render
from django.template import Context


def index(request):
    specie_list = ["Tomato_v3_2", "Tomato_v2_4"]
    context = {
        'specie_list': specie_list,
    }
    return render(request, 'clusters/index.html', context)

# def detail(request, specie_name):
#     return render(request, 'clusters/{}_cluster.html'.format(specie_name))
