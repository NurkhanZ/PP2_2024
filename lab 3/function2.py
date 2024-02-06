# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
movie_name = str(input())
def find_by_movie(movie_dict,movie_name):
    for movie in movie_dict:
        if movie["name"] == movie_name:
            if movie["imdb"] > 5.5:
                return True
    return False
print(find_by_movie(movies, movie_name))

#2
def sublist_of_movies(movie_dict):
    sublist = []
    for movie in movie_dict:
        if movie["imdb"] > 5.5:
            sublist.append(movie["name"])
    print(sublist)
sublist_of_movies(movies)

#3
category_name = str(input())
def movies_by_category(movie_dict, category_name):
    sublist = []
    for movie in movie_dict:
        if movie["category"] == category_name:
            sublist.append(movie["name"])
    print(sublist)
movies_by_category(movies, category_name)

#4
def average_imdb_by_movies(movie_dict):
    sum = 0
    for movie in movie_dict:
        sum += movie["imdb"]
    avg = sum / len(movie_dict)  
    print(avg)
average_imdb_by_movies(movies)

#5
category_name = str(input())
def average_imdb_by_category(movie_dict, category_name):
    sum = 0
    count = 0
    for movie in movie_dict:
        if movie["category"] == category_name:
            sum += movie["imdb"]
            count += 1
    avg = sum / count
    print(avg)
average_imdb_by_category(movies, category_name)