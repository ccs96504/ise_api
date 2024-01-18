from ISE_api_func import  Endpoint_MAC  , internaluser

MAC = "00FF00AABBCC"


internaluser_MAC = internaluser(MAC)
internaluser_MAC.delete()
End_Mac = Endpoint_MAC(MAC)
delete = End_Mac.delete()