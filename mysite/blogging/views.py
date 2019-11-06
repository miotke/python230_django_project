from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404


def stub_view(request, *args, **kwargs):
    body = 'Stub view\n\n'
    if args:
        body += 'Args:\n'
        body += '\n'.join(['\t%s' % a for a in args])
    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join(['\t%s' % i for i in kwargs])

    return HttpResponse(body, content_type='text/plain')
