import unittest
from models import movies
Movie = movie.Movie


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
    '''
    set up method that will run before every Test
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ =='__main__':
    unittest.main()    