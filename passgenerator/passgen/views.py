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

class test(View):
    def get(self, request):
        return render(request, 'passgen/test.html')
    def post(self, request):
        pass