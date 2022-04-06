import managealooma.transformation_functions as transforms
import pprint
from inputs import bread_production, sweets_production

print(bread_production)
pp = pprint.PrettyPrinter(indent=4)

for day in bread_production:
	type(day)
	x = transforms.flatten_json(day, ['sourdough', 'yeasted'], 2)
	pp.pprint(x)

# for day in sweets_production:
# 	pp.pprint(day)
# 	type(day)







