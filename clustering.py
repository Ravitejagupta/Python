a ={'cluster0': {'row_0': {'User': 'ravi', 'Issue': 'Utility', 'SubIssue': 'Gas', 'additional_info': 'bloackade', 'Phone': '+14086573319', 'latitude': '37.3422', 'longitude': '-121.8833', 'zip_code': '95112'}, 'row_1': {'User': 'abcabc', 'Issue': 'Utility', 'SubIssue': 'Telephone', 'additional_info': 'Hacked', 'Phone': '+14086573319', 'latitude': '37.3422', 'longitude': '-121.8833', 'zip_code': '95112'}, 'row_2': {'User': 'ravi', 'Issue': 'Utility', 'SubIssue': 'Telephone', 'additional_info': 'Hacked', 'Phone': '+14088194712', 'latitude': '37.3422', 'longitude': '-121.8833', 'zip_code': '95112'}}, 'cluster1': {'row_0': {'User': 'ravi', 'Issue': 'Fire', 'SubIssue': 'Hazardous Material released/spilled', 'additional_info': 'Shortage', 'Phone': '+917769988670', 'latitude': '37.2525', 'longitude': '-121.8894', 'zip_code': '95118'}, 'row_1': {'User': 'ravi', 'Issue': 'Fire', 'SubIssue': 'Hazardous Material released/spilled', 'additional_info': 'Acid', 'Phone': '+16504959189', 'latitude': '37.2525', 'longitude': '-121.8894', 'zip_code': '95118'}, 'row_2': {'User': 'ravi', 'Issue': 'Utility', 'SubIssue': 'Gas', 'additional_info': 'Leak', 'Phone': '+917769988670', 'latitude': '37.2525', 'longitude': '-121.8894', 'zip_code': '95118'}}, 'cluster2': {}}  

username = ""
issue = ""
subIssue = ""
additional_info = ""
phone = ""
# for i in range(2):
#   for j in range(len(a['cluster0'])):
#     b = 'cluster{}'.format(i)
#     c = 'row_{}'.format(j)
#     username = username +' '+ a[b][c]['User_id']
#     issue = username +' '+ a[b][c]['Issue']
#     subIssue = subIssue +' '+ a[b][c]['SubIssue']
#     additional_info = additional_info +' '+ a[b][c]['additional_info']
#     phone = phone + ' ' + +' '+ a[b][c]['phone']


k = len(a['cluster0'])    
for i in range(2):
  a['cluster{}'.format(i)]['User'] = ""
  a['cluster{}'.format(i)]['Issue'] = ""
  a['cluster{}'.format(i)]['SubIssue'] = ""
  a['cluster{}'.format(i)]['additional_info'] = ""
  for j in range(k):
    a['cluster{}'.format(i)]['User'] +=  a['cluster{}'.format(i)]['row_{}'.format(j)]['User'] + ', '
    a['cluster{}'.format(i)]['Issue'] +=  a['cluster{}'.format(i)]['row_{}'.format(j)]['Issue'] + ', '
    a['cluster{}'.format(i)]['SubIssue'] +=  a['cluster{}'.format(i)]['row_{}'.format(j)]['SubIssue'] + ', '
    a['cluster{}'.format(i)]['additional_info'] +=  a['cluster{}'.format(i)]['row_{}'.format(j)]['additional_info'] + ', '
    
print(a['cluster0']['additional_info'])

    
  
