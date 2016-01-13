from django.db import models
from django.http import Http404
from django.template.loader import render_to_string
import math


class Paginator:
    def __init__(self, objects, count_per_page, current_page):
        self.objects = objects
        self.count_per_page = count_per_page
        self.current_page = self.validate_cp(current_page)

    def count(self):
        if isinstance(self.objects, models.QuerySet):
            return self.objects.count()
        return len(self.objects)

    def paginator(self):
        objects = self.objects[self.count_per_page * (
            self.current_page - 1):(self.count_per_page * self.current_page)]
        return objects

    def max_page(self):
        per_page = self.count_per_page * 1.0
        max_page = int(math.ceil((self.count() / per_page)))
        return max_page

    def validate_cp(self, page):
        try:
            page = int(page)
        except (TypeError, ValueError):
            raise Http404
        if not 1 <= page <= self.max_page():
            raise Http404
        return page

    def page_range(self):
        cp = self.current_page
        mp = self.max_page()
        pages = []
        if 4 <= cp <= mp - 3:
            if cp == 5:
                pages = range(cp - 3, cp + 3)
            elif cp == mp - 4:
                pages = range(cp - 2, cp + 4)
            else:
                pages = range(cp - 2, cp + 3)

            if cp > 5:
                pages = ['...'] + pages
            if cp <= mp - 5:
                pages += ['...']

        elif cp < 4:
            pages = range(2, cp + 3) + ['...']
        elif cp > self.max_page() - 3:
            pages = ['...'] + range(cp - 2, mp)

        pages = [1] + pages + [mp]
        return pages

    def __iter__(self):
        return iter(self.paginator())

    def render(self):
        return render_to_string('paginator/paginator.html', {'paginator': self})