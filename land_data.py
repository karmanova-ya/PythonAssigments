import pprint

raw = [
    {'Country': 'Albania', 'Series': 'Land area (thousand hectares)', 'Value': '2740.0000'},
    {'Country': 'Albania', 'Series': 'Arable land (thousand hectares)', 'Value': '606.9000'},
    {'Country': 'Albania', 'Series': 'Permanent crops (thousand hectares)', 'Value': '84.2000'},
    {'Country': 'Albania', 'Series': 'Forest cover (thousand hectares)', 'Value': '771.5000'},
    {'Country': 'Algeria', 'Series': 'Land area (thousand hectares)', 'Value': '238174.0000'},
    {'Country': 'Algeria', 'Series': 'Arable land (thousand hectares)', 'Value': '7470.8071'},
    {'Country': 'Algeria', 'Series': 'Permanent crops (thousand hectares)', 'Value': '1012.6190'},
    {'Country': 'Algeria', 'Series': 'Forest cover (thousand hectares)', 'Value': '1956.0000'},
    {'Country': 'Aruba', 'Series': 'Land area (thousand hectares)', 'Value': '18.0000'},
    {'Country': 'Aruba', 'Series': 'Arable land (thousand hectares)', 'Value': '2.0000'},
    {'Country': 'Aruba', 'Series': 'Forest cover (thousand hectares)', 'Value': '0.4200'},
    {'Country': 'Australia', 'Series': 'Land area (thousand hectares)', 'Value': '768230.0000'},
    {'Country': 'Australia', 'Series': 'Arable land (thousand hectares)', 'Value': '26402.0000'},
    {'Country': 'Australia', 'Series': 'Permanent crops (thousand hectares)', 'Value': '340.0000'},
    {'Country': 'Australia', 'Series': 'Forest cover (thousand hectares)', 'Value': '127641.0000'}
]

## Step 1
def safe_float(s):
    try:
        return float(s)
    except:
        return 0.0


raw_float_values = []
for row in raw:
    float_row = row.copy()
    float_row['Value'] = safe_float(row['Value'])
    raw_float_values.append(float_row)

## Step 2
land_data = {}
for country in raw_float_values:
    land_name = country['Country']
    land_data[land_name] = {}

for country in raw_float_values:
    land_name = country['Country']
    key = country['Series']
    value = country['Value']
    land_data[land_name][key] = value

# pprint.pprint(land_data)
# print(land_data['Aruba']['Land area (thousand hectares)'])

## Step 3
stats = {}

for land in land_data:
    country_name = land
    series = land_data[land]
    value = land
    for line in series:
        key = series[line]
        if line in stats:
            currentStatMax = list(stats[line].keys())[0]
            if key > currentStatMax:
                stats[line] = {}
                stats[line][key] = value
        else:
            stats[line] = {}
            stats[line][key] = value

pprint.pprint(stats)

## Bonus

