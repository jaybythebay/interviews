

# EXERCISE
# Jay's bakery has a production schedule by day. This data is stored in the JSON data below.
# We'd like to flatten this data in a variety of ways so we can put this data into Snowflake
# Please write a function that will let us flatten the JSON to a variety of levels.
# Please also clean the data in the following ways:
# *All numbers should be integers.  Make a decision and explain the justification if you need to adjust the data.
# *Empty strings should be None.
# *Keys should all be lowercase

# MECHANICS
# - You can add as many helper functions or classes as you see necessary, that will be called by your solution function.
# - Make sure to structure your solution in a way that it can be tested using the unit testing/mocking libraries available in the Coderpad environment. For details see the available libraries for each runtime environment available at Coderpad[5].
# - If there is no time for writing the tests, keep notes of the discrete scenarios that you would check during testing.

from inputs import bread_production

def (input, levels):
	 output = input



	return output



# Tests - you don't need to change this section but feel free to add more tests if you want

import json
import unittest



class BakeryTests(unittest.TestCase):
	def test_case_1(self):
		output = [{   'baguettes': {'french': 20, 'french demi': 30},
		    'production_date': '2022-03-01',
		    'sourdough_baguettes': {'sourdough': 15, 'sourdough demi': 25},
		    'sourdough_rye': {'caraway rye': 33.0, 'plain rye': 22},
		    'sourdough_sourdough': {   'cheddar black pepper': 15.0,
		                               'classic': {'batard': None, 'boule': 12},
		                               'cranberry walnut': 10},
		    'yeasted_honey whole wheat hamburger buns': 80,
		    'yeasted_white': 10}
		{   'baguettes': {'french': None, 'french demi': '    '},
		    'production_date': '2022-03-02 12:33:00',
		    'sourdough_baguettes': {'sourdough': 14, 'sourdough demi': 24},
		    'sourdough_rye': {'caraway rye': 33.0, 'plain rye': 22},
		    'sourdough_sourdough': {   'cheddar black pepper': 15.0,
		                               'classic': {'batard': None, 'boule': 12},
		                               'cranberry walnut': 10},
		    'yeasted_honey whole wheat hamburger buns': None,
		    'yeasted_white': 10}]
		self.assertEqual()
