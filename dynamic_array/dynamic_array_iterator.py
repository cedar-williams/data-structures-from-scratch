class DynamicArrayIterator:
    def __init__(self, dynamic_array) -> None:
        self.dynamic_array = dynamic_array
        self.cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_index >= len(self.dynamic_array):
            raise StopIteration
        return_data = self.dynamic_array.get(self.cur_index)
        self.cur_index += 1
        return return_data