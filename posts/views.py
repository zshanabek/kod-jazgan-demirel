from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(
            set=context['post'].set).order_by('created')
        context['sidebar'] = posts
        return context


def search_post(request):
    if request.method == "POST":
        query_name = request.POST.get('title', None)
        if query_name:
            results = Post.objects.filter(title__contains=query_name)
            return render(request, 'posts/post-search.html', {"results": results})
    return render(request, 'posts/post-search.html')
