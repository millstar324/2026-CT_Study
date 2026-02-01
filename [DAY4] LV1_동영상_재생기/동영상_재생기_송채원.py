from datetime import datetime, timedelta

def skip(pt, os, oe):
    fmt = "%M:%S"
    if datetime.strptime(os,fmt) <= pt <= datetime.strptime(oe,fmt):
        return datetime.strptime(oe,fmt)
    
    return pt


def solution(video_len, pos, op_start, op_end, commands):
    fmt = "%M:%S"
    p_time = datetime.strptime(pos,fmt)
    p_time = skip(p_time, op_start, op_end)
    # print(p_time)
    std_time = timedelta(seconds=10)
        
    for i in commands:
        if i =="next":
            if p_time+std_time< datetime.strptime(video_len,fmt):
                p_time = p_time+std_time
                p_time = skip(p_time, op_start, op_end)
            else:
                p_time = datetime.strptime(video_len, fmt)
                p_time = skip(p_time, op_start, op_end)
        elif i == "prev":
            if p_time - std_time > datetime.strptime("00:00",fmt):
                p_time = p_time-std_time
                p_time = skip(p_time, op_start, op_end)
            else:
                p_time = datetime.strptime("00:00", fmt)
                p_time = skip(p_time, op_start, op_end)
                
                
          
    return p_time.strftime(fmt)