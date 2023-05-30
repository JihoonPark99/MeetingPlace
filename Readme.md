## 우리의 결과물

> 사람들은 흔히 약속장소를 정하기 어려워하는 상황에 처하기도 한다.
> 이번 기회에 그들을 위해서, 아싸리 각 사람의 위치를 기준으로 무게중심점에서 보는건 어떨까?
> 
> 파이썬 코드와 함께 구현을 해보자. 
> 
> 멘토링 시간에서, 함께 재미삼아 코딩을 해본다. 
<div align="center">

![image](https://github.com/JihoonPark99/NLP_study/assets/108673913/2868c13b-5598-469f-9c65-593a9a87d4d1)
  
 </div>
 
> 3명인 경우, 약속장소를 정하는게 어렵지만은 않다.
> 하지만, n명(n>=3) 인 경우는 어떨까?
>
> 방정식을 풀어야한다.  
- 방법1  ** n각형의 중심은 모든 꼭짓점을 활용하여 삼각형으로 나눈 후, 그 삼각형의 중심들의 중심을 구하면 된다.**

- 방법2  ** n각형의 중심은 모든 꼭짓점을 활용하여 모든 꼭짓점에서 거리가 같은 점 1개를 찾으면 된다. (n차방정식 근을 구하기)**

> 본 멘토링에선, 방법2를 사용하여 n명의 중심을 구한다.


> N각형을 삼각형으로 만들고, 모든 삼각형의 중심의 평균을 구하는 방법이다. 

----
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
---- 
> Dealunay라는 간단한 방정식의 근을 구하는 라이브러리를 import 해야한다.
> 이로써 n명의 주소를 통해서, n명의 약속장소를 구할 수 있다!!
 
 
 <div align="center">

![image](https://github.com/JihoonPark99/Detecting_Abnormal_Sound/assets/108673913/fbe5367c-c195-4e30-8061-4b0dd86dcf11)  
 </div>
 
 
  
  
  
