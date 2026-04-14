from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView



# Create your views here.
# def home(request):
#     posts = Posts.objects.order_by('-date_posted')
#     return render(request, 'blog/home.html', {'posts': posts})
class PostLiveView(ListView):
    model = Posts
    #default view name <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=self.author).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


def calendar_404(request):
    return render(request, 'blog/404.html', status=404)


def custom_404(request, *args, **kwargs):
    return render(request, 'blog/404.html', status=404)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
