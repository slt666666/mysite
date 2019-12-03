from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from .models import Imochi1
import numpy as np


def index(request):
    gene_list = Imochi1.objects.order_by('id')[:10]
    context = {
        'gene_list': gene_list,
    }
    return render(request, 'rice4869/index.html', context)


def detail(request, gene_id):
    gene_data = get_object_or_404(Imochi1, gene_id=gene_id)
    gene_list = Imochi1.objects.order_by('id')[:100]
    return render(request, 'rice4869/detail.html', {'gene_data': gene_data, 'gene_list': gene_list})


def network(request, gene_id):
    first_gene = get_object_or_404(Imochi1, gene_id=gene_id)
    all_gene = Imochi1.objects.order_by('id')
    all_gene_index = list(all_gene.values_list('gene_id'))
    all_gene = all_gene.values_list('rddw_16h', 'rddw_24h', 'rddw_48h', 'rddw_72h', 'rmo_16h', 'rmo_24h', 'rmo_48h', 'rmo_72h', 'sddw_12h', 'sddw_24h', 'sddw_36h', 'sddw_48h', 'sddw_72h', 'smo_12h', 'smo_24h', 'smo_36h', 'smo_48h', 'smo_72h')
    all_gene = np.array(all_gene)
    try:
        second_gene = get_object_or_404(Imochi1, gene_id=request.POST['second_gene'])
    except (KeyError, Imochi1.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'rice4869/detail.html', {
            'question': gene_id,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'rice4869/network.html', {'first': first_gene, 'second': second_gene, 'all': all_gene, 'index': all_gene_index})


def view_detail(req):
    if req.method == 'POST':
        gene = req.POST['select_gene']
        surprise_txt = gene + "!!!"

        response = {'your_surprise_txt': surprise_txt, }

        return JsonResponse(response)

    else:
        raise Http404
