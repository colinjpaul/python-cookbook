# Sort a list of a dicts on a common key

test_data = [
    {"@type": "CatalogResource", "id": "a9777677-3cdf-4fc4-a8c1-bec814e9aede", "name": "Configure and Install McAfee Enterprise"},
    {"@type": "CatalogResource", "id": "78fd65db-d5aa-446f-8547-3dc6db90859c", "name": "Configure VM Product ID Activation"},
    {"@type": "CatalogResource", "id": "62dbbdf7-a323-4c03-9ee6-8590f328a9cf", "name": "CLDLVQAEP0564"},
]

result = next((item for item in test_data if item['name'] == "CLDLVQAEP0564"), None)
vm_id = result.get('id')
print(vm_id)














