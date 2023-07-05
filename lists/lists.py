class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        result_list = input_list.copy()
        max_element = 0
        for elem in input_list:
            if elem > max_element:
                max_element = elem
        for index, element in enumerate(result_list):
            if element > 0:
                result_list[index] = max_element
        return result_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def recursive_search(target_list: list[int], element: int, start: int, finish: int) -> int:
            """
            Функция рекурсивного двоичного поиска индекса элемента.

            :param target_list: Целевой список
            :param element: Искомый элемент
            :param start: Индекс начального элемента поиска
            :param finish: Индекс конечного элемента поиска
            :return: Номер элемента
            """
            if finish < start:
                return -1
            middle = (start + finish) // 2
            if target_list[middle] == element:
                return middle
            elif target_list[middle] < element:
                return recursive_search(
                    target_list,
                    element,
                    middle + 1,
                    finish,
                )
            else:
                return recursive_search(
                    target_list,
                    element,
                    start,
                    middle - 1,
                )

        start = 0
        finish = len(input_list) - 1
        return recursive_search(input_list, query, start, finish)
