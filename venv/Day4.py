
# The goal is to find complete overlaps of assignments.

def intify_list(list_in:list)->list:
    ret = []
    for string in list_in:
        '''
        if string is not type(str):
            Raise n
            '''
        ret.append(int(string))
    return ret

''' 4 possible cases: r1[0]<r0[0]<r1[1], r1[0]<r0[1]<r1[1], r0[0]<r1[0]<r0[1], r0[0]<r1[1]<r0[1]'''
def overlap(range0, range1)->bool:
    if range0[0] >= range1[0] and range0[0] <= range1[1]:
        return True
    elif range0[1] >= range1[0] and range0[1] <= range1[1]:
        return True
    elif range1[0] >= range0[0] and range1[0] <= range0[1]:
        return True
    elif range1[1] >= range0[0] and range1[0] <= range0[1]:
        return True
    return False


''' 'main' for Day4'''
def run():
    print("Running day 4.")

    inputData = []

    with open("./Data/input_day4.txt", 'r') as fileData:
        inputData = fileData.readlines()

    assignments = []
    num_overlapping_fully = 0

    num_overlap_at_all = 0

    for line in inputData:
        ranges = line.strip().split(",")
        range0 = ranges[0].split("-")
        range1 = ranges[1].split("-")
        ranges_overlap = False
        range0 = intify_list(range0)
        range1 = intify_list(range1)
        if range0 is None or range1 is None:
            continue

        #print(f"Range0: {range0}, range1: {range1}")
        # A range will be subsumed iff the low is >= and the high is <=:
        if range0[0] >= range1[0] and range0[1] <= range1[1]:
            num_overlapping_fully += 1
            print("Overlapping ranges: ", range0, range1)
            True == ranges_overlap
        elif range1[0] >= range0[0] and range1[1] <= range0[1]:
            num_overlapping_fully += 1
            True == ranges_overlap

        if ranges_overlap:
            # numoverlappingAssignments += 1
            print("Overlapping ranges: ", range0, range1)
        #assignments.append(line.split(','))


        # for part two, we just want to know if they overlap at all:
        if overlap(range0, range1):
            num_overlap_at_all += 1

    print("Fully overlap: ", num_overlapping_fully)
    print("Overlap at all: ", num_overlap_at_all)

