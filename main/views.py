from django.shortcuts import render, redirect
from django.contrib.auth import login
from main.models import Main, Hero, Blog
from django.views.generic import TemplateView, ListView, DetailView
from main.forms import RegisterForm


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main"] = Main.objects.latest('id')
        context["heroes"] = Hero.objects.order_by('-id')[:3]
        context["recentlies"] = Hero.objects.order_by('-id')[:6]
        context["trends"] = Hero.objects.all()
        context["populars"] = Hero.objects.order_by('-views')[:3]
        context["anime_details"] = Hero.objects.order_by('id')


        return context

class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-published_at']


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

class AnimeDetailView(DetailView):
    model = Hero
    template_name = 'anime-details.html'
    context_object_name = 'anime'


# class ProductDetailView(DetailView):
    # model = Product
    # template_name = "product-details.html"
    # context_object_name = 'product'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = self.get_object()
    #     return context
    #
    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return get_object_or_404(Product, id=id)
    #
