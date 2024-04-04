# test_queens.py
#
# ICS 33 Spring 2024
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_queen_count_is_zero_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState
import unittest



class TestQueensState(unittest.TestCase):
    def test_queen_count_is_zero_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_queen_count_is_one_initially(self):
        state = QueensState(8,8)
        self.assertEqual(state.queen_count(), 1)

    def test_board_is_equal_initially(self):
        state = QueensState(8,8)
        self.assertEqual(state.board(),[[0 for i in range(state.columns)] for j in range(state.rows)])
    def test_board_is_not_equal_initially(self):
        state = QueensState(8,8)
        self.assertEqual(state.board(),[[0 for i in range(state.columns - 2)] for j in range(state.rows - 4 )])

    '''def test_queens_position(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queens(rows=8, columns=8))'''

if __name__ == '__main__':
    unittest.main()
