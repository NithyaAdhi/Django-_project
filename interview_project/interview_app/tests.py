

import unittest
from interview_project.settings import BASE_DIR
from interview_app.models import School, Class
class SchoolModelTest(unittest.TestCase):
    def setUp(self):
        self.school = School.objects.create(name='Test School')

    def test_school_name(self):
        self.assertEqual(self.school.name, 'Test School')

class ClassModelTest(unittest.TestCase):
    def setUp(self):
        self.school = School.objects.create(name='Test School')
        self.class_name = 'Test Class'
        self.class_obj = Class.objects.create(name=self.class_name, school=self.school)

    def test_class_name(self):
        self.assertEqual(self.class_obj.name, self.class_name)

    def test_class_school(self):
        self.assertEqual(self.class_obj.school, self.school)

if __name__ == '__main__':
    unittest.main()
