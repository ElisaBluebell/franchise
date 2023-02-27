import collections
import requests
import folium
import pandas as pd
import numpy as np
from folium.plugins import MiniMap
#
#
# # 카카오 API
# def whole_region(keyword, start_x, start_y, end_x, end_y):
#     page_num = 1
#     data_list = []
#
#     while True:
#         url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
#         params = {'query': keyword, 'page': page_num, 'rect': f'''''{start_x}, {start_y}, {end_x}, {end_y}'''}
#         headers = {'Authorization': 'KakaoAK 3e6f33dd880519c5be39333ce69e712a'}
#         resp = requests.get(url, params=params, headers=headers)
#
#         search_count = resp.json()['meta']['total_count']
#         print('총 개수', search_count)
#
#         if search_count > 45:
#             print('좌표 4등분')
#             dividing_x = (start_x + end_x) / 2
#             dividing_y = (start_y + end_y) / 2
#
#             data_list.extend(whole_region(keyword, start_x, start_y, dividing_x, dividing_y))
#             data_list.extend(whole_region(keyword, dividing_x, start_y, end_x, dividing_y))
#             data_list.extend(whole_region(keyword, start_x, dividing_y, dividing_x, end_y))
#             data_list.extend(whole_region(keyword, dividing_x, dividing_y, end_x, end_y))
#             return data_list
#
#         else:
#             if resp.json()['meta']['is_end']:
#                 data_list.extend(resp.json()['documents'])
#                 return data_list
#
#             else:
#                 print('다음페이지')
#                 page_num += 1
#                 data_list.extend(resp.json()['documents'])
#
#
# def overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y):
#     # 최종 데이터가 담길 리스트
#     overlapped_result = []
#
#     # 지도를 사각형으로 나누면서 받아옴
#     for i in range(1, num_x + 1):
#         end_x = start_x + next_x
#         initial_start_y = start_y
#         for j in range(1, num_y + 1):
#             end_y = initial_start_y + next_y
#             each_result = whole_region(keyword, start_x, initial_start_y, end_x, end_y)
#             overlapped_result.extend(each_result)
#             initial_start_y = end_y
#         start_x = end_x
#
#     return overlapped_result
#
#
# keyword = '카페'
# start_x = 126.14
# start_y = 33.11
# next_x = 0.01
# next_y = 0.01
# num_x = 92
# num_y = 58
#
# overlapped_result = overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y)
#
# results = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.teims())) for d in overlapped_result)))
# X = []
# Y = []
# stores = []
# road_address = []
# place_url = []
# ID = []
# for place in results:
#
#     X.append(float(place['x']))
#     Y.append(float(place['y']))
#     stores.append(place['place_name'])
#     road_address.append(place['road_address_name'])
#     place_url.append(place['place_url'])
#     ID.append(place['id'])
#
#     ar = np.array([ID, stores, X, Y, road_address, place_url]).T
#     df = pd.DataFrame(ar, columns = ['ID', 'stores', 'X', 'Y', 'road_address', 'place_url'])
#
#     print('total_result_number = ', len(df))
#     print(results)
#
#
#
#

##카카오 API
def whole_region(keyword, start_x, start_y, end_x, end_y):
    # print(start_x,start_y,end_x,end_y)
    page_num = 1
    # 데이터가 담길 리스트
    all_data_list = []

    while True:
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        params = {'query': keyword, 'page': page_num,
                  'rect': f'{start_x},{start_y},{end_x},{end_y}'}
        headers = {'Authorization': 'KakaoAK 3e6f33dd880519c5be39333ce69e712a'}
        ## 입력예시 -->> headers = {'Authorization': 'KakaoAK f64acbasdfasdfasf70e4f52f737760657'}
        resp = requests.get(url, params=params, headers=headers)

        search_count = resp.json()['meta']['total_count']
        print('총 개수', search_count)

        if search_count > 45:
            print('좌표 4등분')
            dividing_x = (start_x + end_x) / 2
            dividing_y = (start_y + end_y) / 2
            ## 4등분 중 왼쪽 아래
            all_data_list.extend(whole_region(keyword, start_x, start_y, dividing_x, dividing_y))
            ## 4등분 중 오른쪽 아래
            all_data_list.extend(whole_region(keyword, dividing_x, start_y, end_x, dividing_y))
            ## 4등분 중 왼쪽 위
            all_data_list.extend(whole_region(keyword, start_x, dividing_y, dividing_x, end_y))
            ## 4등분 중 오른쪽 위
            all_data_list.extend(whole_region(keyword, dividing_x, dividing_y, end_x, end_y))
            return all_data_list

        else:
            if resp.json()['meta']['is_end']:
                all_data_list.extend(resp.json()['documents'])
                return all_data_list
            # 아니면 다음 페이지로 넘어가서 데이터 저장
            else:
                print('다음페이지')
                page_num += 1
                all_data_list.extend(resp.json()['documents'])


def overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y):
    # 최종 데이터가 담길 리스트
    overlapped_result = []

    # 지도를 사각형으로 나누면서 데이터 받아옴
    for i in range(1, num_x + 1):  ## 1,10
        end_x = start_x + next_x
        initial_start_y = start_y
        for j in range(1, num_y + 1):  ## 1,6
            end_y = initial_start_y + next_y
            each_result = whole_region(keyword, start_x, initial_start_y, end_x, end_y)
            overlapped_result.extend(each_result)
            initial_start_y = end_y
        start_x = end_x

    return overlapped_result

# 시작 x 좌표 및 증가값
keyword = '카페'
start_x = 126.64
start_y = 33.61
next_x = 0.01
next_y = 0.01
num_x = 92
num_y = 58

overlapped_result = overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y)

# 최종 데이터가 담긴 리스트 중복값 제거
results = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in overlapped_result)))
X = []
Y = []
stores = []
road_address = []
place_url = []
ID = []
for place in results:
    X.append(float(place['x']))
    Y.append(float(place['y']))
    stores.append(place['place_name'])
    road_address.append(place['road_address_name'])
    place_url.append(place['place_url'])
    ID.append(place['id'])

    ar = np.array([ID, stores, X, Y, road_address, place_url]).T
    df = pd.DataFrame(ar, columns=['ID', 'stores', 'X', 'Y', 'road_address', 'place_url'])

print(results)
