import unittest
from app.models import Movie


class movieTest(unittest.TestCase):
    '''
    Test class to test the behavour of the Movie class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new python Series','/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))
        
