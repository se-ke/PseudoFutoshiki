from unittest.mock import patch
from io import StringIO
import unittest
import main


class TestSolvablity(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid1_solvable(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid1.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid1_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid1.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n1"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_solvable(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid2_2ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_2ineq2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_2val.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_4ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_base.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_down.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_left.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_right.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_up.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_val.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_2ineq_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid2_2ineq.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2 1"
                                                 "\nv ^"
                                                 "\n1 2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_4ineq_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid2_4ineq.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2>1"
                                                 "\nv ^"
                                                 "\n1<2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_val_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid2_val.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2 1"
                                                 "\n. ."
                                                 "\n1 2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_2val_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid2_2val.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n1 2"
                                                 "\n. ."
                                                 "\n2 1"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid2_unsolvable(self, mock_stdout):
        self.assertIsNone(main.solve_with_file("boards/grid2_2ineq_fail.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_ineq_val_fail1.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_ineq_val_fail2.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_val_fail.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_solvable(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid3_3ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val_3ineq2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_base.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_2ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val1.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val_3ineq1.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val_4ineq.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_base_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid3_val1.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2 3 1"
                                                 "\n. . ."
                                                 "\n1 2 3"
                                                 "\n. . ."
                                                 "\n3 1 2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_3ineq_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid3_3ineq.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n1 2<3"
                                                 "\n^ . ."
                                                 "\n2 3 1"
                                                 "\n^ . ."
                                                 "\n3 1 2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_val2_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid3_val2.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2 3 1"
                                                 "\n. . ."
                                                 "\n3 1 2"
                                                 "\n. . ."
                                                 "\n1 2 3"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_val_4ineq_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid3_val_4ineq.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n2 3>1"
                                                 "\n. . ^"
                                                 "\n3 1 2"
                                                 "\n. ^ ."
                                                 "\n1 2<3"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid3_unsolvable(self, mock_stdout):
        self.assertIsNone(main.solve_with_file("boards/grid3_val_2ineq_fail1.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid3_val_fail.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid5(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid5.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid9(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid9.txt"))
