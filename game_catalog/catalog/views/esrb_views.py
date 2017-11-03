from django.views import generic
from django.db.models import Q

from ..models.esrb import ESRB


class ESRBListView(generic.ListView):
    template_name = 'catalog/esrb/esrb-list.html'
    context_object_name = 'rate_list'
    model = ESRB

    def get_queryset(self):
        queryset = super(ESRBListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(rate_full_name__icontains=q) |
                Q(rate_short_name__icontains=q)|
                Q(rate_description__icontains=q)
            )
        return queryset


class ESRBCreateView(generic.CreateView):
    model = ESRB
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/esrb-list'
    fields = ['rate_full_name', 'rate_short_name', 'rate_description']


class ESRBDetailView(generic.DetailView):
    model = ESRB
    template_name = 'catalog/esrb/esrb-detail.html'


class ESRBUpdateView(generic.UpdateView):
    model = ESRB
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/esrb-list'
    fields = ['rate_full_name', 'rate_short_name', 'rate_description']


class ESRBDeleteView(generic.DeleteView):
    model = ESRB
    template_name = 'catalog/delete-form.html'
    success_url = '../../catalog/esrb-list'
