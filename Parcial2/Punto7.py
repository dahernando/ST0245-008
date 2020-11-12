#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:04:08 2020

@author: daho
"""

class Node:
    def __init__(self,data, next =None):
        self.data = data
        self.next = next
        
class Stack:
    
    def __init__(self):
        self.head =None
    
    def push(self,element):
        if self.head == None:
            self.head = Node(element)
        else:
            newNode = Node(element)
            newNode.next = self.head
            self.head = newNode
    
    def toPrint(self):
        if self.head==None:
            print("Vacia")
            return
        aux = self.head
        while(aux.next!=None):
            print(aux.data,"->",end=" ")
            aux = aux.next
        print(aux.data)
    
    def CalculateAverage(self):
        aux = self.head
        average = 0
        index =0
        while(aux!=None):
            average+=aux.data
            aux = aux.next
            index+=1
        return average/index  
    
    def pop(self):
        if self.head ==None:
            print("No hay datos en la pila")
            return
        aux = self.head.next
        self.head.next = None
        self.head = aux
        
def inversa(pila):
    aux = pila.head
    pilaAux = Stack()
    while(aux!=None):
        pilaAux.push(aux.data)
        aux = aux.next
        pila.pop()
    return pilaAux

def main():
     myPila =Stack()
     myPila.push(3)
     myPila.push(6)
     myPila.push(2)
     myPila.push(1)
     myPila.push(5)
     print("Pila creada:")
     myPila.toPrint()
     reverse = inversa(myPila)
     print("******************************")
     print("Pila nueva:")
     reverse.toPrint()
     print("******************************")
     print("Pila que habia creada:")
     myPila.toPrint()

if __name__=='__main__':
    main()
