import json

dict1 = {"cost":"HIGH", "type":["Mobile", "SmartPhone"], "values":[["Android", 250]]}
dict2 = {"cost":"HIGH", "type":["Mobile", "SmartPhone"], "values":[["iPhone",  450]]}

def combine(dict1, dict2):
    if dict1['cost'] == dict2['cost'] and dict1['type'] == dict2['type']:
        return {
            'cost': dict1['cost'],
            'type': dict1['type'],
            'values': dict1['values'] + dict2['values']
        }

result1 = combine(dict1, dict2)
result2 = json.dumps(combine(dict1, dict2))

print('dict1["cost"]:',dict1["cost"])
print('dict1["type"]:',dict1["type"])
print('dict1["values"]:',dict1["values"])
print()
print('dict2["cost"]:',dict2["cost"])
print('dict2["type"]:',dict2["type"])
print('dict2["values"]:',dict2["values"])
print()
print('result1["cost"]:',result1["cost"])
print('result1["type"]:',result1["type"])
print('result1["values"]:',result1["values"])
print()
print('result2:',result2)

