from django.shortcuts import render,HttpResponseRedirect
from . models import Notes
# Create your views here.
from .forms import NotesForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name="notes"
    login_url= "/login"
    paginate_by = 10 

    def get_queryset(self):
        return self.request.user.notes.all().order_by('-created')

   
class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name="note"
    login_url="/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    success_url ='/smart/notes'
    form_class = NotesForm
    login_url="/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class=NotesForm
    login_url="/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name='notes/notes_delete.html'
    login_url="/login"

    def get_queryset(self):
        return self.request.user.notes.all()