# EXAMPLE 1
test_data = [
    {"@type": "CatalogResource", "id": "a9777677-3cdf-4fc4-a8c1-bec814e9aede", "name": "Configure and Install McAfee Enterprise"},
    {"@type": "CatalogResource", "id": "78fd65db-d5aa-446f-8547-3dc6db90859c", "name": "Configure VM Product ID Activation"},
    {"@type": "CatalogResource", "id": "62dbbdf7-a323-4c03-9ee6-8590f328a9cf", "name": "CLDLVQAEP0564"},
]

result = next((item for item in test_data if item['name'] == "CLDLVQAEP0564"), None)
vm_id = result.get('id')
print(vm_id)


# Example 2:        Remove \xef\xbb\xbf when reading in a csv file
#                   This returns a string
#                   Convert to a dict

fp = open("config_matrix.csv")
data = fp.read().decode("utf-8-sig").encode("utf-8")
data_list = data.split()



#Example 3

s = '#one cat #two dogs #three birds'
out = s.split()
print(type(out))
entries = dict([(x, y) for x, y in zip(out[::2], out[1::2])])
from pprint import pprint
pprint(entries)

#For each list item seperate on ',' to make a k,v pair

products = 'VSE,CLDLVQAEP0564'
out = products.split(",")

#entries = dict([(x, y) for x, y in zip(out[::2], out[1::2])])


entries = dict([(x, y) for x, y in zip(value1, out[0::2])])


print(entries)



#
# for x, y in zip('Product', out[::2])]
#
# print(products)
# print(out)


#entries = dict([x,y] for x,y in zip(out[::2]))