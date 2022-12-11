def getSubroutine(filename, markerType, markerCharacter):
    input_file = open(filename, 'r')
    Lines = input_file.readlines()
    for i in range(len(Lines[0])):
        # Form a string with the new one
        subset = Lines[0][i:i+markerCharacter]
        if len(set(subset)) != len(subset):
            continue
        else:
            print(subset)
            print(f'First {markerType} after character {i+markerCharacter}')
            break



if __name__ == "__main__":
    file = "input.txt"
    getSubroutine(file, "packet", 4)
    getSubroutine(file, "message", 14)

    