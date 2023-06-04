from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from .models import Book, BookInstance, Author, Genre
from django.views import generic

def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_visits' : num_visits, 
    }
    
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
   
    
    def get_context_data(self) -> Dict[str, Any]:
        context = super().get_context_data()
        # context['onlybook'] = Book.objects.all()[1]
        return context  