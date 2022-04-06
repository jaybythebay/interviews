import alooma
import pprint
from inputs import bread_production, sweets_production

print(bread_production)
pp = pprint.PrettyPrinter(indent=4)

for day in bread_production:
	pp.pprint(day)
	type(day)

for day in sweets_production:
	pp.pprint(day)
	type(day)