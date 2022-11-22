from django.shortcuts import render, redirect
from .models import today_task
from .forms import todayform

# Create your views here.
def index(request):
    if request.method == 'POST':
        Take_name = request.POST.get('taskname')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = today_task(Take_name=Take_name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, "index.html")


def details(request):
    task = today_task.objects.all()
    return render(request, "details.html", {'task_results': task})


def update(request, id):
    taskvar = today_task.objects.get(id=id)
    formvar=todayform(request.POST or None, instance=taskvar)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html", {'formresult': formvar, 'taskresult': taskvar})
