'Doubly Linked List'
'2023.4.5'

import re
class Node():
#to class the nodes that will be used
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkList():
#to class the doublylinklist
    def __init__(self):
        self.head = None


    def is_empty(self):
        return not self.head
    #to check if the list is an empty one

    def show(self):
        if self.is_empty():
            print('empty list')
            return
        cur = self.head
        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next
    #to show the list

    def insert(self, data):
    #to define the insert instruct
        node = Node(data)
        if self.is_empty():
            self.head = node
            return
        """if the list was empty then the hand of the listhead should be directed to node
        """
        node.next = self.head
        self.head.prev = node
        self.head = node
        """if the list was not empty then use double way to link node with self
           then also direct the hand of the list head  to node 
        """
    def deleteFirst(self):
        cur = self.head
        if self.is_empty():
            print('error')
            return
        self.head = self.head.next
        if cur.next:
            cur.next.prev = None
        #the point is to check if the first one is also the only one+



    def deleteLast(self):
        cur = self.head
        if self.is_empty():
            print('error')
            return
        while cur.next != None:
            cur = cur.next
        if cur.prev == None and cur.next == None:
            self.head = None
            return
        cur.prev.next = None
        #the point is to check if the last one is also the only one

    def delete(self, value):
        cur = self.head
        if self.is_empty():
            print('error')
            return
        while cur is not None:
            if cur.data == value:
                if cur == self.head:
                    self.head = self.head.next
                    if cur.next:
                        cur.next.prev = None
                    return
                #to check if the data is the first one
                if cur.next is None:
                    if cur.prev:
                        cur.prev.next = None
                    return
                #to check if the data is the last one
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next

def inputs():
    #the main function to deal with the inputs
    d = DoublyLinkList()
    n = int(input('please input how many commands do you want:'))
    nd = 0
    #get the number of delete instructs
    # get the command numbers
    if n > 2000000 or n == 0:
        print('error')
    else:
        for ns in range(n):
            ins = input('please input the instruct')
            if ins == 'deleteFirst':
                d.deleteFirst()
                nd += 1
            elif ins == 'deleteLast':
                d.deleteLast()
                nd += 1
            elif 'insert'in ins:
                num = int(re.findall('\d+', ins)[0])
                if num >= 10**9 or num <= 0:
                    print('error')
                    return
                d.insert(num)
            elif 'delete'in ins:
                num = int(re.findall('\d+', ins)[0])
                if num >= 10**9 or num <= 0:
                    print('error')
                    return
                d.delete(num)
                nd += 1
            if nd > 20:
                print('error')
                return
            ns += 1
    d.show()


if __name__ == '__main__':
    inputs()