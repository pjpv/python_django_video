from django.shortcuts import render
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel
from line.models import lineModel


# Create your views here.

class subjectView(View):
    def get(self, request, id):
        subject = get_object_or_404(subjectModel, id=id)
        lines = lineModel.objects.filter(subject=subject)
        l_list = []
        for line in lines:
            l_list.append({
                'name': line.name,
                'videos': videoModel.objects.filter(line=line)
            })
        return render(request, 'subject/subject.html', context={'subject': subject, 'lines': l_list})
