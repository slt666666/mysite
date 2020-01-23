from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'specie_list': ["Tomato_v3_2", "Tomato_v2_4"],
    }
    return render(request, 'clusters/index.html', context)

def cluster(request, specie):
    return render(request, 'clusters/index.html')
