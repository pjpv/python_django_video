from django.shortcuts import render
from django.views import View
from category.models import categoryModel
from subject.models import subjectModel


# Create your views here.

class IndexView(View):
    def get(self, request):
        categorys = categoryModel.objects.all()
        c_list = []
        for c in categorys:
            s = subjectModel.objects.filter(category=c)[:6]
            c_list.append({
                'name': c.name,
                'subjects': s
            })
        content = {
            'categorys': c_list
        }

        return render(request, 'front/index.html', context=content)
