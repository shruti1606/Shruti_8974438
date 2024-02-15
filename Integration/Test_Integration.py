import unittest
from Student import Student
class TestStudentManagerIntegration(unittest.TestCase):
    def setUp(self):
        self.manager = Student()



    def test_add_update_student(self):
        self.manager.add_student(1, 'Alice', 'A')
        self.manager.update_student(1, name='Alicia', grade='A+')
        self.assertEqual(self.manager.students[1]['name'], 'Alicia')
        self.assertEqual(self.manager.students[1]['grade'], 'A+')

    def test_delete_student(self):
        self.manager.add_student(1, 'Alice', 'A')
        self.manager.add_student(2, 'Bob', 'B')
        self.manager.delete_student(1)
        self.assertIs(1, self.manager.students)



if __name__ == '__main__':
    unittest.main()
