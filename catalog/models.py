from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from datetime import date




# Create your models here.

# 품사 
class PartofSpeech(models.Model):
  name = models.CharField(max_length=200, help_text='품사', unique=True)
  
  def __str__(self):
    return self.name

# 학년
class Grade(models.Model):
  name = models.CharField(max_length=200, help_text='학년', null=True, unique=True)

  def __str__(self):
    return self.name
  
# 학교
class School(models.Model):
  name = models.CharField(max_length=200, help_text='학교', null=True, unique=True)

  def __str__(self):
    return self.name
  
# 학생
class Student(models.Model):
  name = models.CharField(max_length=10, help_text='학생')
  school = models.ForeignKey(School, on_delete=models.SET_NULL, help_text='학교', null=True)
  grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, help_text='학년', null=True)
  admissiondate = models.DateField(help_text='등록일', null=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('student-detail', args=[str(self.id)])

  
# 모의고사 지문
class Article(models.Model):
  title = models.CharField(max_length=200, help_text='제목(예:고3 2023년 3월 18번)')  
  grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, help_text='학년', null=True)
  year = models.CharField(max_length=4, help_text='연도')
  no = models.IntegerField(help_text='문항번호', null=True)
  question = models.CharField(max_length=200, help_text='질문', null=True)    
  answer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text='정답[1-5]', null=True)
  context = models.TextField(max_length=3000, help_text='지문', null=True)
  
  def __str__(self):
      return self.title
  
  def get_absolute_url(self):
      return reverse('article-detail', args=[str(self.id)])
    
# 모의평가 (모의고사 지문 - 학생 평가)
class ArticleTest(models.Model):
  article = models.ForeignKey(Article, on_delete=models.RESTRICT, null=True)
  student = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
  test_date = models.DateField(null=True, blank=True)
  reply = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
  correct = models.BooleanField(null=True, blank=True)
  due_test = models.DateField(null=True, blank=True)
  
  @property
  def is_overdue(self):    
    return bool(self.due_test and date.today() > self.due_test)
    
  class Meta: 
    ordering = ['article']
    
  def __str__(self):
    return f'{self.id} ({self.article.title})'
  
    
# 학교 기출 시험
class SchoolExam(models.Model):
  year = models.CharField(max_length=4, help_text='연도', null=True)
  quarter = models.CharField(max_length=10, help_text='1학기 중간', null=True)
  school = models.ForeignKey(School, on_delete=models.SET_NULL, help_text='학교', null=True)
  grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, help_text='학년', null=True)  
  no = models.IntegerField(help_text='문항번호', null=True)
  question = models.CharField(max_length=200, help_text='질문', null=True)    
  answer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text='정답[1-5]', null=True)
  writing = models.CharField(max_length=1000, help_text='서술형정답', null=True)
  context = models.TextField(max_length=3000, help_text='지문', null=True)
  article = models.ForeignKey(Article, on_delete=models.SET_NULL, help_text='원본', null=True)
  
  def __str__(self):
    return self.year + ' ' + self.quarter
  
  
  