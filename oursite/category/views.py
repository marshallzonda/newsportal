from mylib.helpers import get_user
from django.shortcuts import render, redirect
from django.utils import timezone
from.forms import AdForm
from.models import Ad


def forhome(request):
    data:dict = get_user(request)
    return render(request,'category/forhome.html',context=data)

def wear(request):
    data:dict = get_user(request)
    ads = Ad.objects.all()
    data['ads'] = ads
    return render(request,'category/wear.html',context=data)

def electronics(request):
    data:dict = get_user(request)
    return render(request,'category/electronics.html',context=data)

def turism(request):
    data:dict = get_user(request)
    return render(request,'category/turism.html',context=data)

def create(request):
    data = get_user(request)
    if request.method == 'GET':
        data['form'] = AdForm()
        return render(request,'category/create.html',context=data)
    elif request.method == 'POST':
        ad_form = AdForm(request.POST,request.FILES)
        #ad_form.Meta.model.publish = timezone.now()
        ad_form.save()
        return redirect('category/wear')
