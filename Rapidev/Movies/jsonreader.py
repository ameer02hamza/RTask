#this code i tried on django shell for testing
import json
# from .models import MpaaRating, MoviesData
movies_data = open('/root/Rapidev/Rapidev/JSONFile/movies.json',)

data = json.load(movies_data)
for i in range(len(data)):
    gen = str(data[i]['genre'])[1:-1:]
    p = gen.replace("'", "")
    m = p.replace('"', "")
    print(m)
# genre_data = []
# name = []
# description = []
# M = MoviesData(id = data[0]['id'], name= data[0]['name'], description=data[0][description],
#                imgPath=data[0]["imgPath"], duration= data[0]['duration'],
#                genre=m, language= data[0]['language'],
#                userRating=data[0]["userRating"])
# p = MoviesData.objects.get(id=M.id)
# Mp = MpaaRating(type=data[0]["mpaaRating"]["type"], label = data[0]["mpaaRating"]["label"], mdata=p)
# for i in range(len(data)):
#     try:
#         gendata = genre_data.append(data[i]["genre"])
#
#     except:
#         pass
#
# for i in range(len(genre_data)):
#         try:
#             print(data[i]["mpaaRating"]["type"])
#         except:
#             pass

