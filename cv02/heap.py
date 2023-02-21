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

# Implement methods __init__, insert, __str__ and _heap_up
class Heap(AbstractHeap):
    
    def _heap_up(self):
        """ Takes the last inserted element and 
    	checks the heap requirement"""
	# Take the last element
	# Check if heap requirement is valid
	# It is -> end
	# It is not -> compare with neighbor, swap smaller with the parent and repeat 
	# on the parent

my_heap = Heap()

print(my_heap)
str(my_heap)