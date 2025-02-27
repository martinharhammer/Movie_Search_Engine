import unittest


class StudentIDTest(unittest.TestCase):
    # Todo:
    #  Please fill in your student id to make this test is green
    def test_student_id_filled(self):
        student_id = "12221683"
        self.assertNotEqual(student_id, "")
        with open("student_id.txt", "wt") as f:
            f.write(f"{student_id}")


if __name__ == "__main__":
    unittest.main()
