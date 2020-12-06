"""view for the Todo app"""
from django.shortcuts import render, render, redirect, get_object_or_404
from django.http import Http404

from .models import Todo
from .forms import TodoForm

def index(request):
    """Home page"""
    tasks = Todo.objects.all()

    """adding a New Task"""
    if request.method != 'POST':
        #No data submitted
        form = TodoForm()
    else:
        #data in the form, process data
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request,'todo_list/index.html', context)

def task_edit(request, pk):
    """Editing a task"""
    task = get_object_or_404(Todo, id=pk)
    if request.method != 'POST':
        form = TodoForm(instance=task)
    else:
        #changing the Task
        form = TodoForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:todo_list')
    context = {'task': task, 'form': form}
    return render(request, 'todo_list/task_edit.html', context)

def task_delete(request, pk):
    """Deleting a task"""
    task = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('todo_list:todo_list')

    context = {'task': task}
    return render(request, 'todo_list/task_delete.html', context)
