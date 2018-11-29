from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.core.paginator import Paginator

from category.models import categoryModel
from subject.models import subjectModel


# Create your views here.
class categoryView(View):
    def get(self, request, id):
        category = get_object_or_404(categoryModel, id=id)
        subjects = subjectModel.objects.filter(category=category).order_by('-pub_date', '-update_time')
        page = request.GET.get('p', 1)

        p = Paginator(subjects, per_page=18)#, per_page=page - 1
        subjects = p.page(page)

        breadcrumbs = []
        breadcrumbs.append({'title': category.name})
        breadcrumbs.append({'title': '第%d页' % subjects.number})

        return render(request, 'category/category.html',
                      context={'subjects': subjects, 'category': category, 'breadcrumbs':breadcrumbs})
