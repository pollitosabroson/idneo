# -*- coding: utf-8 -*-
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from books.models import Book


def home(request):
    return render_to_response(
        'home.html', context_instance=RequestContext(request))


def search(request):
    category = request.GET.get('category', None)
    format = request.GET.get('type', None)
    filters = {}
    if category:
        filters.update(category__name__icontains="{0}".format(category))

    if format:
        filters.update(format__name__icontains="{0}".format(format))
    queryset = Book.objects.filter(**filters)
    books = []
    for book in queryset:
        parse = {
            "id": book.public_id,
            "title": book.title,
            "description": book.description,
            "thumbnail": book.thumbnail_url,
            "price": book.price
        }
        books.append(parse)
    data = json.dumps(books, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def book(request, pk=None):
    context = RequestContext(request)
    book = get_object_or_404(Book, public_id=pk)
    return render_to_response(
        'single.html', {'book': book}, context_instance=context)
