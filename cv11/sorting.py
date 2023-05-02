import json
import pprint as pp

with open("kont.json") as f:
    data = json.load(f)['features']

a = [3,4,7,4,5,2,7,12]

b = sorted(a,reverse=True)
print(b)
print(a)

a.sort(reverse=True)
print(a)

def get_y(f):
    return f['geometry']['coordinates'][1]

f_get_y = lambda f: f['geometry']['coordinates'][1]
print(f_get_y(data[0]))
print(get_y(data[0]))

data.sort(key=lambda f: f['geometry']['coordinates'][1])
#pp.pprint(data)

coords = list(map(lambda f: f['geometry']['coordinates'][0],data))
print(coords)

int_coords = list(map(int,coords))
print(int_coords)
