# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        if self.iter.hasNext():
            self.buffer = self.iter.next()
        else:
            self.buffer = None
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        

    def peek(self) -> int:
        return self.buffer
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        ans = self.buffer
        if self.iter.hasNext():
            self.buffer = self.iter.next()
        else:
            self.buffer = None
        return ans
        """
        :rtype: int
        """
        

    def hasNext(self):
        return self.buffer is not None
        """
        :rtype: bool
        """
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].