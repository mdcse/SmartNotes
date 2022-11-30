from django.shortcuts import render
from django.http import Http404 #for page not found
from django.views.generic import CreateView, ListView, DetailView


# Create your views here.
from .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

# class NotesCreateView(CreateView):
#     model = Notes
#     fields = ['title', 'content']
#     success_url = '/smart/notes'


class NotesListViews(ListView):
    model = Notes
    # template_name = 'notes_list.html'
    context_object_name = 'notes'

# def list(request):
#     mynotes = Note.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': mynotes})

class NotesDetailViews(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

# def detail(request, note_id):
#     try:
#         mynote = Notes.objects.get(id=note_id)
#     except Notes.DoesNotExist:
#         raise Http404("Note Not Found")
#     return render(request, 'notes/detail_note.html', {'note': mynote})