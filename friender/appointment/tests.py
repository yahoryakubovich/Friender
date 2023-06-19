from django.test import TestCase
from .utils import Queue
import unittest


class TestQueue(unittest.TestCase):
    def test_init_queue(self):
        queue = Queue("FIFO")

    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            queue = Queue("FIFA")

    def test_add_and_return_fifo_value(self):
        queue = Queue("FIFO")
        first_value = 5
        queue.add(first_value)
        value = queue.pop()
        self.assertEqual(value, first_value)

    def test_add_and_return_fifo_multivalues(self):
        queue = Queue("FIFO")
        first_value = 5
        second_value = 1
        third_value = 1
        storage = [first_value, second_value, third_value]
        for val in storage:
            queue.add(val)
            value = queue.pop()
            self.assertEqual(value, val)

    def test_add_and_return_fifo_multivalues_with_salt(self):
        queue = Queue("FIFO")
        first_value = 5
        second_value = 1
        third_value = 1
        storage = [first_value, second_value, third_value]
        for val in storage:
            queue.add(val)

        for el in range(10, 17):
            queue.add(el)

        for val in storage:
            value = queue.pop()
            self.assertEqual(value, val)

    def test_add_simple_return_fifo_multivalues(self):
        queue = Queue("FIFO")
        first_value = 1
        second_value = 5
        third_value = 1
        storage = [first_value, second_value, third_value]
        for val in storage:
            queue.add(val)

        for val in storage:
            value = queue.pop()
            self.assertEqual(value, val)

    def test_empty_queue(self):
        queue = Queue("FIFO")
        value = queue.pop()
        self.assertIs(value, None)

if __name__ == "__main__":
    unittest.main()
