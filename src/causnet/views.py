from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import SWM, SWMFragment


class IndexView(generic.ListView):
    template_name = 'causnet/index.html'
    context_object_name = 'all_swms'

    def get_queryset(self):
        return SWM.objects.order_by('-creation_date')


class DetailView(generic.DetailView):
    model = SWM
    template_name = 'causnet/detail.html'


class FragmentView(generic.DetailView):
    model = SWMFragment
    template_name = 'causnet/fragment.html'
