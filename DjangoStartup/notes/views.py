from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from . forms import NotesForm
from . models import Notes


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'


class NotesUpdataView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


# function based view

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
