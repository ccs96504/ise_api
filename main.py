from ISE_api_func import  Endpoint_MAC  , internaluser
import read_xlsx_mac_info


MAC_info = read_xlsx_mac_info.MAC_list

for i in range(5):
    internaluser_MAC = internaluser(MAC_info[i])
    internaluser_MAC.delete()
    End_Mac = Endpoint_MAC(MAC_info[i])
    delete = End_Mac.delete()
