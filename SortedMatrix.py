def NumTextCase():
    roda = True
    t = 0
    while roda:
        t = int(input("Tape a Integer(> 0 and < 100): "))
        if t > 0 and t < 100:
            roda = False

        else:
            print("Error! Number out of range, try again")
    return t

def CreateMatrix():
    roda = True
    matrix = []
    while roda:
        n = int(input("Type the size of the matrix: "))
        if n > 0 and n < 100:
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(int(input("Type a number: ")))
                matrix.append(row)
                roda = False
            print("Typed Matrix: ")
            for line in matrix:
                print(line)

        else:
            print("Error! Number out of range, try again")
    print("\n")
    return matrix

def SortMatrix(matrix):
    allElem = []
    cont = -1
    sortedMatrix = []
    for i in matrix:
        cont += 1
        for j in i:
            allElem.append(j)
    allElem.sort()
    row = []
    for elem in range(len(allElem)):
        row.append(allElem[elem])
        if len(row) == cont+1:
            sortedMatrix.append(row)
            row = []
    return sortedMatrix

def Output(sortedMatrix):
    print("Sorted Matrix: ")
    for i in sortedMatrix:
        print(i)
    print("\n")
    

def main():
    T = NumTextCase()
    for i in range(T):
        matrix = CreateMatrix()
        sortedMatrix = SortMatrix(matrix)
        Output(sortedMatrix)

main()