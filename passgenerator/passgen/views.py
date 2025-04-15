from django.shortcuts import render
from django.views import View

from .forms import PassGenForm


class Index(View):
    def get(self, request):
        form = PassGenForm()

        context = {'form': form}
        return render(request, 'passgen/index.html', context)
    def post(self, request):
        pass