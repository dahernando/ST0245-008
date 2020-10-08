class Node:
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self,head=None):
        self.head = head
        
    def length(self):
        current = self.head
        if current == None:
            return 0
        else:
            counter = 0
            while(current!=None):
                counter +=1
                current = current.next 
            return counter
        
    def insertByTail(self,element):
        if self.head ==None:
            self.head = Node(element)
        else:
            current = self.head
            while(current.next!=None):
                current = current.next
            newNode = Node(element)
            current.next = newNode
        
    def insertByHead(self,element):
        if self.head ==None:
            self.head = Node(element)
        else:
            newNode = Node(element)
            newNode.next = self.head
            self.head = newNode
            
    def insertByPosition(self, element, position):
        newNode = Node(element)
        if self.head==None or position==0:
            self.head = newNode
        elif position<self.size():
            current = self.head
            counter =1 
            while(current != None and counter <position-1):
                current = current.next
                counter +=1
            newNode.next = current.next
            current.next = newNode
        else:
            print("invalided position")
        
    def reverse(self,changes):
        counter = 0
        current = self.head
        pre =None
        while(counter<changes):
            while(current.next!=None):
                pre = current
                current = current.next
            pre.next = None
            aux = self.head
            current.next = aux
            self.head = current
            counter+=1
    
    def toPrint(self):
        current = self.head
        while(current.next!=None):
            print(current.data,"->",end=" ")
            current = current.next
        print(current.data)
            
    def size(self):
        current = self.head
        counter = 0
        while(current!=None):
            current = current.next
            counter+=1
        return counter
            

def main():
    myList = LinkedList()
    myList.insertByTail(5)
    myList.insertByHead(3)
    myList.insertByHead(2)
    myList.toPrint()
    myList.reverse(3)
    myList.toPrint()
    
if __name__ =='__main__':
    main()
    
            
            
    
    