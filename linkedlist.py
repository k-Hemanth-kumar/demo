'''class Node:
    def __init__(self ,data=None,next=None):
        self.data=data
        self.next=next   
class Linkedlist():
    def __init__(self):
        self.head=None
    def inserting_begining(self,data):
        node=Node(data,self.head)
        self.head=node
        return 
    def print_list(self):
        if self.head is None:
            print("nothing will be printed")
            return
        itr=self.head
        val=''
        while itr:
            val+=str(itr.data)+" " if itr.next else str(itr.data)
            itr=itr.next
        return val
    def len_of_list(self,c=0):
        if self.head is None:
            print("you don't have inseted any value to the linkedlist")
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    def max_no(self,c=0):
        itr=self.head
        while itr:
            if itr.data>c:
                c=itr.data
            itr=itr.next
        return c
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def inser_values(self,datalist):
        for d in datalist:
            self.insert_at_end(d)
    
    def insert_at(self,index,data):
        if index<0 and index>self.len_of_list():
            raise Exception("the given index of out of range! please give in range index")
        if index==0:
            self.inserting_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def remove_at(self,index):
        if index<0 or index>self.len_of_list():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
if __name__=="__main__":
    l1=Linkedlist()
    n=[1,2,3,4]
    for i in n:
        l1.inserting_begining(i)
    print(l1.len_of_list())
    (l1.inserting_begining(12))
    l1.inserting_begining(6)
    (l1.inserting_begining(16))
    l1.inser_values([45,5,3,12,567,99])
    print(l1.print_list())
    print(l1.max_no())
    l1.remove_at(0)

    (l1.insert_at(4,77))
    print(l1.print_list())'''




from types import new_class


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")
 
 
if __name__ == '__main__':
 
    e = Node(5, None)   # last node
    d = Node(4, e)
    c = Node(3, d)
    b = Node(2, c)
    a = Node(1, b)      # first node
 
    head = a
    printList(head)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def print_(head):
    itr=head
    while itr:
        print(itr.data,end='--')
        itr=itr.next
    print()
def len_(head,c=0):
    if head is None:
        return None
    itr=head
    while itr:
        c+=1
        itr=itr.next
    return c
def copy_(head):
    if head is None:
        print('nothig is there in your linked list')
    itr=head
    newnode=None
    tail=None
    while itr:
        if newnode is None:
            newnode=Node(itr.data,tail)
            tail=newnode
        else:
            tail.next=Node(itr.data,tail.next)
            tail=tail.next
        itr=itr.next
    return newnode
def delete_(head,index,c=0):
    if head is None:
        print("nothing is there in your linked list")
    if index==0:
        head=head.next
    itr=head
    
    while itr:
        if index-1==c:
            itr.next=itr.next.next
        itr=itr.next
        c+=1
def pop_(head,v=0):
    if head is None:
        return None
    itr=head
    z=len_(head)
    while itr and v<z-1 :
        itr=itr.next
        v+=1
    itr.next=None
    return head
def insert_sort(head,value):
    nownode=Node(value)
    if head is None or head.data>=nownode.data:
        nownode.next=head
        head=nownode
        return head
    itr=head
    while itr.next and itr.next.data<nownode.data:
        itr=itr.next
    nownode.next=itr.next
    itr.next=nownode
    return head
def get_elem(head,res):
    itr=head
    while itr:
        res.append(itr.data)
        itr=itr.next
    return res
def sortedinsert(head,newnode):
    dummy=Node()
    current=dummy
    dummy.next=head
    while current.next and current.next.data<newnode.data:
        current=current.next
    newnode.next=current.next
    current.next=newnode
    return dummy.next
def insetsore(head):
    result=None
    Current=head
    while Current:
        next=Current.next
        result=sortedinsert(result,Current)
        Current=next
    return result
def frontback(source):
    length=len_(source)
    if length<2:
        front=source
        back=None
        return front,back
    current=source
    for i in range((length-1)//2):
        current=current.next
    front=source
    back=current.next
    current.next=None
    return front,back
def removedu(head):
    if head is None:
        return None
    itr=head
    while itr.next:
        if itr.data==itr.next.data:
            nxtnxt=itr.next.next
            itr.next=nxtnxt
        else:
            itr=itr.next
    return head
def addingfrontnode(first,second):
    if first is None:
        return 'your first is none'
    if second is None: 
        return 'your second is none'
    v=second
    second=second.next
    v.next=first
    first=v
    return first
def moving_even_last(head):
    if head is None:
        return None
    itr=head
    evennode=oddnode=None
    while itr:
        if itr.data%2==0:
            evennode=Node(itr.data,evennode)
        else:
            oddnode=Node(itr.data,oddnode)
        itr=itr.next
    nn=oddnode
    while nn.next:
        nn=nn.next
    nn.next=evennode
    head=oddnode
    return head
 
if __name__ == '__main__':
 
    A = [1,2,3,4,5,8,10,11,48]
 
    node = [None] * len(A)
 
    for i in range(len(A)):
        node[i] = Node(A[i], None)
        if i > 0:
            node[i - 1].next = node[i]

 
    head = node[0]
    print_(head)
    '''print_(head)
    res=[]
    res=sorted(get_elem(head,[]))
    print(res)
    for i in range(len(res)):
        node[i]=Node(res[i],None)
        if i>0:
            node[i-1].next=node[i]
    nnn=node[0]
    nnn=insert_sort(nnn,4)
    print_(nnn)
    print_(head)
    bb=None
    for i in reversed(range(len(A))):
       bb=Node(A[i],bb) 
    bb=insetsore(bb)
    print_(bb)
    first,second=frontback(head)
    print_(first)
    print_(second)
    head=removedu(head)
    print_(head)
    first=addingfrontnode(first,second)
    print_(first)'''
    head=moving_even_last(head)
    print_(head)
    