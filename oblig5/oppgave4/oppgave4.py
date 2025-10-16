import csv
from collections import defaultdict
from collections import deque


def les_movies(filename):
    # leser inn filen movies.tsv og lagrer tt-id og rating i en dictionary
    movies = {}
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")  # leser og splitter radene i lister
        for row in reader:
            tt_id, title, rating, votes = row  # lagrer verdiene på hver rad (liste)
            movies[tt_id] = {
                "title": title,
                "rating": float(rating),
            }  # tar vare på både tittel og rating
    return movies


def les_actors(filename):
    # leser inn filen actors.tsv og lagrer skuespiller-ID og filmene de har spilt i, samt navnene deres
    actors = {}
    names = {}  # ordbok for å koble skuespiller-ID med navn
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            nm_id = row[0]  # skuespillerens ID
            name = row[1]  # skuespillerens navn
            movies_played = row[2:]  # alle filmene skuespilleren har spilt i
            actors[nm_id] = movies_played
            names[nm_id] = name  # lagre navnet med ID som nøkkel
    return actors, names


def bygg_graf(actors, movies, names):
    graf = defaultdict(list) #graf er en dictionary med lister som verdier
    film_til_skuespillere = defaultdict(list) #dictionary for å koble filmer med skuespillere

    # bygger omvendt indeks for filmer (de som har gyldige tt-id i movies.tsv)
    for nm_id, movie_list in actors.items():
        for movie in movie_list:
            if movie in movies:
                film_til_skuespillere[movie].append(nm_id)

    # kobler skuespillere sammen basert på felles filmer
    for movie, skuespillere in film_til_skuespillere.items():
        movie_data = movies[movie]
        title = movie_data["title"]
        rating = movie_data["rating"]
        weight = 10 - rating  # Vekten på kanten (10 - rating)

        # kobler alle skuespillere som spilte i samme film
        for i in range(len(skuespillere)):
            for j in range(i + 1, len(skuespillere)):
                skuespiller1 = skuespillere[i]
                skuespiller2 = skuespillere[j]
                graf[skuespiller1].append((skuespiller2, title, weight, rating))
                graf[skuespiller2].append((skuespiller1, title, weight, rating))

    # legger til skuespillere som ikke har noen filmer, slik at de også blir med i grafen
    for nm_id in actors:
        if nm_id not in graf:
            graf[nm_id] = []  # skuespilleren har ingen naboer

    return graf


def tell_noder_og_kanter(graf):
    # antall noder er antall unike skuespillere (nøklene i grafen)
    antall_noder = len(graf)

    # teller unike kanter ved å iterere gjennom kantene for hver skuespiller
    antall_kanter = 0
    for skuespiller, kanter in graf.items():
        antall_kanter += len(kanter)

    # siden grafen er urettet, deles antall kanter på 2
    antall_kanter //= 2

    # skriver ut resultatene
    print(f"Antall noder (skuespillere): {antall_noder}")
    print(f"Antall kanter (koblinger mellom skuespillere): {antall_kanter}")


def finn_korteste_sti(graf, start, slutt, names):
    # bruker BFS for å finne korteste sti
    queue = deque([(start, [])])  # queue holder (nåværende skuespiller, sti så langt)
    visited = {start}  # holder oversikt over besøkte noder

    while queue:
        current_actor, path = queue.popleft()

        if current_actor == slutt:
            # har funnet en sti, returner den sammen med filmene
            return path

        # går gjennom naboene (skuespillere de har spilt i film med)
        for co_actor, movie, weight, rating in graf[current_actor]:
            if co_actor not in visited:
                visited.add(co_actor)
                # legger til co-actor i stien og fortsett BFS
                queue.append(
                    (co_actor, path + [(current_actor, movie, rating, co_actor)])
                )

    return None  # returnerer None hvis ingen sti ble funnet


def skriv_ut_sti(sti, names):
    if not sti:
        print("Ingen sti funnet.")
        return

    # starter utskrift med den første skuespilleren
    print(names[sti[0][0]])
    for skuespiller1, film, rating, skuespiller2 in sti:
        print(f"===[ {film} ({rating}) ] ===> {names[skuespiller2]}")

def main():
    movies = les_movies("movies.tsv")
    actors, names = les_actors("actors.tsv")

    graf = bygg_graf(actors, movies, names)

    print(f"Oppgave 1.\n")
    tell_noder_og_kanter(graf)

    print("-----------------------------------------------------------------------")
    # Eksemplene fra oppgaven:
    print(f"\nOppgave 2.")
    test_par = [
        ("nm2255973", "nm0000460"),  # Donald Glover og Jeremy Irons
        ("nm0424060", "nm8076281"),  # Scarlett Johansson og Emma Mackey
        ("nm4689420", "nm0000365"),  # Carrie Coon og Julie Delpy
        ("nm0000288", "nm2143282"),  # Christian Bale og Lupita Nyong'o
        ("nm0637259", "nm0931324"),  # Tuva Novotny og Michael K. Williams
    ]

    for start, slutt in test_par:
        print(f"\nFinner korteste sti mellom {names[start]} og {names[slutt]}:\n")
        sti = finn_korteste_sti(graf, start, slutt, names)
        skriv_ut_sti(sti, names)



if __name__ == "__main__":
    main()
