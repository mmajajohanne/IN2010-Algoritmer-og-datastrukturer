import csv
from collections import defaultdict
from graphviz import Graph


def les_movies(filename):
    # leser inn filen movies.tsv og lagrer tt-id og rating i en dictionary
    movies = {}
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")  # lagrer og splitter radene i lister
        for row in reader:
            tt_id, title, rating, votes = row  # lagrer verdiene på hver rad (liste)
            movies[tt_id] = float(rating)  # tar vare på ratingen
    return movies


def les_actors(filename):
    # Les inn filen actors.tsv og lagrer skuespiller-ID og filmene de har spilt i, samt navnene deres
    actors = {}
    names = {}  # Ordbok for å koble skuespiller-ID med navn
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            nm_id = row[0]  # Skuespillerens ID
            name = row[1]  # Skuespillerens navn
            movies_played = row[2:]  # Alle filmene skuespilleren har spilt i
            actors[nm_id] = movies_played
            names[nm_id] = name  # Lagre navnet med ID som nøkkel
    return actors, names


def bygg_graf(actors, movies):
    # bruker en ordbok for å representere grafen
    graf = defaultdict(list)  # nøkkel: skuespiller, verdi: (skuespiller, film, rating)

    # iterer gjennom hver skuespiller og deres filmer
    for nm_id, movie_list in actors.items():
        for i in range(len(movie_list)):
            for j in range(i + 1, len(movie_list)):
                movie_1 = movie_list[i]
                movie_2 = movie_list[j]

                # hvis filmene finnes i movies dictionary
                if movie_1 in movies and movie_2 in movies:
                    rating_1 = movies[movie_1]
                    rating_2 = movies[movie_2]

                    # legg til kant mellom to skuespillere med vekt (rating)
                    for co_actor in actors:
                        if nm_id in actors:
                            rating = movies.get(movie_list[i])
                            graf[nm_id].append((co_actor, movie_1, rating))
    return graf


def visualiser_graf(graf):
    dot = Graph(
        comment="Film-relasjoner mellom skuespillere", engine="sfdp"
    )  # Prøv 'sfdp' eller 'neato'

    for skuespiller, kanter in graf.items():
        for co_actor, film, rating in kanter:
            # Legg til kant mellom skuespillere
            dot.edge(skuespiller, co_actor, label=f"{film} (Rating: {rating})")

    # Skriv ut .dot-filen og visualiser grafen
    dot.render("graf_visualisering", view=True)


def main():
    movies = les_movies("marvel_movies.tsv")
    actors, names = les_actors("marvel_actors.tsv")

    graf = bygg_graf(actors, movies)

    # Visualiser grafen ved hjelp av Graphviz
    visualiser_graf(graf)


if __name__ == "__main__":
    main()
