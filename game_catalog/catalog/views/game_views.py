from django.views import generic
from django.db.models import Q

from ..models.game import Game


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'game_list'
    model = Game

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(game_name__icontains=q) |
                Q(game_company__icontains=q) |
                Q(game_description__icontains=q)|
                Q(game_release_date__icontains=q)
            )
        return queryset


class GameCreateView(generic.CreateView):
    model = Game
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/index'
    fields = [
        'game_name',
        'game_company',
        'game_description',
        'game_release_date',
        'category_id',
        'esrb_id',
        'genres',
        'platforms',
    ]


class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'catalog/game/game-detail.html'


class GameUpdateView(generic.UpdateView):
    model = Game
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/index'
    fields = [
        'game_name',
        'game_company',
        'game_description',
        'game_release_date',
        'category_id',
        'esrb_id',
        'genres',
        'platforms',
    ]


class GameDeleteView(generic.DeleteView):
    model = Game
    template_name = 'catalog/delete-form.html'
    success_url = '../../catalog/index'
