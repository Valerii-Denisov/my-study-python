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

        def get_rating(target_dict: dict) -> float:
            rating = target_dict.get("rating_kinopoisk")
            if rating not in ("", "0"):
                countries = target_dict.get("country")
                if countries.count(",") >= 1:
                    return float(rating)
            return None

        rating_list = [elem for elem in (map(get_rating, list_of_movies)) if elem is not None]
        return sum(rating_list) / len(rating_list)

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

        def get_rating(target_dict: dict, target_rating: Union[float, int]) -> bool:
            film_rating = target_dict.get("rating_kinopoisk")
            if film_rating != "":
                return float(film_rating) >= target_rating
            return None

        result_list = [
            elem
            for elem in map(
                lambda x: x.get("name").count("и") if get_rating(x, rating) else None,
                list_of_movies,
            )
            if elem is not None
        ]
        return sum(result_list)
