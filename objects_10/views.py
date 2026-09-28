from django.shortcuts import render
from django.views.generic import TemplateView
from objects_10.utils import getPrediction
import urllib


def detector(request):
    if request.method == 'POST':
        url = request.POST.get('img_url')
        urllib.request.urlretrieve(url,'objects_10/images/img.png')

        result = getPrediction('objects_10/images/img.png')
        # print(result)
    else:
        print("something wrong")
    return render(request,'objects_10/detector.html',{"result":result})

