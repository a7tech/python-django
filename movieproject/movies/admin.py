from django.contrib import admin

# Register your models here.
from movies.models import Movies, Category, Relationship

@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    '''----------Admin for movie modal----------'''
    list_display = ['id', 'title', 'description',
                    'movie_length','movie_release_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''------------Admin for Category table------------'''
    list_display = ['id', 'movie_type', 'value']

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    '''------------Admin for Relationship table----------'''
    list_display = ['taxonomy_id', 'movie_id']        