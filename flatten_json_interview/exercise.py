import managealooma.transformation_functions as transforms
from inputs import bread_production

# EXERCISE
# Jay's bakery has a production schedule by day. This data is stored in the JSON data below.
# We'd like to flatten this data in a variety of ways so we can put this data into Snowflake
# Please write a function called flatten that will let us flatten the JSON to a variety of levels.
# Please also clean the data in the following ways:
# *All numbers should be integers.  Make a decision and explain the justification if you need to adjust the data.
# *Empty strings should be None.
# *Keys should all be lowercase

# MECHANICS
# - You can add as many helper functions or classes as you see necessary, that will be called by your solution function.
# - Make sure to structure your solution in a way that it can be tested using the unit testing/mocking libraries available in the Coderpad environment. For details see the available libraries for each runtime environment available at Coderpad[5].
# - If there is no time for writing the tests, keep notes of the discrete scenarios that you would check during testing.

bread_production = [
	{"production_date": "2022-03-01",
	 "sourdough":
		 {"baguettes":
			  {"sourdough": 15,
			   "sourdough demi": 25, },
		  "rye":
			  {"caraway rye": 33.0,
			   "plain rye": 22},
		  "SOURDOUGH": {"cheddar black pepper": 15.0,
		                "cranberry walnut": 10,
		                "classic": {"boule": 12,
		                            "batard": None, }
		                }
		  },
	 "yeasted": {"white": 10,
	             "Honey Whole Wheat Hamburger Buns": 80,
	             "baguettes": {"french": 20,
	                           "french demi": 30},
	             },
	 },
	{"production_date": "2022-03-02 12:33:00",
	 "sourdough":
		 {"baguettes":
			  {"sourdough": 14,
			   "sourdough demi": 24, },
		  "rye":
			  {"caraway rye": 33.0,
			   "plain rye": 22},
		  "SOURDOUGH": {"cheddar black pepper": 15.0,
		                "cranberry walnut": 10,
		                "classic": {"boule": 12,
		                            "batard": None, }
		                },
		  },
	 "yeasted": {"white": 10,
	             "Honey Whole Wheat Hamburger Buns": None,
	             "baguettes": {"french": None,
	                           "french demi": "    "},
	             },
	 },
]


def flatten(my_input, levels):

	output_list = []
	for item in my_input:
		new_dict = transforms.flatten_json(item, ['sourdough', 'yeasted'], levels)
		output_list.append(new_dict)

	return output_list

import unittest


