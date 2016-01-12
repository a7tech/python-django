from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from movies.forms import CriteriaForm
import json
from movies.models import Movies, Category, Relationship
from django.db.models import Q

# Create your views here.
class MoviesHome(View):
    def get(self, request):
        '''-------------View for the home page----------------'''
        form=CriteriaForm()
        return render(request, 'home.html', {'form':form})

class Moviesfunctions(View):
    '''---------View for handeling movies functionalities-------------''' 
    def get(self, request):
        '''-----------load page view-----------'''
        if request.is_ajax():    
            form=CriteriaForm(request.GET)
            if form.is_valid():
                lan=form.cleaned_data['language']
                genre=form.cleaned_data['genre']
                sort_by=form.cleaned_data['sort_by']
                page_id=int(request.GET.get('page_id',1))
                if lan == 'All':
                    movies_ids=Relationship.objects.all().values_list('movie_id', flat=True)
                    #movies_ids=Relationship.objects.filter(taxonomy_id__movie_type__iexact='Language').values_list('movie_id', flat=True)
                else:
                    movies_ids=Relationship.objects.filter(taxonomy_id__movie_type__iexact='Language',
                                                             taxonomy_id__value__iexact=lan).values_list('movie_id', flat=True)
                if genre == 'All':
                    movies_ids=Relationship.objects.filter(taxonomy_id__movie_type__iexact='Genre',
                                                            movie_id__in=movies_ids).values_list('movie_id', flat=True)      
                else:
                    movies_ids=Relationship.objects.filter(taxonomy_id__movie_type__iexact='Genre',
                                                            taxonomy_id__value__iexact=genre,                          
                                                            movie_id__in=movies_ids).values_list('movie_id', flat=True)        
                movies_objs=Movies.objects.filter(id__in=movies_ids)
                if sort_by == 'ReleaseDate':
                    movies_objs=movies_objs.order_by('-movie_release_date')
                else:
                    movies_objs=movies_objs.order_by('-movie_length')
                count=movies_objs.count()
                if count > (page_id-1)*10:
                    movies_objs=movies_objs[(page_id-1)*10:page_id*10]
                else:
                    movies_objs=[]
                    count=(page_id-1)*10+1    
                response={'result':'SUCCESS', 'message':'Movies List', 'movies':self.MoviesResponse(movies_objs),'total_count':count}
            else:
                response={'result':'FAILED', 'message':'Invalid Request'}
        else:
            response={'result':'FAILED', 'message':'Invalid Request'}        
        return HttpResponse(json.dumps(response))

    def MoviesResponse(self, movie_objs):
        '''------------Function for making response of movies--------------'''
        movies_list=[]
        for m in movie_objs:
            lan_list=[]
            genre_list=[]
            relation_objs=m.relationship_set.all()
            for r in relation_objs:
                if r.taxonomy_id.movie_type.lower()=='genre':
                    genre_list.append(r.taxonomy_id.value.title())
                elif r.taxonomy_id.movie_type.lower()=='language':
                    lan_list.append(r.taxonomy_id.value.title())    
            movies_list.append({'title':m.title,
                                'description':m.description,
                                'featured_image':m.featured_image.url,
                                'movie_length':m.movie_length,
                                'languages':lan_list,
                                'genres':genre_list,
                                'resease_date':m.movie_release_date.strftime('%d-%m-%Y')})
        return movies_list    
