"""
Heap data structure.
"""


class Heap:
    """
    Priority queue using binary min-heap.
    """

    def __init__(self, array=None):
        """
        Initializes a heap from the given list. Each item of the list should
        be a 2-tuple (priority, item).
        """
        array = [] if array is None else array

        # first copy the array to heap
        self.heap = list(array)
        self.index = {x[1]: i for i, x in enumerate(array)}

        # then perform movie_down() for all non-leaf items in bottom-up way
        for i in range(len(array) >> 1, -1, -1):
            self._move_down(i)

    def __repr__(self):
        return repr(self.heap)

    def __len__(self):
        return len(self.index)

    def __getitem__(self, item):
        """
        Returns the priority of the given item.
        """
        return self.heap[self.index[item]][0]

    def __contains__(self, item):
        """
        Checks if heap contains item.
        """
        return item in self.index

    def __delitem__(self, item):
        """
        Delete the item from the heap.
        """
        i = self.index[item]
        self.heap[i] = (float("-inf"), item)
        self._move_up(i)
        self.pop()

    def __setitem__(self, item, priority):
        """
        Add or update an item with priority.
        """
        # if item already exists
        if item in self.index:
            # get the old index and priority
            _i = self.index[item]
            _priority = self.heap[_i][0]

            # update the priority in the heap
            self.heap[_i] = (priority, item)

            # move the item up or down by comparing old vs new priority
            if priority < _priority:
                self._move_up(_i)
            elif priority > _priority:
                self._move_down(_i)

        # if item doesn't exist, add the item at the end of heap and move up
        else:
            i = len(self.heap)
            self.heap.append((priority, item))
            self.index[item] = i
            self._move_up(i)

    def _move_up(self, i):
        """
        Move an item up the heap tree until the heap invariant is satisfied.
        """
        while i:
            p = (i - 1) >> 1
            if self.heap[p][0] <= self.heap[i][0]:
                break
            self._swap(p, i)
            i = p

    def _move_down(self, i):
        """
        Move an item down the heap tree until the heap invariant is satisfied.
        """
        h = self.heap
        N = len(self.heap)
        while True:
            l = (i << 1) + 1  # index of left child
            r = (i + 1) << 1  # index of right child
            low = i
            if l < N and h[l][0] < h[low][0]:
                low = l
            if r < N and h[r][0] < h[low][0]:
                low = r
            if low == i:
                break
            self._swap(i, low)
            i = low

    def _swap(self, i, j):
        """
        Swap two items in the heap.
        """
        a, b = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = b, a
        self.index[a[1]] = j
        self.index[b[1]] = i

    def push(self, item, priority=1):
        """
        Add or update item to heap with priority.
        """
        self[item] = priority

    def peek(self):
        """
        Returns the root of heap without removing it.
        """
        priority, item = self.heap[0]
        return priority, item

    def pop(self):
        """
        Returns the root of heap after removing it from the heap.
        """
        priority, item = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop(-1)
            self.index[self.heap[0][1]] = 0
            self._move_down(0)
        del self.index[item]
        return item, priority


def min_heapify(array, index):
    """
    Push the given root down to its proper place.
    """
    left = 2 * index + 1
    right = left + 1
    smallest = index

    if left < len(array) and array[left] < array[smallest]:
        smallest = left

    if right < len(array) and array[right] < array[smallest]:
        smallest = right

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest)


def build_min_heap(array):
    """
    Build a min-heap from an existing array.
    """
    # all non-leaf nodes (bottom-up)
    for i in range(len(array) // 2, -1, -1):
        min_heapify(array, i)

    return array


def min_heap_push(array, key):
    """
    Push an item to heap.
    """
    index = len(array)
    array.append(key)
    while index > 0:
        parent = (index - 1) // 2
        if array[index] >= array[parent]:
            break
        array[index], array[parent] = array[parent], array[index]
        index = parent


def min_heap_pop(array):
    """
    Pop out the root of heap (min element).
    """
    out = array[0]  # item to return
    last_item = array.pop(-1)
    if array:
        array[0] = last_item
        min_heapify(array, 0)
    return out
