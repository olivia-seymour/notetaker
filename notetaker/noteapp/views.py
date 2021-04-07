from django.shortcuts import render
from .models import noteItem
from django.http import HttpResponseRedirect

# Create your views here.
def notesView(request):
    all_note_items = noteItem.objects.all()
    return render(request, 'notes.html', {'all_items': all_note_items})

def addNotesView(request):
    y = request.POST['title']
    x = request.POST['body']
    new_item = noteItem(body = x, title = y)
    new_item.save()
    return HttpResponseRedirect('/noteapp/') 

def deleteNotesView(request, i):
    y = noteItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/noteapp/')