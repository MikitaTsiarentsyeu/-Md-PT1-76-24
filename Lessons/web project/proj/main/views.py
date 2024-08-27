from django.shortcuts import render
import datetime

# Create your views here.
def test(request):
    c_time = datetime.datetime.now().time()
    return render(request, 'test.html', {'c_time':c_time})