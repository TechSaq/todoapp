from django.shortcuts import render, redirect
from datetime import date
from .todoform import TodoForm

from .models import ToDo


def home(request):

    if request.method == 'POST':
        if request.POST.get('add') == 'add-task':
            print(request.POST)
            form = TodoForm(request.POST or None)
            if form.is_valid():
                description = form.cleaned_data['description']
                category = form.cleaned_data['category']
                due_date = form.cleaned_data['due_date']
                ToDo.objects.create(description=description,
                                    category=category,
                                    created_at=date.today(),
                                    due_date=due_date)

            return redirect('/')        

        if request.POST.get('delete') == 'delete-tasks':
            delete_ids = request.POST.getlist('todo')        
            print(delete_ids)
            ToDo.objects.filter(id__in=delete_ids).delete()
            return redirect('/')

    todos = ToDo.objects.all()

    todoData = {
        'todos': todos
    }

    todoData['todoform'] = TodoForm()
    return render(request, 'home.html', todoData)
