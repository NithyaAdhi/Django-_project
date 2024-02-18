from django.test import TestCase
from interview_app.models import School  # Replace 'myapp' with the name of your Django app
from interview_app.models import import_data_from_csv  # Replace 'myapp' with the name of your Django app

class ImportDataFromCsvTestCase(TestCase):
    def test_import_data_from_csv(self):
        # Run the import function
        import_data_from_csv()
        
        # Check if data was imported correctly
        # For example, you could check if a School object was created
        self.assertTrue(School.objects.exists())
