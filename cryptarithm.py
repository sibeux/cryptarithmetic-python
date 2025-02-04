from itertools import product

input1 = str(input("Enter the first letter: "))
input2 = str(input("Enter the second letter: "))
print("----------------------------- +")
result = str(input("Enter the result: "))

arrayInput1 = list(input1)
arrayInput2 = list(input2)
arrayResult = list(result)

permInput1 = product(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat = arrayInput1.__len__())
permInput2 = product(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat = arrayInput2.__len__())

combInput1 = []
combInput2 = []

for i in list(permInput1):
    combInput1.append(i)

for i in list(permInput2):
    combInput2.append(i)

totalPenyelesaian = 0

for i in combInput1:
    for j in combInput2:
        bilA = int("".join(map(str, i)))
        bilB = int("".join(map(str, j)))
        hasil = bilA + bilB

        if len(str(hasil)) == len(arrayResult):
            numbInput1 = list(i)
            numbInput2 = list(j)
            numbResult = list(str(hasil))

            numbInput1 = list(map(str, numbInput1))
            numbInput2 = list(map(str, numbInput2))

            allList = arrayInput1+arrayInput2+arrayResult
            allListNumb = numbInput1+numbInput2+numbResult
            
            setAllList = set(allList)
            setAllListNumb = set(allListNumb)

            if (len(setAllList) == len(setAllListNumb)):
                count = 0
                for indexSetAllList in range (0, len(setAllList)):
                    listSetAllList = list(setAllList)
                    indexValue = [i for i, x in enumerate(
                        allList) if x == listSetAllList[indexSetAllList]]
                    
                    numbByIndexValue = []
                    for i_indexValue in indexValue:
                        numbByIndexValue.append(allListNumb[i_indexValue])
                        
                    setNumbByIndexValue = set(numbByIndexValue)
                    if len(setNumbByIndexValue) == 1:
                        count += 1
                    else:
                        break
                if count == len(setAllList):
                    totalPenyelesaian += 1
                    print(f"{bilA} + {bilB} = {hasil}")

print(f"Total Penyelesaian: {totalPenyelesaian}")
