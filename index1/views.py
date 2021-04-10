from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class index1(TemplateView):
    template_name = 'index1.html'
    template_engine = None
    content_type = None
    extra_context = {'title': 'this is a Get'}

    # 重新定义模板获取上下文
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'i am django'
        return context

    # 定义http的POST请求处理方法
    def post(self, request, *args, **kwargs):
        self.extra_context = {'title': 'this is a POST'}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)