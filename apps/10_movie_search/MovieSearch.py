import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")


def main():
    print("-------------------------")
    print("MOVIE SEARCH".center(25, " "))
    print("-------------------------")

    search_loop()


def search_loop():
    title = "required field"

    while title != "x":
        try:
            title = input("Enter movie title(x to exit): ")

            if title != "x":
                result = find_movies(title)
                for i in result:
                    print(f"{i.year} -- {i.title}")

        except ValueError:                                      # handle empty title
            print("Error: title is required")
        except requests.exceptions.ConnectionError:             # handle connection issue
            print("Host unreachable, check your network connection!")
        except Exception as x:                                  # handle other error
            print("Unexpected error. Details: {}".format(x))

    print("Exiting the app...")


def find_movies(title):
    # check if its empty string or white spaces
    if not title or not title.strip():
        raise ValueError("Title is required")

    # Replace spaces with %20
    title_encoded = title.replace(" ", "%20")
    url = f'http://movie_service.talkpython.fm/api/search/{title_encoded}'

    response = requests.get(url)
    data = response.json()

    # get movie data that stored in hits object
    movie_data = data.get("hits")

    #
    movies = [
        MovieResult(**md) for md in movie_data
    ]

    movies.sort(key=lambda m: -m.year)

    return movies


if __name__ == '__main__':
    main()
