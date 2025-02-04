import unittest
from custom_array import Array
from stack_queue import Stack, Queue
from linked import LinkedList


class TestDataStructures(unittest.TestCase):
    def test_array(self):
        arr = Array(5)
        arr.insert(0, 10)
        self.assertEqual(arr.access(0), 10)
        arr.delete(0)
        self.assertIsNone(arr.access(0))
    
    def test_stack(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())
    
    def test_queue(self):
        queue = Queue()
        queue.enqueue(20)
        self.assertEqual(queue.dequeue(), 20)
        self.assertTrue(queue.is_empty())
    
    def test_linked_list(self):
        linked_list = LinkedList()
        linked_list.insert(30)
        linked_list.insert(40)
        linked_list.delete(30)
        linked_list.traverse()

if __name__ == '__main__':
    unittest.main()
