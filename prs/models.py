from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    """
    Model representing user
    """
    genderchoices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )


    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    #dob = models.DateField
    #gender = models.CharField(max_length=6, choices=genderchoices)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.email

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class ReportedCases(models.Model):
    """
    Model representing reported cases
    """
    case_id = models.CharField(max_length=30)
    case_user = models.CharField(max_length=15)
    case_date = models.DateTimeField
    #case_loc = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    case_vector = models.CharField(max_length=10)
    case_vec_num = models.PositiveSmallIntegerField
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])
