from django.shortcuts import render , redirect
from shortner.models import Url
# Create your views here.

def index(req):
    if req.method == 'POST':
        full_url = req.POST.get('full_url')
        obj = Url.create(full_url)
        return render(req,'shortner/index.html',{
            'full_url' :obj.full_url,
            'short_url' : req.get_host() + '/' + obj.short_url
        })
    return render(req,'shortner/index.html')


def routetoUrl(req,key):
    try:
        obj=Url.objects.get(short_url= key)
        return redirect(obj.full_url)
    except:
        return redirect(index)    
    