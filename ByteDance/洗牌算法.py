import random
def shuffle(arr:list):
    for i in range(len(arr)):
        random_index = random.randint(0,i)
        arr[i],arr[random_index] = arr[random_index],arr[i]
    return arr
print(shuffle([1,2,3,4,5,6,7,8,9,10]))