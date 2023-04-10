class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return input_list
        max_value = input_list[0]
        for items in input_list:
            if items > max_value:
                max_value = items
        replaced_list = list(
            map(lambda replaced: max_value if replaced > 0 else replaced, input_list)
        )
        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if len(input_list) == 0:
            return -1

        mid = len(input_list) // 2

        if input_list[mid] == query:
            return mid

        elif query < input_list[mid]:
            return ListExercise.search(input_list[:mid], query)

        else:
            new_mid = mid + 1
            result = ListExercise.search(input_list[new_mid:], query)
            if result == -1:
                return -1
            else:
                return mid + 1 + result
