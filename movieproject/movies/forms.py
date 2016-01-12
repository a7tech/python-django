from django import forms

class CriteriaForm(forms.Form):
    '''---------Form for filters and sorting parameters---------'''
    language=forms.ChoiceField(label="Language", choices=(('All','All'),
                                                          ('English','English'),
                                                          ('Hindi','Hindi')))
    genre=forms.ChoiceField(label="Genre", choices=(('All','All'),
                                                    ('Action','Action'),
                                                    ('Comedy','Comedy'),
                                                    ('Sci-Fi','Sci-Fi')))
    sort_by=forms.ChoiceField(label="Sort by", choices=(('ReleaseDate','Release Date'),
                                                    ('Length','Length')))




