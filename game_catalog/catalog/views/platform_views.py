from django.views import generic
from django.db.models import Q

from ..models.platform import Platform


class PlatformListView(generic.ListView):
    template_name = 'catalog/platform/platform-list.html'
    context_object_name = 'platform_list'
    model = Platform

    def get_queryset(self):
        queryset = super(PlatformListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(platform_name__icontains=q) |
                Q(platform_version__icontains=q) |
                Q(platform_description__icontains=q)
            )
        return queryset


class PlatformCreateView(generic.CreateView):
    model = Platform
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/platform-list'
    fields = ['platform_name', 'platform_version', 'platform_description']


class PlatformDetailView(generic.DetailView):
    model = Platform
    template_name = 'catalog/platform/platform-detail.html'


class PlatformUpdateView(generic.UpdateView):
    model = Platform
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/platform-list'
    fields = ['platform_name', 'platform_version', 'platform_description']


class PlatformDeleteView(generic.DeleteView):
    model = Platform
    template_name = 'catalog/delete-form.html'
    success_url = '../../catalog/platform-list'
