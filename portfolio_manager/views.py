import mimetypes

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from django.views import View

from portfolio_manager.models import *



class PortfolioView(View):
    def get(self, request):
        try:
            cv = CV.objects.get(id=1)
        except:
            raise Http404("No MyModel matches the given query.")
        return render(request, 'portfolio/portfolio.html', {'file':cv})


class FileDownloadView(View):
    
    def get(self, request):
        cv_file = CV.objects.latest('created_date')
        file_path = cv_file.cv_file.path
        filename = cv_file.cv_file.name

        with open(file_path, 'rb') as fl:
            mime_type, _ = mimetypes.guess_type(file_path)
            response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
