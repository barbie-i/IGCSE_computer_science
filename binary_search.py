
sorted_list = [1,2,3]
target = 3
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list) - 1

while(left_idx <= right_idx):
    middle_idx = (left_idx + right_idx) /2

    if(sorted_list[middle_idx] == target):
        return middle_idx
    
    elif(target< sorted_list[middle_idx]):
        right_idx = middle_idx - 1
    
    else:
        left_idx = middle_idx + 1

return -1 

    