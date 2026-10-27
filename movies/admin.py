from django.contrib import admin
from .models import Movie, Review, Genre

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    list_display = ('id', 'name', 'price', 'is_available', 'display_genres')
    list_editable = ('is_available',)
    filter_horizontal = ('genre',)

    def display_genres(self, obj):
        return ", ".join(genre.name for genre in obj.genre.all())
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Genre)

    