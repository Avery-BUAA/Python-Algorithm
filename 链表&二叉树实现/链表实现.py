class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class Single_link(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def add(self,item):
        node = Node(item)
        node.next = self._head
        self._head = node
    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def length(self):
        count = 0
        cur = self._head
        while cur:
            cur = cur.next
            count +=1
        return count

    def append(self,item):
        node = Node(item)
        cur = self._head
        if self._head == None:
            self.add(item)
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        node = Node(item)
        cur = self._head
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            pre = None
            while pos>0:
                pre = cur
                cur = cur.next
                pos -=1

            pre.next = node
            node.next = cur

    def remove(self,target):
        pre = None
        cur = self._head


        while cur:
            if cur.item == target:
                #如果是第一个就删除节点
                if not pre:
                    self._head = cur.next
                else:
                    pre.next =cur.next
                break
            else:
                pre = cur
                cur = cur.next


s=Single_link()
s.append(1)
s.append(2)
s.append(3)
s.insert(0,"aa")
s.remove(1)
print(s.length())
print(s.is_empty())
s.travel()
