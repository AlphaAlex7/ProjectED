from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import PostModel, PostCategory, PostComment
from .forms import AddPostForm
from .utils import DataMixin


class PostOneView(DetailView, DataMixin):
    model = PostModel
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context_mixin = self.get_user_context(title="Статьи")
        context = dict(list(context.items()) + list(context_mixin.items()))

        paginator = Paginator(PostComment.objects.filter(post=self.kwargs['pk']), 2)
        if "page" in self.request.GET:
            page_num = self.request.GET.get("page")
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context["page_obj"] = page
        context["comments"] = page.object_list

        return context


class PostAllView(ListView, DataMixin):
    model = PostModel
    paginate_by = 5
    paginate_orphans = 3
    template_name = 'blog/post_all_view.html'
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context_mixin = self.get_user_context(title="Статьи")
        context = dict(list(context.items()) + list(context_mixin.items()))

        print(context["posts"][0].get_comment_counts())
        return context


class AddPost(LoginRequiredMixin, CreateView, DataMixin):
    template_name = "blog/post_add.html"
    form_class = AddPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context_mixin = self.get_user_context(title="Новая статья")
        context = dict(list(context.items()) + list(context_mixin.items()))

        print(context)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
