from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

def createPriorities():
    letters = {}
    value = 1
    for i in alc:
        letters[i] = value
        value += 1
    for i in auc:
        letters[i] = value
        value += 1
    return letters
def getRucksackPriorityCount(filename, scores):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    total_score = 0
    for line in Lines:
        compartment1 = line[:int(len(line)/2)]
        compartment2 = line[int(len(line)/2):]
        common_character = ''.join(set(compartment1).intersection(compartment2))
        total_score = total_score + scores[common_character]
    return total_score
def getGroupPriorityCount(filename, scores):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    group = []
    total_score,count = 0,0
    for line in Lines:
        if count % 2 == 0 and count != 0:
            group.append(line.strip())
            common_character = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))
            total_score = total_score + scores[common_character]
            group.clear()
            count = 0
        else:
            group.append(line.strip())
            count += 1
    return total_score

if __name__ == "__main__":
    file = "input.txt"
    letters = createPriorities()
    print(f'The sum of priority items is {getRucksackPriorityCount(file, letters)}')
    print(f'The sum of group priority items is {getGroupPriorityCount(file, letters)}')