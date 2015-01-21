from django.shortcuts import render
from django.contrib.flatpages import views as ftviews
from django.contrib.flatpages.views import *
from django.conf import settings
from photologue.models import Gallery

import os

from core.models import Section, Page, MenuItem
# Create your views here.

def page(request, url):
    if not url.startswith('/'):
        url = '/' + url
    try:
        page = get_object_or_404(Page, url=url)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            page = get_object_or_404(Page, url=url)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise

    return render(request, 'base.html', {
        'page': page,
        'sections': MenuItem.objects.order_by('position'),
        'gallery': Gallery.objects.get(id=settings.PRODUCTS_GALLERY_ID) if 'products' in request.path else None
        }, content_type="text/html")

@csrf_protect
def render_flatpage_fix(request, f):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    c = RequestContext(request, {
        'page': f,
        'sections': Section.objects.order_by('position'),
        'gallery': Gallery.objects.get(id=settings.PRODUCTS_GALLERY_ID) if 'products' in request.path else None
    })

    response = HttpResponse(t.render(c))
    return response

ftviews.render_flatpage = render_flatpage_fix

def robots(request):
    return HttpResponse('User-agent: *\nDisallow: /staff', content_type="text/plain")

def google_verification(request):
    return HttpResponse('google-site-verification: google5a5a66ed4665c7ff.html', content_type="text/plain")

def yandex_verification(request):
    return HttpResponse('', mimetype="text/plain")