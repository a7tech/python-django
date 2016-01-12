from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.forms import forms

def ImageValidator(value):
    '''----------Validator for image file-------------'''
    file_obj=value.file   
    try:    
        content_type=file_obj.content_type
        if content_type in ['image/jpg','image/jpeg','image/png','image/gif']:
            
            if file_obj.size > 1048576 * 2:
                raise forms.ValidationError(_('Please upload file less than 2MB.'))    
        else:
            raise forms.ValidationError(_('Please upload valid image file.'))    
    except AttributeError:
        pass



class Movies(models.Model):
    '''------------Model for Movie table---------------'''
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    featured_image=models.FileField(upload_to='images', validators=[ImageValidator,])
    movie_length=models.PositiveSmallIntegerField()
    movie_release_date=models.DateField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    '''------------Model for movie category-------------------'''
    movie_type=models.CharField(max_length=30)
    value=models.CharField(max_length=30)

    def __unicode__(self):
        return self.movie_type+'-'+self.value 
        
class Relationship(models.Model):
    '''-------------Relation between movie and Category---------'''
    taxonomy_id=models.ForeignKey(Category)
    movie_id=models.ForeignKey(Movies)           