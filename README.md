py3_wordsmith
=========

### About

**API for Wordsmith**

* Allows user to create narratives by passing data through the API.
* You can also pull down project lists, template lists, and data types


**Installation**

```pip install py3_wordsmith```

**Requirements**
* Written for Python 3.3+
* Requires a Wordsmith account to use.

**Parameters**
* API key
  - Can be found inside your Wordsmith account
* Version
  - Can be found in Wordsmith's API docs. Currently built using v0.1

### Request a Narrative
**See example.py**


**Returns JSON**
```[{'narrative': {'content': 'This is an awesome narrative that was generated by wordsmith! You can now go on to create amazing narratives using almost any kind of data set that you can imagine.'}, 'raw_data': {'bedrooms': 1.0, 'elementary_rating_numeric': 1.0, 'address_state': 'Text', 'basement': 'Text', 'house_style': 'Text', 'bathrooms': 1.0, 'middle_rating': 'Text', 'price_per_sq_ft': 1.0, 'lot_size_sq_ft': 1.0, 'address_street': 'Text', 'num_floors': 1.0, 'elementary_rating': 'Text', 'id': 1.0, 'parking_type': 'Text', 'flooring': '[1, 2, 3, 4]', 'middle_rating_numeric': 1.0, 'sale_price': 120.0, 'lot_size_acre': 1.0, 'elementary_school': 'Text', 'zpid': 1.0, 'heating_source': 'Text', 'call_address': 'Text', 'roof_type': 'Text', 'finished_sq_ft': 33.0, 'high_rating': 'Text', 'middle_school': 'Text', 'high_rating_numeric': 1.0, 'neighborhood': 'Text', 'year_built': 1987.0, 'last_sold_date': 'Text', 'avg_price_per_sq_ft': 1.0, 'address_city': 'Text', 'high_school': 'Text'}}]```


### Credits
* Connecting to Wordsmith heavily based off John Hegele's wrapper for Python 2