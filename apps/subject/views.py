from django.shortcuts import render, reverse
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel
from line.models import lineModel


# Create your views here.

class subjectView(View):
    def get(self, request, cid, id):
        subject = get_object_or_404(subjectModel, id=id)
        lines = lineModel.objects.filter(subject=subject)
        l_list = []
        for line in lines:
            l_list.append({
                'name': line.name,
                'videos': videoModel.objects.filter(line=line)
            })

        breadcrumbs = []
        breadcrumbs.append(
            {'title': subject.category.name, 'url': reverse('category', kwargs={'id': subject.category_id})})
        breadcrumbs.append({'title': subject.name})

        return render(request, 'subject/subject.html',
                      context={'subject': subject, 'lines': l_list, 'breadcrumbs': breadcrumbs})
