from django.shortcuts import render


def index(request):
    specie_list = {"specie_name": "Tomato_v3_2", "specie_name": "Tomato_v2_4"}
    return render(request, 'clusters/index.html', {})

# def detail(request, specie_name):
#     return render(request, 'clusters/{}_cluster.html'.format(specie_name))
