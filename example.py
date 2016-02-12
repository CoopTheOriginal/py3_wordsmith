from py3_wordsmith import Wordsmith

# create Wordsmith object with API version and key
word_obj = Wordsmith('0.1', 'api_key')

# Generate list of projects to choose from
word_obj.getProjects()

# Generate list of templates to choose from
word_obj.getTemplates('Real Estate')

# Generate data schema for a project
word_obj.getDataSchema('Real Estate')

# Generate narratives. Pass project name, project template, and list of data dicts
# you'd like to run narratives for
print(word_obj.generateNarratives("Real Estate", "Real Estate Sample Narrative", [{'price_per_sq_ft' : 1,
'middle_school': 'Text', 'middle_rating_numeric': 1, 'heating_source': 'Text', 'high_rating_numeric': 1,
'avg_price_per_sq_ft': 1, 'lot_size_sq_ft': 1, 'bedrooms': 1, 'elementary_rating': 'Text', 'middle_rating': 'Text',
'roof_type': 'Text', 'elementary_school': 'Text', 'flooring': [1,2,3,4], 'address_city': 'Text', 'zpid': 1,
'elementary_rating_numeric': 1, 'price_per_sq_ft': 1, 'num_floors': 1, 'lot_size_acre': 1, 'call_address': 'Text',
'parking_type': 'Text', 'address_street': 'Text', 'basement': 'Text', 'address_state': 'Text',
'last_sold_date': 'Text', 'id': 1, 'high_rating': 'Text', 'bathrooms': 1, 'year_built': 1987, 'neighborhood': 'Text',
'sale_price': 120, 'house_style': 'Text', 'finished_sq_ft': 33, 'high_school': 'Text'}]))
