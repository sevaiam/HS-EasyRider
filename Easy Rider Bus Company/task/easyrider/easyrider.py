# Write your code here
import json
from datetime import datetime


data_types = {"bus_id": (int, True, 0, 0),
              "stop_id": (int, True, 0, 0),
              "stop_name": (str, True, 0, r'^([A-Z]\w+ )+(Road|Avenue|Boulevard|Street)$'),
              "next_stop": (int, True, 0, 0),
              "stop_type": (str, False, 1, r'^[S|O|F]$'),
              "a_time": (str, True, 0, r'^([0-2][\d]):([0-5][0-9])$')}

inp_json = input()
json_list = json.loads(inp_json)

forbidden_stops = set()
wrong_stops = set()
transfer_stops = {}
for i in json_list:
    transfer_stops.setdefault(i['stop_name'], 0)
    transfer_stops[i['stop_name']] += 1
    if i['stop_type'] == 'S' or i['stop_type'] == 'F':
        forbidden_stops.add(i['stop_name'])
for k, v in transfer_stops.items():
    if v > 1:
        forbidden_stops.add(k)
for i in json_list:
    stop = i['stop_type']
    if stop == 'O' and i['stop_name'] in forbidden_stops:
        wrong_stops.add(i['stop_name'])



print('On demand stops test:')
print(forbidden_stops)
print(wrong_stops)

if not wrong_stops:
    print('OK')
else:
    print(f'Wrong stop type: {sorted(list(wrong_stops))}')

# all_stops_dic = {}
# lines_dic = {}

# transfer_dic = {}
# correct_stops = True
#  task 1
# for i in json_list:
#     for k, v in data_types.items():
#         error_dic.setdefault(k, 0)
#         if not isinstance(i[k], v[0]):
#             error_dic[k] += 1
#         elif v[1] and i[k] == '':
#             error_dic[k] += 1
#         elif v[2] and len(i[k]) > v[2]:
#             error_dic[k] += 1

# #  task 2
# for i in json_list:
#     for k, v in data_types.items():
#         if v[-1]:
#             error_dic.setdefault(k, 0)
#             match = re.match(v[3], i[k])
#             if match is None and i[k]:
#                 error_dic[k] += 1
#
# for i in json_list:
#     key = i['bus_id']
#     lines_dic.setdefault(key, [])
#     all_stops_dic.setdefault(key, set())
#     transfer_dic.setdefault(i['stop_name'], 0)
#     transfer_dic[i['stop_name']] += 1
#     lines_dic[key].append(i['stop_type'])
#     all_stops_dic[key].add(i['stop_name'])
#     if i['stop_type'] == 'S':
#         start_stops.add(i['stop_name'])
#     elif i['stop_type'] == 'F':
#         end_stops.add(i['stop_name'])
#
#
#
# for x, y in lines_dic.items():
#     if y.count('S') != 1 or y.count('F') != 1:
#         print(f'There is no start or end stop for the line: {x}')
#         correct_stops = False
#         break
#
# for a, b in transfer_dic.items():
#     if b > 1:
#         transfer_stops.add(a)
#
#
# print(f'Start stops: {len(start_stops)} {sorted(list(start_stops))}')
# print(f'Transfer stops: {len(transfer_stops)} {sorted(list(transfer_stops))}')
# print(f'Finish stops: {len(end_stops)} {sorted(list(end_stops))}')



    #  lines_dic[i['bus_id']].append(i['stop_id'])

# print(f'Type and required field validation: {sum(i for i in error_dic.values())} errors')
# print(f'Format validation: {sum(i for i in error_dic.values())} errors')
# print('Line names and number of stops:')
# for k, v in lines_dic.items():
#     print(f'bus_id : {k}, stops: {len(v)}')
