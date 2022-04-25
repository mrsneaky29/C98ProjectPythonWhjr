def swapFileData():
    file1name=input("Name of First file: ")
    file2name=input("Name of Second file: ")
    with open(file1name , 'r') as a:
        dataA = a.read()
    with open(file2name , 'r') as b:
        dataB = b.read()
    with open(file1name , 'w') as a:
        a.write(dataB)
    with open(file2name , 'w') as b:
        b.write(dataA)
        print("Swapped!")

swapFileData()