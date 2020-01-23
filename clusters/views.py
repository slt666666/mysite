from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'specie_list': ["Brapa","Arabidopsis","Ashtree","Bentham_v0_4_4","Buckwheat","Cacao","Carrot","Cassava",
                        "Coffee","Cucumber","Eucalyptus","Grape","Kiwifruit","Lettuce","Malus","Medicago","Monkeyflower",
                        "Olive","Orange","Papaya","Pepper","Poplar","Prunus","Soybean_a4v1","Spinach",
                        "Sugarbeet","Sunflower","Sweetpotato","Tomato_v2_4","Tomato_v3_2"],
    }
    return render(request, 'clusters/index.html', context)

def cluster(request, specie):
    return render(request, 'clusters/{}_cluster.html'.format(specie))
