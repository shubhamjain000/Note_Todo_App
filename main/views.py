from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Todo
from .forms import NoteForm, TodoForm

# Optional landing page
def home(request):
    return render(request, 'main/home.html')

# ------------------- Notes Views -------------------
def note_list(request):
    notes = Note.objects.all().order_by('-id')
    return render(request, 'main/note_list.html', {'notes': notes})

def add_note(request):
    form = NoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'main/note_form.html', {'form': form})

def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    form = NoteForm(request.POST or None, request.FILES or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'main/note_form.html', {'form': form})

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note_list')

# ------------------- Todos Views -------------------
def todo_list(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'main/todo_list.html', {'todos': todos})

def add_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'main/todo_form.html', {'form': form})

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'main/todo_form.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')

from django.shortcuts import redirect

def home(request):
    return redirect('note_list')  # redirect directly to Notes page

