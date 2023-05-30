import folium #지도 라이브러리
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from geopy.geocoders import Nominatim #위도, 경도

####### 도로명주소 위도 경도 값으로 바꿔주기 ########
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

from scipy.spatial import Delaunay



  
    
    
from geopy.geocoders import Nominatim

def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = (geo.latitude, geo.longitude)

    return crd

## 사용방법
# three_people = ['일산역', '강남역', '광교역']
# where_is_middle_three(three_people)

## 3명만 가능!!
def where_is_middle_three(people:list):

    ##################################################################
    ########################ㅏ주소 기입란 #############################
    ##################################################################
    first = [*geocoding(people[0]), '{}'.format(people[0])]
    second = [*geocoding(people[1]), '{}'.format(people[1])]
    third = [*geocoding(people[2]),'{}'.format(people[2])]
    #################################################################
    #################################################################
    ##################################################################

    first, second, third

    #데이터넣기 : [위도, 경도, 주소]
    ##first = [37.3031, 127.0474, 'first'] #예제
    ##second = [37.3237, 127.1235, 'second'] #예제
    ##third = [37.1996, 127.0696, 'third'] #예제
    data = pd.DataFrame({'latitude' : [first[0], second[0], third[0]],
                         'longitude' : [first[1], second[1], third[1]],
                         'location' : [first[2], second[2], third[2]]})
    data_tria = pd.DataFrame({'latitude' : [first[0], second[0], third[0], first[0]],
                         'longitude' : [first[1], second[1], third[1], first[1]],
                         'location' : [first[2], second[2], third[2], first[2]]})
    lines = data_tria[['latitude', 'longitude']]
    lines
    print(data)


    ##지도의 중심잡기
    center = [data['latitude'].mean(axis = 0), data['longitude'].mean(axis = 0)]
    meeting = folium.Map(location=center, zoom_start=10)
    meeting

    ##각각 위치 표시하기
    for ii in range(len(data)):
        folium.Marker([data.iloc[ii][0],
                       data.iloc[ii][1]],
                      popup=data['location'][ii],
                      tooltip = data['location'][ii]).add_to(meeting)

    ##선따라 그리기
    folium.PolyLine(
        locations = lines,
        tooltip = 'PolyLine'
    ).add_to(meeting)


    meeting

    ##대변 찾기 : 길이가 가장 긴변이 대변
    dist_first_second = np.sqrt((data.iloc[0]['latitude'] - data.iloc[1]['latitude'])**2
                                 + (data.iloc[0]['longitude'] - data.iloc[1]['longitude'])**2)
    dist_first_third = np.sqrt((data.iloc[0]['latitude'] - data.iloc[2]['latitude'])**2
                                 + (data.iloc[0]['longitude'] - data.iloc[2]['longitude'])**2)
    dist_second_third = np.sqrt((data.iloc[1]['latitude'] - data.iloc[2]['latitude'])**2
                                 + (data.iloc[1]['longitude'] - data.iloc[2]['longitude'])**2)
    dist_list = [dist_first_second, dist_first_third, dist_second_third]
    data_distance_list = pd.DataFrame({'first_to_second' : [0], 
                                       'first_to_third' : [1],
                                       'second_to_third' : [2]})

    print('대변은 : '+ data_distance_list.T.iloc[[np.argmax(dist_list)]].index)
    # 0 : first와 second가 대변
    # 1 : first와 third가 대변
    # 2 : second과 third가 대변

    ##대변의 중앙 구하기
    middle = [(second[0] + third[0])/2, (second[1] + third[1])/2]
    center_of_gravity = [(2*middle[0] + first[0])/3, (2*middle[1] + first[1])/3]

    ##무게중심 표시하기
    folium.Circle(
        location = center_of_gravity,
        tooltip = 'center_of_gravity',
        radius = 500,
        color = 'red'
    ).add_to(meeting)
    return meeting

##########################################################
##########################################################
##n명 다 가능!!
## 사용방법
# people = ['일산역', '강남역', '광교역', '수원역']
# aa = people_middle(people)
# aa[1] : return 데이터프레임
# aa[0] : return 지도


def people_middle(people):
    ##받은 인자로 데이터프레임 만들기##
    df = pd.DataFrame(people, columns=['location'])

    latitude_li = []
    longitude_li = []

    for person in people :
        latitude, longitude = geocoding(person)
        latitude_li.append(latitude)
        longitude_li.append(longitude)
    df['latitude'] = latitude_li
    df['longitude'] = longitude_li

    ##지도의 중심 계산하기##
    center = [df['latitude'].mean(axis = 0), df['longitude'].mean(axis = 0)]
    meeting = folium.Map(location=center, zoom_start=10)


    ##각각 위치 표시하기
    for ii in range(len(df)):
        folium.Marker([df.iloc[ii]['latitude'],
                       df.iloc[ii]['longitude']],
                       popup=df['location'][ii],
                       tooltip = df['location'][ii]).add_to(meeting)

    ##각 위치들을 튜플리스트로 변환
    vertices = [(lat,long) for lat, long in df[['latitude','longitude']].values]
    vertices = pd.DataFrame(vertices)    

    ##삼각형으로 쪼개고
    ##각 삼각형의 중심의 중점
    tri = Delaunay(vertices)
    centers = []
    for indices in tri.simplices:
        # 삼각형의 꼭지점 좌표를 가져옵니다.
    #     print('indices : ', indices)
        triangle = vertices.iloc[indices]
    #     print('triangle : ', triangle)
        # 삼각형의 중심을 계산합니다.
        center = triangle.mean(axis=0)
        centers.append(center)
    center_mean = sum(centers) / len(centers)

    ## 중심 표시!!
    folium.Marker([center_mean[0],
                   center_mean[1]],
                   popup='Middel Of People',
                   tooltip = 'Middle Of People',
                   icon=folium.Icon(color='red')).add_to(meeting)
    
    return meeting, df



