from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')

    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoapp/index.html', context)


def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')


def updateTodo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            todo.text = text
            todo.save()
            return redirect('/')
    
    context = {
        'todo': todo
    }
    return render(request, 'todoapp/update_todo.html', context)



def about(request):
    return render(request, 'todoapp/about.html')

