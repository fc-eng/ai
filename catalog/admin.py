from django.contrib import admin
from .models import PartofSpeech, Grade, School, Student, SchoolExam, Article, ArticleTest

class StudentAdmin(admin.ModelAdmin):
  list_display = ('name', 'grade', 'school') 
  fields = ['name', ('school', 'grade'), 'admissiondate']

class SchoolExamAdmin(admin.ModelAdmin):
  list_display = ('year', 'quarter', 'school', 'grade', 'article',)
  list_filter = ('quarter',)
 
  fieldsets = (
    (None, {
      'fields': (('year', 'quarter'), ('school', 'grade'))
    }), 
    ('문항', {
      'fields': (('no', 'question'), ('answer', 'writing'), 'context', 'article')
    })
  )
  
class SchoolExamInline(admin.TabularInline):
  model = SchoolExam

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'question', 'answer')
  inlines = [SchoolExamInline]
  
@admin.register(ArticleTest)
class ArticleTest(admin.ModelAdmin):
  list_display = ('article', 'student', 'test_date', 'reply', 'correct', 'due_test')

# Register your models here.
admin.site.register(PartofSpeech)
admin.site.register(Grade)
admin.site.register(School)
#admin.site.register(Student)
#admin.site.register(SchoolExam)
#admin.site.register(Article)


#Register the admin class with the associated model
admin.site.register(Student, StudentAdmin)
admin.site.register(SchoolExam, SchoolExamAdmin)


