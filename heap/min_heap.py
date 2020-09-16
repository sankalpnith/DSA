class MinHeap:
    def __init__(self):
        self.size = 0
        self.data = []

    def parent_index(self, i):
        if i <= 0 or i > self.size:
            return -1
        return (i-1)//2

    def left_child_index(self, i):
        index = 2*i+1
        return -1 if index >= self.size else index

    def right_child_index(self, i):
        index = 2*i+2
        return -1 if index >= self.size else index

    def insert(self, value):
        self.data.append(value)
        self.size += 1
        self.percolate_up(self.size - 1)

    def delete_min(self):
        minimum_value = self.data[0]
        self.data[0] = self.data[self.size-1]
        self.data.pop()
        self.size -= 1
        self.percolate_down(0)
        return minimum_value

    # With Recursion
    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        if parent_index != -1 and self.data[parent_index] > self.data[index]:
            self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
            self.percolate_up(parent_index)

    # Without Recursion
    def percolate_up(self, index):
        parent_index = self.parent_index(index)
        while parent_index >= 0:
            if self.data[parent_index] > self.data[index]:
                self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
                parent_index = self.parent_index(parent_index)

    # With Recursion
    def percolate_down(self, index):
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)
        minimum_index = index
        # change < to > for Max heap
        if left_child_index != -1 and self.data[left_child_index] < self.data[index]:
            minimum_index = left_child_index
        # change < to > for Max heap
        if right_child_index != -1 and self.data[right_child_index] < self.data[minimum_index]:
            minimum_index = right_child_index

        if minimum_index != index:
            self.data[minimum_index], self.data[index] = self.data[index], self.data[minimum_index]
            self.percolate_down(minimum_index)

    # Without Recursion
    def percolate_down(self, index):
        while index*2+1 <= self.size:
            left_child_index = self.left_child_index(index)
            right_child_index = self.right_child_index(index)
            minimum_index = index
            # change < to > for Max heap
            if left_child_index != -1 and self.data[left_child_index] < self.data[index]:
                minimum_index = left_child_index
            # change < to > for Max heap
            if right_child_index != -1 and self.data[right_child_index] < self.data[minimum_index]:
                minimum_index = right_child_index

            if minimum_index != index:
                self.data[minimum_index], self.data[index] = self.data[index], self.data[minimum_index]
                index = minimum_index
            else:
                break

    def build_min_heap(self, arr):
        if not arr:
            print("Empty List")
        self.data.extend(arr)
        self.size = len(self.data)
        index = self.parent_index(self.size)
        while index >= 0:
            self.percolate_down(index)
            index -= 1
