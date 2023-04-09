# Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive.
# The files must be saved in the order they appear in the queue.

# Input:
# Array of file sizes (0 <= s <= 100)
# Capacity of the HD (0 <= c <= 500)
# Output:
# Number of files that can be fully saved in the HD.

def save(sizes, hd): 
    sym = 0
    count = 0
    
    for i in sizes:
        print(sym)
        if sym < hd:
            sym += i
            count += 1
            
    if sym > hd:
        count -= 1
    return count 
