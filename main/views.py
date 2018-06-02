from django.urls import reverse_lazy
from django.views.generic import TemplateView
from random import randint


if '_' not in locals():
    def _(s): return s


from . import _View, cached


class BaseView(_View, TemplateView):

    def get_template_names(self):
        return ["main/base.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        app_name = 'ProApp1'
        data.app_name = app_name
        title = 'Главная'
        data.title = title
        subscribe_email = 'you@yourwebsite.com'
        data.subscribe_email = subscribe_email

        data.menu_main = {
            'index': {'label': _('Главная'), 'link': reverse_lazy('main.index')},
            'service': {'label': _('Услуги'), 'link': reverse_lazy('main.service')},
            'personal': {'label': _('Частный клиент'), 'link': reverse_lazy('main.personal')},
            'business': {'label': _('Бизнес клиент'), 'link': reverse_lazy('main.business')},
        }

        return data + {'url': url, 'app_name': app_name, 'title': title, 'subscribe_email': subscribe_email}


class IndexView(BaseView):

    def activate_main_menu(self, *args, **kwargs):
        self.get_data().menu_main['index']['active'] = True

    def get_template_names(self):
        return ["main/index.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        self.activate_main_menu()

        return data + {'url': url}


class ServiceView(BaseView):

    def activate_main_menu(self, *args, **kwargs):
        self.get_data().menu_main['service']['active'] = True

    def get_template_names(self):
        return ["service.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        title = 'Услуги'
        data.title = title

        self.activate_main_menu()

        return data + {'url': url, 'title': title}


class PersonalView(BaseView):

    def activate_main_menu(self, *args, **kwargs):
        self.get_data().menu_main['personal']['active'] = True

    def get_template_names(self):
        return ["personal.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        title = 'Частный клиент'
        data.title = title

        self.activate_main_menu()

        return data + {'url': url, 'title': title}


class BusinessView(BaseView):

    def activate_main_menu(self, *args, **kwargs):
        self.get_data().menu_main['business']['active'] = True

    def get_template_names(self):
        return ["business.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        title = 'Бизнес клиент'
        data.title = title

        self.activate_main_menu()

        return data + {'url': url, 'title': title}


class TestView(BaseView):

    def get_template_names(self):
        return ["test.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        title = 'Тестирование онлайн'
        data.title = title
        procrastination_level_personal = randint(10, 100)
        data.procrastination_level_personal = procrastination_level_personal
        procrastination_level_business = randint(50, 110)
        data.procrastination_level_business = procrastination_level_business
        return_url = format(url.param1)
        data.return_url = return_url
        procrastination_result_1 = 'Недостаточный уровень прокрастинации!'
        data.procrastination_result_1 = procrastination_result_1
        procrastination_result_2 = 'Средний уровень прокрастинации!'
        data.procrastination_result_2 = procrastination_result_2
        procrastination_result_3 = 'Очень хороший уровень прокрастинации!'
        data.procrastination_result_3 = procrastination_result_3
        procrastination_result_4 = 'Великолепный уровень прокрастинации!'
        data.procrastination_result_4 = procrastination_result_4
        procrastination_result_5 = 'Вы гений прокрастинации!'
        data.procrastination_result_5 = procrastination_result_5

        return data + {'url': url, 'title': title, 'procrastination_level_personal': procrastination_level_personal, 'procrastination_level_business': procrastination_level_business, 'return_url': return_url, 'procrastination_result_1': procrastination_result_1, 'procrastination_result_2': procrastination_result_2, 'procrastination_result_3': procrastination_result_3, 'procrastination_result_4': procrastination_result_4, 'procrastination_result_5': procrastination_result_5}


class Page404View(BaseView):

    def get_template_names(self):
        return ["main/page404.html"]

    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        url = type('url', (object,), self.kwargs)

        title = 'Страница не найдена!'
        data.title = title

        return data + {'url': url, 'title': title}


from django.conf import urls

from django.conf.urls import handler404
handler_404_view = Page404View.as_view()
setattr(urls, 'handler404', 'main.views.handler_404_view')
