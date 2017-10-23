from django.views import generic
from django.db.models import Q

from ..models.genre import Genre


class GenreListView(generic.ListView):
    template_name = 'catalog/genre/genre-list.html'
    context_object_name = 'genre_list'
    model = Genre

    def get_queryset(self):
        queryset = super(GenreListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(genre_name__icontains=q) |
                Q(genre_description__icontains=q)
            )
        return queryset


class GenreCreateView(generic.CreateView):
    model = Genre
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/genre-list'
    fields = ['genre_name', 'genre_description']


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'catalog/genre/genre-detail.html'


class GenreUpdateView(generic.UpdateView):
    model = Genre
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/genre-list'
    fields = ['genre_name', 'genre_description']


class GenreDeleteView(generic.DeleteView):
    model = Genre
    template_name = 'catalog/delete-form.html'
    success_url = '../../catalog/genre-list'