# Tests - you don't need to change this section but feel free to add more tests if you want
class BakeryTests(unittest.TestCase):

	def setUp(self):
		self.data = [
	{"production_date": "2022-03-01",
	 "sourdough":
		 {"baguettes":
			  {"sourdough": 15,
			   "sourdough demi": 25, },
		  "rye":
			  {"caraway rye": 33.0,
			   "plain rye": 22},
		  "SOURDOUGH": {"cheddar black pepper": 15.0,
		                "cranberry walnut": 10,
		                "classic": {"boule": 12,
		                            "batard": None, }
		                }
		  },
	 "yeasted": {"white": 10,
	             "Honey Whole Wheat Hamburger Buns": 80,
	             "baguettes": {"french": 20,
	                           "french demi": 30},
	             },
	 },
	{"production_date": "2022-03-02 12:33:00",
	 "sourdough":
		 {"baguettes":
			  {"sourdough": 14,
			   "sourdough demi": 24, },
		  "rye":
			  {"caraway rye": 33.0,
			   "plain rye": 22},
		  "SOURDOUGH": {"cheddar black pepper": 15.0,
		                "cranberry walnut": 10,
		                "classic": {"boule": 12,
		                            "batard": None, }
		                },
		  },
	 "yeasted": {"white": 10,
	             "Honey Whole Wheat Hamburger Buns": None,
	             "baguettes": {"french": None,
	                           "french demi": "    "},
	             },
	 },
]

	def test_case_1(self):


		expected_output = [{   'production_date': '2022-03-01',
			    'sourdough_baguettes': {'sourdough': 15, 'sourdough demi': 25},
			    'sourdough_rye': {'caraway rye': 33.0, 'plain rye': 22},
			    'sourdough_sourdough': {   'cheddar black pepper': 15.0,
			                               'classic': {'batard': None, 'boule': 12},
			                               'cranberry walnut': 10},
			    'yeasted_baguettes': {'french': 20, 'french demi': 30},
			    'yeasted_honey whole wheat hamburger buns': 80,
			    'yeasted_white': 10},
			{   'production_date': '2022-03-02 12:33:00',
			    'sourdough_baguettes': {'sourdough': 14, 'sourdough demi': 24},
			    'sourdough_rye': {'caraway rye': 33.0, 'plain rye': 22},
			    'sourdough_sourdough': {   'cheddar black pepper': 15.0,
			                               'classic': {'batard': None, 'boule': 12},
			                               'cranberry walnut': 10},
			    'yeasted_baguettes': {'french': None, 'french demi': '    '},
			    'yeasted_honey whole wheat hamburger buns': None,
			    'yeasted_white': 10}]

		self.assertEqual(flatten(self.data, 1), expected_output)

	def test_case_2(self):
		expected_output = [{'production_date': '2022-03-01',
						    'sourdough_baguettes_sourdough': 15,
						    'sourdough_baguettes_sourdough demi': 25,
						    'sourdough_rye_caraway rye': 33.0,
						    'sourdough_rye_plain rye': 22,
						    'sourdough_sourdough_cheddar black pepper': 15.0,
						    'sourdough_sourdough_classic': {'batard': None, 'boule': 12},
						    'sourdough_sourdough_cranberry walnut': 10,
						    'yeasted_baguettes_french': 20,
						    'yeasted_baguettes_french demi': 30,
						    'yeasted_honey whole wheat hamburger buns': 80,
						    'yeasted_white': 10},
						{'production_date': '2022-03-02 12:33:00',
						    'sourdough_baguettes_sourdough': 14,
						    'sourdough_baguettes_sourdough demi': 24,
						    'sourdough_rye_caraway rye': 33.0,
						    'sourdough_rye_plain rye': 22,
						    'sourdough_sourdough_cheddar black pepper': 15.0,
						    'sourdough_sourdough_classic': {'batard': None, 'boule': 12},
						    'sourdough_sourdough_cranberry walnut': 10,
						    'yeasted_baguettes_french': None,
						    'yeasted_baguettes_french demi': '    ',
						    'yeasted_honey whole wheat hamburger buns': None,
						    'yeasted_white': 10}]
		self.assertEqual(flatten(self.data, 2), expected_output)

	def test_case_3(self):
		expected_output = [{   'production_date': '2022-03-01',
	    'sourdough_baguettes_sourdough': 15,
	    'sourdough_baguettes_sourdough demi': 25,
	    'sourdough_rye_caraway rye': 33.0,
	    'sourdough_rye_plain rye': 22,
	    'sourdough_sourdough_cheddar black pepper': 15.0,
	    'sourdough_sourdough_classic_batard': None,
	    'sourdough_sourdough_classic_boule': 12,
	    'sourdough_sourdough_cranberry walnut': 10,
	    'yeasted_baguettes_french': 20,
	    'yeasted_baguettes_french demi': 30,
	    'yeasted_honey whole wheat hamburger buns': 80,
	    'yeasted_white': 10},
		{   'production_date': '2022-03-02 12:33:00',
		    'sourdough_baguettes_sourdough': 14,
		    'sourdough_baguettes_sourdough demi': 24,
		    'sourdough_rye_caraway rye': 33.0,
		    'sourdough_rye_plain rye': 22,
		    'sourdough_sourdough_cheddar black pepper': 15.0,
		    'sourdough_sourdough_classic_batard': None,
		    'sourdough_sourdough_classic_boule': 12,
		    'sourdough_sourdough_cranberry walnut': 10,
		    'yeasted_baguettes_french': None,
		    'yeasted_baguettes_french demi': '    ',
		    'yeasted_honey whole wheat hamburger buns': None,
		    'yeasted_white': 10}]
		self.assertEqual(flatten(self.data, 3), expected_output)
