from django.shortcuts import render
from django.views.generic.base import RedirectView

# Create your views here.
def index(req):
    return render(req, 'index.html')

class turnTo(RedirectView):
    # 设置属性
    permanent = False
    url = None
    pattern_name = 'index:index'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print('this is get_red_url')
        return super().get_redirect_url(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        print(request.META.get('HTTP_USER_AGENT'))
        return super().get(request, *args, **kwargs)