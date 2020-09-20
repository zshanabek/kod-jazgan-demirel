from django.views.generic import DetailView, ListView

from .models import Set


class SetListView(ListView):
    model = Set
    template_name = 'sets/index.html'


class SetDetailView(DetailView):
    model = Set
    template_name = 'sets/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SetDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        set = kwargs['object']
        context['posts'] = set.posts.all()
        return context
