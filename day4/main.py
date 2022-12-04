
def getContainedRange(filename, requirement):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    total_score = 0
    for line in Lines:
        set1 = (set(range(int((line.split(",")[0]).split('-')[0]), int((line.split(",")[0]).split('-')[1])+1)))
        set2 = (set(range(int((line.split(",")[1]).split('-')[0]), int((line.split(",")[1]).split('-')[1])+1)))
        if requirement == "full":
            if len(set1.intersection(set2)) == len(set1) or len(set1.intersection(set2)) == len(set2):
                total_score = total_score + 1
        if requirement == "partial":
            if len(set1.intersection(set2)) > 0:
                total_score = total_score + 1
    return total_score

if __name__ == "__main__":
    file = "input.txt"
    print(f'Total fully contained ranges are {getContainedRange(file,"full")}')
    print(f'Total partially contained ranges are {getContainedRange(file,"partial")}')