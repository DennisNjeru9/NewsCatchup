import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    
    def setUp(self):

        self.new_source = Source('bloomberg','bloomberg','Delivers business and market news,data','http://www.bloomberg.com','en','us')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    
    def test_init(self):
        self.assertEqual(self.new_source.id,"bloomberg")
        self.assertEqual(self.new_source.name,"bloomberg")
        self.assertEqual(self.new_source.description,"Delivers business and market news,data")
        self.assertEqual(self.new_source.url,"http://www.bloomberg.com")
        self.assertEqual(self.new_source.language,"en")

