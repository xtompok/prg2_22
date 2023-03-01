from abc import ABC, abstractmethod


class BSTMeta(ABC):
    @abstractmethod
    def search(self,num: int) -> bool:
        pass

    @abstractmethod
    def insert(self, num:int):
        pass

class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node|None = None
        self.right: Node|None = None


class BST(BSTMeta):
    def __init__(self):
        self.root: Node|None = None

    def search(self, num: int) -> bool:
	    # Root is empty -> false
        if self.root is None:
            return False
	    # Root is searched num -> true
        if self.root.val == num:
            return True
	    # search_parent
        parent = self._search_parent(num)
	    # check son
        if num < parent.val:
            if parent.left is not None:
                return True
            else:
                return False
        if num > parent.val:
            if parent.right is not None:
                return True
            else:
                return False

    def insert(self, num: int):
        if self.root is None:
            self.root = Node(num)
            return
        parent = self._search_parent(num)
        if num < parent.val:
            parent.left = Node(num)
        else:
            parent.right = Node(num)
   
    def _search_parent(self, num) -> Node:
        """Find the parent of num. Expects that searched num is not in the root node"""
	    # define current node as tree root
        cur = self.root
	    # define parent node as tree root
        parent = self.root
        while True:
	        # if current node is searched num:
            if cur.val == num:
                return parent
	        # parent node is current node
            parent = cur
	        # if num is lower than current node value:
            if num < cur.val:
	            # if left son exists:
                if cur.left is not None:
                	# current node is left son
                    cur = cur.left
                else:
	                # return current node
                    return cur
	        # if num is greater than current node value:
            else:
	            # if right son exists:
                if cur.right is not None:
	                # current node is right son
                    cur = cur.right
                else:
	                # return current node
                    return cur

mytree = BST()
mytree.insert(4)
mytree.insert(3)
mytree.insert(7)
mytree.insert(8)
print(mytree.search(4))
print(mytree.search(5))
print(mytree.search(1))
print(mytree.search(3))
print(mytree.search(9))
