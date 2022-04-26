from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ProjectED.utils import DataMixin
from .forms import AddPostForm, AddCommentForm
from .models import PostModel, PostComment
from .utils import BlogMixin


class AddComment(CreateView):
    form_class = AddCommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.author = self.request.user
        form.instance.post = PostModel.objects.get(pk=kwargs['post_id'])
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        if PostModel.objects.get(pk=kwargs['post_id']):
            return redirect("blog:detail", pk=kwargs['post_id'])
        else:
            return redirect("blog:all_posts")


class PostOneView(DetailView, DataMixin, BlogMixin):
    model = PostModel
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    comment_paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Статьи")
        context = super().all_blog_context(**context)

        paginator = Paginator(
            object_list=PostComment.objects.filter(post=self.kwargs['pk']),
            per_page=self.comment_paginate_by
        )

        page = paginator.get_page(self.request.GET.get("page", 1))

        context["page_obj"] = page
        context["comments"] = page.object_list
        context["paginator"] = page.paginator
        context["is_paginated"] = (self.comment_paginate_by < page.paginator.count)
        context["form_comment"] = AddCommentForm()

        return context


class PostAllView(ListView, DataMixin, BlogMixin):
    model = PostModel
    paginate_by = 5
    paginate_orphans = 3
    template_name = 'blog/post_all_view.html'
    context_object_name = "posts"

    def get_queryset(self):
        print(self.kwargs)
        if self.kwargs.get("cat"):
            query_set = self.model.objects.filter(category=self.kwargs["cat"])
        else:
            query_set = self.model.objects.all()
        query_set = query_set.select_related("author").select_related("category").prefetch_related("post_id")
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Статьи")
        context = super().all_blog_context(**context)
        return context


class AddPost(LoginRequiredMixin, CreateView, DataMixin, BlogMixin):
    template_name = "blog/post_add.html"
    form_class = AddPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Новая статья")
        context = super().all_blog_context(**context)
        context["user"] = self.request.user
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.img = self.request.FILES
        return super().form_valid(form)


class DelPost(DeleteView):
    model = PostModel
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = "post"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponseBadRequest()


class UpdatePost(UpdateView, DataMixin, BlogMixin):
    model = PostModel
    template_name = "blog/post_add.html"
    form_class = AddPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_menu_context(**context, title="Редактировать статью")
        context = super().all_blog_context(**context)
        context["user"] = self.request.user
        context["edit"] = True
        return context
