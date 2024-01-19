import pandas as pd , re
MAC = pd.read_excel('endpoint_mac.xlsx')
MAC_list = MAC['無線網卡MAC'].tolist()


pattern = re.compile(r'-')
MAC_list = [pattern.sub('', sub) for sub in MAC_list]

