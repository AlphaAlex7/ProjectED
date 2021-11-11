from .models import PostCategory


class BlogMixin:
    def all_blog_context(self, **kwargs):
        context = self.add_category_to_context(**kwargs)
        return context

    def add_category_to_context(self, **kwargs):
        context = kwargs
        print(context)
        if context is None:
            context = {}
        context["category"] = PostCategory.objects.all()
        if self.request.resolver_match.kwargs.get("cat"):
            context["cat_select_id"] = self.request.resolver_match.kwargs.get("cat")
        else:
            context["cat_select_id"] = 0
        return context
