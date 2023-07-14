# import re
# from process_arrange.settings import IP_NET, SERVER_IP_LIST
# from app.function import t_public_error_code
# import requests
#
# ip = ''
# try:
#     res = requests.get(IP_NET, timeout=5).text
#     ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
#     ip = ip[0] if ip else ''
#     print("this ip is ======>" + ip)
#     ip_list = SERVER_IP_LIST
#     if ip in ip_list:
#         t_public_error_code.check_error_code_status()
# except Exception as e:
#     print(str(e))
#     pass
