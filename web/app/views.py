from django.views import View
from django.shortcuts import render

class CaratView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/carat.html', { 'title': 'Main page', 'page_title': 'CARAT' })


class FreeVygemView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/free-vygem.html', { 'title': 'Vygem', 'page_title': '' })


class CutView(View):
    @staticmethod
    def get(request):
        return render(request, 'pages/cut.html', { 'title': 'CUT', 'page_title': 'CUT' })
