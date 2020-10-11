from django.contrib import admin
from .models import MoviesData, MpaaRating

class MData(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'genre')


admin.site.register(MoviesData, MData)


class MpaRating(admin.ModelAdmin):
    list_display = ('id', 'label', 'type', 'mdata')


admin.site.register(MpaaRating, MpaRating)