from .models import PostCategory


class BlogMixin:
    def all_blog_context(self, **kwargs):
        context = self.add_category_to_context(**kwargs)
        return context

    def add_category_to_context(self, **kwargs):
        if kwargs is None:
            kwargs = {}
        kwargs["category"] = PostCategory.objects.all()
        kwargs["cat_select_id"] = self.kwargs.get("cat", 0)

        return kwargs
