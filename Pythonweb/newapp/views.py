from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import data, steps
from .forms import creatation

# Create your views here.

def home(req):
    title = "ahihi"
    data_ = data.objects.all()
    context = {"title": title, "data": data_}
    return render(req, 'newapp/home.html', context)

def notify(req):
    return render(req, 'newapp/notify.html')

def login(req):
    return render(req, 'newapp/login.html')

def post(req, id):
    data_ = data.objects.get(id=id)
    steps_ = data_.steps_address
    media_url = settings.MEDIA_URL
    num = data.num_of_steps
    input = []
    step_arr = steps_.split()
    for i in range(len(step_arr)):
        s = steps.objects.get(id=int(step_arr[i]))
        input.append(s)

    context = {"data": data_, "steps": input, "media_url": media_url, "num": num}
    return render(req, 'newapp/post.html', context)

def create(req):
    form = creatation()

    if req.method == 'POST':
        form = creatation(req.POST)
        if form.is_valid():
            a = form.update_data()
            return render(req, 'newapp/show.html', {'data':a})
    return render(req, 'newapp/create.html', {'form': form})