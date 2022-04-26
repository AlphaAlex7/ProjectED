class DataMixin:
    menu = [
        {'title': "Главная", 'url_name': '/posts/'},
        {'title': "Блог", 'url_name': '/posts/'},
        {'title': "Х", 'url_name': ''}
    ]

    def get_menu_context(self, **kwargs):
        context = kwargs
        if context is None:
            context = {}
        context['menu'] = self.menu
        # context["category"] = PostCategory.objects.all()
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
