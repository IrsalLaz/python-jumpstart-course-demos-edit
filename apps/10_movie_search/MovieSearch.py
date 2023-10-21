import requests


def main():
    print("-------------------------")
    print("MOVIE SEARCH".center(25, " "))
    print("-------------------------")

    search_loop()


def search_loop():
    title = ""

    while title != "x":
        try:
            title = input("Enter movie title(x to exit): ")

            if title != "x":
                find_movies(title)

        except ValueError:
            print("Error: title is required")

        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print("Exiting the app...")


def find_movies(title):
    url = f'http://movie_service.talkpython.fm/api/search/{title}'

    response = requests.get(url)
    data = response.json()

    print(data)


if __name__ == '__main__':
    main()
