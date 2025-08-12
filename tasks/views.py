from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


def board(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tasks:board')

    tasks = Task.objects.all()
    context = {
        'form': form,
        'tmt_tasks': tasks.filter(is_two_mins=True, is_completed=False),
        'do_tasks': tasks.filter(category=Task.DO, is_two_mins=False),
        'plan_tasks': tasks.filter(category=Task.PLAN, is_two_mins=False),
        'delegate_tasks': tasks.filter(category=Task.DELEGATE, is_two_mins=False),
        'forget_tasks': tasks.filter(category=Task.FORGET, is_two_mins=False),
    }
    return render(request, 'tasks/board.html', context)


def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/all_tasks.html', {'tasks': tasks})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tasks:board')
    return render(request, 'tasks/edit_task.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:board')
    return render(request, 'tasks/delete_task.html', {'task': task})


def update_category(request, pk):
    task = get_object_or_404(Task, pk=pk)
    category = request.POST.get('category')
    if category in dict(Task.CATEGORY_CHOICES):
        task.category = category
        task.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
