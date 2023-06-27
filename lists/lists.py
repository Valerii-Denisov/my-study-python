class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        new_list = input_list.copy()
        counter = 0
        for element in new_list:
            if element > 0:
                new_list[counter] = max(input_list)
            counter += 1
        return new_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        first = 0
        last = len(input_list) - 1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first + last) // 2
            if input_list[mid] == query:
                index = mid
            else:
                if query < input_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index
