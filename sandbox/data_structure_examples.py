# # EXAMPLE 1
# test_data = [
#     {"@type": "CatalogResource", "id": "a9777677-3cdf-4fc4-a8c1-bec814e9aede", "name": "Configure and Install McAfee Enterprise"},
#     {"@type": "CatalogResource", "id": "78fd65db-d5aa-446f-8547-3dc6db90859c", "name": "Configure VM Product ID Activation"},
#     {"@type": "CatalogResource", "id": "62dbbdf7-a323-4c03-9ee6-8590f328a9cf", "name": "CLDLVQAEP0564"},
# ]
#
# result = next((item for item in test_data if item['name'] == "CLDLVQAEP0564"), None)
# vm_id = result.get('id')
# #print(vm_id)
#
#
# # Example 2:        Remove \xef\xbb\xbf when reading in a csv file and convert to dict
# #                   This returns a string
# #                   Convert to a dict
#
# fp = open("config_matrix.csv")
# data = fp.read().decode("utf-8-sig").encode("utf-8")
# data_to_list = data.split()
# data_elements = [y for x in data_to_list for y in x.split()]
# entries = tuple([(x, y, z) for x, y, z in zip(data_elements[::3], data_elements[1::3], data_elements[2:3])])
#print(entries)

# Exmample 3:       Retrieve value for provider_machine_id (nested dictionary in a list)

data ={u'values': {u'entries': [{u'value': {u'type': u'string', u'value': u'CLDLVQAEP0572'}, u'key': u'provider-MachineName'}, {u'value': {u'type': u'string', u'value': u'Infrastructure.Virtual.Action.RevertSnapshot'}, u'key': u'provider-operationId'}, {u'value': {u'type': u'string', u'value': u'cb3eea06-fbfa-4452-8757-c35130cbc4ff'}, u'key': u'provider-machineId'}]}, u'layout': {u'pages': [{u'state': {u'facets': [], u'dependencies': []}, u'sections': [{u'state': {u'facets': [], u'dependencies': []}, u'rows': [{u'items': [{u'extensionRendererContext': None, u'description': u'Select an existing snapshot to restore the machine to the state it was in when the snapshot was taken.', u'dataType': {u'classId': u'Infrastructure.Compute.Machine.Snapshot', u'typeFilter': None, u'label': u'Snapshot', u'componentTypeId': u'com.vmware.csp.component.iaas.proxy.provider', u'type': u'ref', u'componentId': None}, u'labelSize': None, u'permissibleValues': None, u'label': u'Snapshot', u'state': {u'facets': [{u'type': u'readOnly', u'value': {u'type': u'constantClause', u'value': {u'type': u'boolean', u'value': False}}}, {u'type': u'internal', u'value': {u'type': u'constantClause', u'value': {u'type': u'boolean', u'value': True}}}], u'dependencies': []}, u'displayAdvice': u'TREE', u'orderIndex': None, u'detailLayout': None, u'isMultiValued': False, u'type': u'field', u'id': u'provider-SnapshotReference', u'columns': [], u'size': 4}]}], u'id': None, u'label': None}], u'id': None, u'label': u'Resource Action'}]}, u'fieldPrefixes': None}

data_2 = data.get('values')
print(data_2)

test_data = {u'entries': [{u'key': u'provider-MachineName', u'value': {u'type': u'string', u'value': u'CLDLVQAEP0572'}}, {u'key': u'provider-operationId', u'value': {u'type': u'string', u'value': u'Infrastructure.Virtual.Action.RevertSnapshot'}}, {u'key': u'provider-machineId', u'value': {u'type': u'string', u'value': u'cb3eea06-fbfa-4452-8757-c35130cbc4ff'}}]}
entries = test_data.get('entries')
result = (item for item in entries if item["key"] == "provider-machineId").next()
machine_id = result['value']['value']

print(machine_id)