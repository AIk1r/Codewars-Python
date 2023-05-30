def pendulum(values):
    sorted_values = sorted(values)
    mid = [sorted_values[0]]
    right = sorted_values[1::2]
    left = sorted_values[2::2]
    return left[::-1] + mid + right
