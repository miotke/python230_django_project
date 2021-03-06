from django import forms
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.template import loader
from blogging.models import Post
from blogging.forms import CommentForm


def stub_view(request, *args, **kwargs):
    body = 'Stub view\n\n'
    if args:
        body += 'Args:\n'
        body += '\n'.join(['\t%s' % a for a in args])
    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join(['\t%s' % i for i in kwargs])

    return HttpResponse(body, content_type='text/plain')


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts if request.user.is_authenticated else []}

    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}

    return render(request, 'blogging/detail.html', context)


def add_comment(request):

    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()

            return redirect('/')
    else:
        form = CommentForm()

        return render(request, 'blogging/list.html')
