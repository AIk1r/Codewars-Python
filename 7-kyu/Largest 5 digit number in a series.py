def solution(number):
    values = [number[i:i+5] for i in range(len(number)-4)]
    values.sort()
    return int(values[-1])
