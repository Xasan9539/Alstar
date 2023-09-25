from django.shortcuts import render
from .models import Alstar
# Create your views here.
def test(request):
    return render(request,'mainapp/test.html')


def index(request):
    alstars = Alstar.objects.all()

    context = {
        "alstars":alstars
    }
    return render(request,'mainapp/index.html',context)