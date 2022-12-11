# 
def parseInput(filename):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    position = []
    INITIAL_STACK_COUNTER = 9
    STACK_LABEL = 8
    MOVE_START = 10
    
    # Create columnwise lists
    for x in range(INITIAL_STACK_COUNTER): # CHANGE THIS. total inital rows till stack number count
        globals()[f'stack_{x}'] = []
    for x in range(len(Lines[STACK_LABEL])): # CHANGE THIS ACCORDING TO INPUT. Lines[x] is the labelling of the stack.
        linechar = Lines[STACK_LABEL][x]
        if linechar.strip() != '':
            position.append(x)
    
    for i in range(len(position)):
        for idx, line in enumerate(Lines):
            if idx == STACK_LABEL: # CHANGE THIS
                break
            if (line[position[i]].strip()):
                globals()[f'stack_{i}'].append(line[position[i]])
    for i in (range(MOVE_START,len(Lines))): # CHANGE THIS. Range starts with the move procedure line
        query = Lines[i]
        stopwords = ['move', 'from', 'to']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        move_count = int(resultwords[0])
        for j in range(move_count):
            # Move 0th element of source stack to 0th elem of destination
            globals()[f'stack_{int(resultwords[2])-1}'].insert(0,globals()[f'stack_{int(resultwords[1])-1}'][0])
            globals()[f'stack_{int(resultwords[1])-1}'].pop(0)
    final_ans = []
    for i in range(len(position)):
        final_ans.append(globals()[f'stack_{i}'][0])
    return(''.join(final_ans))

if __name__ == "__main__":
    file = "input.txt"
    print(parseInput(file))