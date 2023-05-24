from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="enter the book genre")
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='enter the text in brief')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text='Select genre')
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'maintainance'),
        ('o', 'on loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability'
    )
    
    def __str__(self) -> str:
        return f"{self.id} ({self.title})"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'