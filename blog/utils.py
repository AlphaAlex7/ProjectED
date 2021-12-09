from .models import PostCategory


class BlogMixin:
    def all_blog_context(self, **kwargs):
        context = self.add_category_to_context(**kwargs)
        context = self.add_action_button(**context)
        return context

    def add_action_button(self, **kwargs):
        action_button = [
            {
                "title": "Мой аккаунт",
                "id": "my_page",
                "href": "",
                "hiden": True,
            },
            {
                "title": "Добавить статью",
                "id": "add_article",
                "href": "blog:add_post",
                "hiden": False,
            }
        ]
        kwargs["actions"] = action_button
        return kwargs

    def add_category_to_context(self, **kwargs):
        if kwargs is None:
            kwargs = {}
        kwargs["category"] = PostCategory.objects.all()
        if self.request.resolver_match.kwargs.get("cat"):
            kwargs["cat_select_id"] = self.request.resolver_match.kwargs.get("cat")
        else:
            kwargs["cat_select_id"] = 0
        return kwargs
