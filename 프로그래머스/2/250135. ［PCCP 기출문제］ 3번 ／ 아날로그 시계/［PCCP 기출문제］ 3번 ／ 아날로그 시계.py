def to_seconds(h,m,s):
    return h*60*60 + m*60 + s


def solution(h1,m1,s1,h2,m2,s2):
    answer = 0
    mcount, hcount = 0,0
    
    start_time = to_seconds(h1,m1,s1)
    end_time = to_seconds(h2,m2,s2)
    
    if start_time == 0 or start_time == 60*60*12 :
        answer += 1
        
    for time in range(start_time,end_time):
        s = (time*6)%360
        m = (time/10)%360
        h = (time/120)%360
        
        ns = 360 if (time+1)*6%360 == 0 else (time+1)*6%360
        nm = 360 if (time+1)/10%360 == 0 else (time+1)/10%360
        nh = 360 if (time+1)/120%360 == 0 else (time+1)/120%360
        
        if s < h and ns >= nh :
            hcount += 1
        if s < m and ns >= nm :
            mcount += 1
        if ns==nm==nh :
            answer -= 1
    
    answer += mcount+hcount
    return answer