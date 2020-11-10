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
        self.assertIsNotNone(main.solve_with_file("boards/grid5_1.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid5_2.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid5_1_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid5_1.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n5 2>1 3 4"
                                                 "\n. . . . ."
                                                 "\n3 5 2 4 1"
                                                 "\n. . . v ."
                                                 "\n4 1<3 2 5"
                                                 "\n. . . . ."
                                                 "\n1 3 4 5 2"
                                                 "\n^ ^ . . ."
                                                 "\n2 4<5 1 3"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid7(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid7.txt"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid7_solvable_solution(self, mock_stdout):
        main.solve_with_file("boards/grid7.txt")
        self.assertEqual(mock_stdout.getvalue(), "---------------SOLUTION----------------"
                                                 "\n5>4>1<2<7 3 6"
                                                 "\n. . . . . . v"
                                                 "\n1 7 6>4>2<5 3"
                                                 "\n. v . ^ . . ."
                                                 "\n4 3 5 6 1<2 7"
                                                 "\nv v ^ . . . v"
                                                 "\n3>2 7 5 6 4 1"
                                                 "\n. . . . . . ."
                                                 "\n7>6 2 3 5 1 4"
                                                 "\n. . . . . . ^"
                                                 "\n2 1 3 7 4 6>5"
                                                 "\n. . ^ v . ^ ."
                                                 "\n6>5>4 1 3 7 2"
                                                 "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid9(self, mock_stdout):
        self.assertIsNotNone(main.solve_with_file("boards/grid9.txt"))
