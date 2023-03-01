from abc import ABC, abstractmethod

class AbstractHeap(ABC):
    
    @abstractmethod
    def insert(self,elem: str)->None:
        """ Insert element elem into the heap"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Prints the heap"""
        pass

    @abstractmethod
    def extract_min(self) -> str:
        """Deletes minimal element from heap and returns it"""

# Implement methods __init__, insert, __str__ and _heap_up
class Heap(AbstractHeap):
    def __init__(self) -> None:
        self.heap = ['Kuk!']

    def insert(self, elem: str) -> None:
        self.heap.append(elem)
        self._heap_up()

    def extract_min(self) -> str:
        if len(self.heap) == 1:
            raise IndexError("Heap empty")
        amin = self.heap[1]
        # Swap root and the last element of the heap
        self.heap[1] = self.heap[-1]
	    # Deletes last element from the heap
        self.heap.pop()
	    # Bubbles down and repairs heap requirement
        self._heap_down()
	    # Returns the deleted element
        return amin

    def __str__(self):
#        return str(self.heap)
        outstr = ""
        exp = 1
        for idx,item in enumerate(self.heap):
            if idx == 0:
                continue
            outstr += str(item)+" "
            if idx+1 == 2**exp:
                outstr +="\n"
                exp += 1
        return outstr

    def _heap_down(self):
        """Takes the root of the heap and checks and 
           repairs the heap requirement""" 
        if len(self.heap) == 1:
            return
        curIdx = 1
        # while we are not out of the heap
        while curIdx*2 < len(self.heap):
            # We have only one child -> we will compare with it
            if curIdx*2 == len(self.heap)-1:
                minIdx = curIdx*2
            # we have two children -> select the lesser one
            elif self.heap[curIdx*2] < self.heap[curIdx*2+1]:
                minIdx = curIdx*2
            else:
                minIdx = curIdx*2+1
            
            # If we are greater than the lesser child
            if self.heap[curIdx] > self.heap[minIdx]:
                # swap
                self.heap[curIdx], self.heap[minIdx] = self.heap[minIdx], self.heap[curIdx]
                # Move to the child
                curIdx = minIdx
            else:
                # Heap is ok, nothing to do
                return 
        
                
    def is_empty(self):
        return len(self.heap) == 1
    
    def _heap_up(self):
        """ Takes the last inserted element and 
    	checks the heap requirement"""
        cur_idx = len(self.heap)-1
        parent_idx = cur_idx//2
        # While we are not in the root
        while parent_idx > 0:
            # If the parent is greater than us
            if self.heap[parent_idx] > self.heap[cur_idx]:
                # Swap
                self.heap[cur_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[cur_idx]
                # Move to the parent
                cur_idx//=2
                parent_idx//=2
            else:
                # Nothing to do -> return
                return
                
my_heap = Heap()

for i in reversed('abcdefghij'):
    my_heap.insert(i)

print(my_heap)
str(my_heap)

while not my_heap.is_empty():
    print(my_heap.extract_min())