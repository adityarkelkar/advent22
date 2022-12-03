def getCalories(filename):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    nos,totals = [],[]
    highest_count = 0
    for line in Lines:
        if line.strip() != '':
            value=int(line)
            nos.append(value)
            if line == Lines[-1]:
                highest_count = sum(nos) if highest_count < sum(nos) else highest_count
                totals.append(sum(nos))
                nos.clear()
        else:
            # last line
            highest_count = sum(nos) if highest_count < sum(nos) else highest_count
            totals.append(sum(nos))
            # Clear the list
            nos.clear()
    print(f"Puzzle 1 answer : {highest_count}")
    print(f"Puzzle 2 answer : {sum(sorted(totals,reverse=True)[:3])}")

if __name__ == "__main__":
    file = "input.txt"
    getCalories(file)