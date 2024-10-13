from math import ceil

def solution(fees, records):
    answer = []
    # default time, default fee, unit time, unit fee
    dt, df, ut, uf = fees
    # parking = {차 번호 : 주차장 들어온 시간}
    # parking_time = {차 번호 : 주차장에 머문 총 시간}
    parking, parking_time = dict(), dict()
    
    for record in records:
        time, car, inout = record.split()
        if inout == "IN" : 
            # 주차장 들어왔을 때, 차번호 : 시간
            parking[car] = time
        else:
            # 주차장 나갈 때 시간 계산
            # "IN"일 때 parking에 등록된 차 번호 : 시간 -> in_hour, in_time
            in_hour, in_time = map(int, parking[car].split(':'))
            out_hour, out_time = map(int, time.split(':'))
            total_time = (out_hour*60+out_time) - (in_hour*60+in_time)
            
            # parking_time은 {차 번호 : 주차장에 머문 총 시간} 저장
            parking_time[car] = parking_time.get(car,0) + total_time
            parking[car] = inout
            
    # IN만 있고 OUT 없는 차의 경우
    for key, value in parking.items():
        if value != "OUT":
            in_hour, in_time = map(int,value.split(':'))
            total_time = (23*60+59) - (in_hour*60+in_time)
            parking_time[key] = parking_time.get(key,0) + total_time
            
    parking_time = sorted(parking_time.items())
    
    for car, total_time in parking_time:
        if total_time <= dt : 
            answer.append(df)
        else:
            total_fee = df+ceil((total_time-dt)/ut)*uf
            answer.append(total_fee)
            

    return answer
