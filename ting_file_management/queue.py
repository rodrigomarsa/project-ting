from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if not self.__data == []:
            return self.__data.pop(0)
        else:
            return None

    def search(self, index):
        if not 0 <= index <= len(self.__data) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self.__data[index]
