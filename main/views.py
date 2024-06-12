from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import re


MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|android)", re.IGNORECASE)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

class HtmlView(TemplateView):
    title = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context[self.template_name.split(".")[0]] = True
        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            context['mobile'] = True
            if "iphone" in request.META['HTTP_USER_AGENT'].lower():
                context['apple'] = True
            else:
                context['android'] = True
        else:
            context['mobile'] = False
        context['agent'] = request.META['HTTP_USER_AGENT']
        if 'form' in context:
            context['form_media'] = context['form'].media
        return self.render_to_response(context)

