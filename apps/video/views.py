from django.shortcuts import render
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel


# Create your views here.
class playView(View):
    def get(self, request, id):
        video = get_object_or_404(videoModel, id=id)
        subject = video.line.subject
        return render(request, 'video/play.html', context={'video': video})
