from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        more_2_countries_movies = []
        for movie in list_of_movies:
            if (
                movie["rating_kinopoisk"]
                and float(movie["rating_kinopoisk"]) != 0
                and movie["country"].count(",") >= 1
            ):
                more_2_countries_movies.append(movie)
        rating = map(lambda movie: float(movie["rating_kinopoisk"]), more_2_countries_movies)
        return sum(rating) / len(more_2_countries_movies)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        rating_movies = []
        for movie in list_of_movies:
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating:
                rating_movies.append(movie)
        letters = map(lambda movie: movie["name"].count("и"), rating_movies)
        return sum(letters)
