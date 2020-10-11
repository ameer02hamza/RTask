from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from .models import MpaaRating, MoviesData
from django.views.generic import (ListView, DetailView)


class MoviesList(ListView):
    template_name = "movies_list.html"
    context_object_name = "object"

    def get_queryset(self):
        queryset = MpaaRating.objects.all()
        return queryset


class MoviesDetail(DetailView):
    template_name = "movie_detail.html"
    queryset = MpaaRating.objects.all()
    context_object_name = "object"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MpaaRating, mdata=id_)

# function to store data in database
def Movies_ist(request):
    movies_data = open('/root/Rapidev/Rapidev/JSONFile/movies.json', )
    data = json.load(movies_data)
    for i in range(len(data)):

        genrebra = str(data[i]['genre'])[1:-1]
        removeqouts = genrebra.replace("'", "")
        removedoubleQ = removeqouts.replace('"', "")
        M = MoviesData(id=data[i]['id'], name=data[i]['name'], description=data[i]['description'],
                       imgPath=data[i]["imgPath"], duration=data[i]['duration'],
                       genre=removedoubleQ, language=data[i]['language'],
                       userRating=data[i]["userRating"])
        M.save()
        p = MoviesData.objects.get(id=M.id)
        Mp = MpaaRating(type=data[i]["mpaaRating"]["type"], label=data[i]["mpaaRating"]["label"], mdata=p)
        Mp.save()
        print(Mp, " dif ", M)
    M = MpaaRating.objects.all()
    dict = {"data": M}
    return render(request, "movies_list.html", dict)




