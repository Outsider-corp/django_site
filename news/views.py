from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .models import News, Categories
from .forms import *
from first_site.settings import EMAIL_HOST_USER


class ClassNew(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Daily News"
        return context

    def get_queryset(self):
        return News.objects.filter(is_publ=True).select_related('category')


class ClassCategory(ListView):
    model = Categories
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daily News'
        context['cat1'] = Categories.objects.get(pk=self.kwargs['cat_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'], is_publ=True).select_related('category')


class ClassView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/view_post.html'
    pk_url_kwarg = 'news_id'


class ClassCreate(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_post.html'
    login_url = '/admin/'


def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful Registration")
            return redirect('index')
        else:
            messages.error(request, "Registration Error")
    else:
        form = RegForm()
    return render(request, 'news/registration.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = LogForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back')
            return redirect('index')
    else:
        form = LogForm()
    return render(request, 'news/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')


def mail_send(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            email = send_mail(form.cleaned_data['subject'], form.cleaned_data['mes_email'], EMAIL_HOST_USER,
                              [request.user.email], fail_silently=False)
            if email:
                messages.success(request, "Email was sent")
                return redirect('mail')
            else:
                messages.error(request, "Sending Error")
    else:
        form = MailForm()
    return render(request, 'news/mail.html', {'form': form})
# def index(request):
#     news = News.objects.all()
#     p = Paginator(news, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = p.get_page(page_num)
#     return render(request, 'news/index.html', {"new": news, "title": "Daily News", 'page_obj': page_objects})

# def categories(request, cat_id):
#     news = News.objects.filter(category_id=cat_id)
#     cat = Categories.objects.get(pk=cat_id)
#     return render(request, 'news/category.html',
#                   {"new": news, "cat1": cat, "title": "Daily News"})


# def view_post(request, news_id):
#     # news = News.objects.get(pk=news_id)
#     news = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_post.html', {"news": news, "title": news.title})


# def add_post(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, "news/add_post.html", {"form": form})
