
'''
This problem has a "rucksack" with the same "item" (char) in each "compartment", or half of the line of chars.
The "priorities" are a:z=1:26 and A:Z=27:52
'''

def get_priority(item):
    # a == 97, A == 65
    item = ord(item) + 1  # The problem is 1-indexed.
    if item < 97:
        return item - 65 + 26
    else:
       return item - 97

def run():
    print("Running day 3.")

    inputData = []

    with open("./Data/input_day3.txt", 'r') as fileData:
        inputData = fileData.readlines()

    #
    # PART ONE
    #
    priority_sum = 0

    for line in inputData:
        line = line.strip()
        mid:int = int(len(line)/2)
        #print(f"Len: {len(line)}, mid: {mid}")
        #print(f"Item at mid-1,  mid: ", line[mid-1], line[mid])
        for item in line[0:mid]:
            if item in line[mid:]:
                #print(f"Duplicate item: {item}, with priority: {get_priority(item)}")
                priority_sum += get_priority(item)
                break

    print("Priorities, summed: ", priority_sum)

    #
    # PART TWO
    #
    i1 = 0
    i2 = 1
    i3 = 2
    priority_sum = 0
    inputLen = len(inputData)
    while( i3<inputLen and i2<inputLen and i1<inputLen ):
        for item in inputData[i1]:
            if item in inputData[i2] and item in inputData[i3]:
                badge = item
                priority_sum += get_priority(item)
                break
        i1 += 3
        i2 += 3
        i3 += 3

    print("Badge priority sum: ", priority_sum)



