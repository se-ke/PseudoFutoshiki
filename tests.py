import unittest
import main

class TestSolvablity(unittest.TestCase):

    def test_grid1(self):
        self.assertIsNotNone(main.solve_with_file("boards/grid1.txt"))

    def test_grid2(self):
        self.assertIsNone(main.solve_with_file("boards/grid2_2ineq_fail.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_2ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_2ineq2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_4ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_base.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_down.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_left.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_right.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_ineq_up.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_ineq_val_fail1.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_ineq_val_fail2.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid2_val_fail.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid2_val.txt"))

    def test_grid3(self):
        self.assertIsNotNone(main.solve_with_file("boards/grid3_3ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val_3ineq2.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_base.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid3_val_2ineq_fail1.txt"))
        self.assertIsNone(main.solve_with_file("boards/grid3_val_fail.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_2ineq.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val1.txt"))
        self.assertIsNotNone(main.solve_with_file("boards/grid3_val_3ineq1.txt"))

    def test_grid3_test(self):
        self.assertIsNotNone(main.solve_with_file("boards/grid3_test.txt"))

    def test_grid5(self):
        self.assertIsNotNone(main.solve_with_file("boards/grid5.txt"))

    def test_grid9(self):
        self.assertIsNotNone(main.solve_with_file("boards/grid9.txt"))
