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
    def test_queen_count_is_zero_initially(self): #want to pass (passed)
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_queen_count_is_not_zero_initially(self): #want to pass (passed)
        state = QueensState(8,8)
        state.board = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(state.queen_count(),3)

    def test_board_is_equal_initially(self): #want to pass (passed)
        state = QueensState(8,8)
        self.assertEqual(state.board,[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])

    """def test_board_is_not_equal_initially(self): #don't want to pass(doesn't pass)
        state = QueensState(8,8)
        self.assertEqual(state.board,[[0 for i in range(state.columns - 2)] for j in range(state.rows - 4 )])"""




if __name__ == '__main__':
    unittest.main()
