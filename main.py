import requests

def movie_info(name):
    api_key = "26b4c440"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={name}"
    response = requests.get(url)
    movie_info_json = response.json()

    if movie_info_json["Response"] == "True":
        print("Title:", movie_info_json.get("Title"))
        print("Year:", movie_info_json.get("Year"))
        print("Time:", movie_info_json.get("Runtime"))
        print("Genre:", movie_info_json.get("Genre"))
        print("Director:", movie_info_json.get("Director"))
        print("Writer:", movie_info_json.get("Writer"))
        print("Actors:", movie_info_json.get("Actors"))
        print("Awards:", movie_info_json.get("Awards"))
        print("BoxOffice:", movie_info_json.get("BoxOffice"))
        print("Metascore:", movie_info_json.get("Metascore"))
        print("IMDB:", movie_info_json.get("imdbRating"))
    else:
        print("Movie not found!")

print("# Welcome to Movie Info Finder #")
print()
print("Write the Movie Name, Example: Fight Club")
print()

movie_name = input("Movie Name: ")
print("----------")
movie_info(movie_name)