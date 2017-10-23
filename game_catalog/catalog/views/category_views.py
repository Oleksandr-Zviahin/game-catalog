from django.views import generic
from django.db.models import Q

from ..models.category import Category


class CategoryListView(generic.ListView):
    template_name = 'catalog/category/category-list.html'
    context_object_name = 'category_list'
    model = Category

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(Q(category_name__icontains=q)|
                                   Q(category_description__icontains=q))
        return queryset


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/category-list'
    fields = ['category_name', 'category_description']


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'catalog/category/category-detail.html'


class CategoryUpdateView(generic.UpdateView):
    model = Category
    template_name = 'catalog/add-form.html'
    success_url = '../../catalog/category-list'
    fields = ['category_name', 'category_description']


class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = 'catalog/delete-form.html'
    success_url = '../../catalog/category-list'
