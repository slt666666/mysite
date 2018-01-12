from django.shortcuts import render, get_object_or_404
from .models import Imochi1
import numpy as np


def index(request):
    gene_list = Imochi1.objects.order_by('id')[:100]
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
    all_gene = all_gene.values_list('rddw_16h', 'rddw_24h', 'rddw_48h', 'rddw_72h')
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
        return render(request, 'rice4869/network.html', {'first': first_gene, 'second': second_gene, 'all': all_gene})
