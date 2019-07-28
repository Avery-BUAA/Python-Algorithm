"""
主要是在push的时候保证元素在list1的最前面
"""
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1 = []
        self.list2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if len(self.list1) == 0:
            self.list1.append(x)
        else:
            while self.list1:
                self.list2.append(self.list1.pop(0))
            self.list1.append(x)
            while self.list2:
                self.list1.append(self.list2.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.list1) != 0 :
            return self.list1.pop(0)
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.list2:
            self.list1.append(self.list2.pop(0))
        return self.list1[-1]
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.list1)==0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()