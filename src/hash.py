from collections import Counter, deque
import sys

def mycode_2002(num, all_cars):
    print(f"start 202")
    num = len(all_cars)//2
    in_cars = all_cars[0:num]
    out_cars = all_cars[num:]
    print(f"num is {num}")
    print(f"in_cars is {in_cars}")
    print(f"out_cars is {out_cars}")

    past_map = []
    out_map = {}
    
    for j, car in enumerate(out_cars):
        out_map[hash(car)] = j


    
    print(f"fast_map is {past_map}")

def mycode_python_stype_2002():
    """
    문제
    대한민국을 비롯한 대부분의 나라에서는 터널 내에서의 차선 변경을 법률로 금하고 있다. 조금만 관찰력이 있는 학생이라면 터널 내부에서는 차선이 파선이 아닌 실선으로 되어 있다는 것을 알고 있을 것이다. 이는 차선을 변경할 수 없음을 말하는 것이고, 따라서 터널 내부에서의 추월은 불가능하다.

    소문난 명콤비 경찰 대근이와 영식이가 추월하는 차량을 잡기 위해 한 터널에 투입되었다. 대근이는 터널의 입구에, 영식이는 터널의 출구에 각각 잠복하고, 대근이는 차가 터널에 들어가는 순서대로, 영식이는 차가 터널에서 나오는 순서대로 각각 차량 번호를 적어 두었다.

    N개의 차량이 지나간 후, 대근이와 영식이는 자신들이 적어 둔 차량 번호의 목록을 보고, 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차들이 몇 대 있다는 것을 알게 되었다. 대근이와 영식이를 도와 이를 구하는 프로그램을 작성해 보자.

    입력
    입력은 총 2N+1개의 줄로 이루어져 있다. 첫 줄에는 차의 대수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 대근이가 적은 차량 번호 목록이 주어지고, N+2째 줄부터 N개의 줄에는 영식이가 적은 차량 번호 목록이 주어진다. 각 차량 번호는 6글자 이상 8글자 이하의 문자열로, 영어 대문자('A'-'Z')와 숫자('0'-'9')로만 이루어져 있다.

    같은 차량 번호가 두 번 이상 주어지는 경우는 없다.

    출력
    첫째 줄에 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차가 몇 대인지 출력한다.

    예제 입력 1 
    4
    ZG431SN
    ZG5080K
    ST123D
    ZG206A
    ZG206A
    ZG431SN
    ZG5080K
    ST123D
    예제 출력 1 
    1
    예제 입력 2 
    5
    ZG508OK
    PU305A
    RI604B
    ZG206A
    ZG232ZF
    PU305A
    ZG232ZF
    ZG206A
    ZG508OK
    RI604B
    예제 출력 2 
    3
    예제 입력 3 
    5
    ZG206A
    PU234Q
    OS945CK
    ZG431SN
    ZG5962J
    ZG5962J
    OS945CK
    ZG206A
    PU234Q
    ZG431SN
    예제 출력 3 
    2
    출처
    Olympiad > Croatian Highschool Competitions in Informatics > 2002 > National Competition #1 - Seniors 1번

    빠진 조건을 찾은 사람: kipa00
    문제의 오타를 찾은 사람: pppqqqpq
    """
    input = sys.stdin.readline 
    num = int(input())
    in_cars = [input().strip() for _ in range(num)]
    out_cars = [input().strip() for _ in range(num)]

    # print(f"start 202")
    # num = len(all_cars)//2
    # in_cars = all_cars[0:num]
    # out_cars = all_cars[num:]
    print(f"num is {num}")
    print(f"in_cars is {in_cars}")
    print(f"out_cars is {out_cars}")

    passed_cars = deque()
    out_map = {}
    fast_map = []
    
    in_map = {car:i for i, car in enumerate(in_cars)} 
    
    print(f"in_map is {in_map}")
    overtakes=0
    for car in out_cars:
        in_pos =  in_map[car] 
        for passed_car in passed_cars:
            print(f"{car}, {in_pos} / {passed_car},{in_map[passed_car]}")
            if in_map[passed_car]  > in_pos:
                overtakes += 1
                break
        passed_cars.add(car) 
        print(passed_cars)
    
 
 
    
    print(f"fast_map is {overtakes}")
    return len(fast_map)
                
def counter_2002(num, all_cars):
    from collections import Counter

def mycode202(n, all_cars):
    # 차량별 등장 횟수 카운트
    car_count = Counter(all_cars)

    # 한 번만 등장한 차량 개수 계산
    unique_count = sum(1 for car, count in car_count.items() if count == 1)

    print(unique_count)  # 최종 출력                

def main(num):
    
     
    
    if (num == 2002) :
        result = mycode_python_stype_2002() 
        print(result)

    

    elif (num == 404) :
        print(f"num is 404")
    print(f"end of the program")


if __name__ == "__main__":
    main(2002)