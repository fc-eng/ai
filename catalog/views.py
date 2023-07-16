from django.shortcuts import render

# Create your views here.
from .models import Article, School, Student, ArticleTest

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_articles = Article.objects.all().count()
    num_schools = School.objects.all().count()
    
    #Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)   
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_articles': num_articles,
        'num_schools': num_schools,  
        'num_visits' : num_visits,      
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
  
from django.views import generic

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 2

class ArticleDetailView(generic.DetailView):
    model = Article
    
class StudentDetailView(generic.DetailView):
    model = Student
      
from django.contrib.auth.mixins import LoginRequiredMixin

class DueTestsByUserListView(LoginRequiredMixin,generic.ListView):    
    model = ArticleTest
    template_name = 'catalog/articletest_list_duetests_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            ArticleTest.objects.filter(student=self.request.user)
            .filter(correct=False)
            .order_by('due_test')
        )

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Student

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'school', 'grade', 'admissiondate']
    initial = {'admissiondate': '06/01/2023'}    

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
