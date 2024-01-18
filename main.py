from ISE_api_func import Endpoint_id, Endpoint_MAC

MAC = Endpoint_MAC('FF0000000000')
id = MAC.get_id()
print(id)
delete = MAC.delete()
