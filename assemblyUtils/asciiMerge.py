def readFIle(fileDir):
    # gets text form file
    with open(fileDir, 'r') as file:
        text = file.read()
    
    
    return text

def mergeText(fileDir1, fileDir2, startFromLine: int, startFromColumn: int):
    txt1 = readFIle(fileDir1).split("\n")
    txt2 = readFIle(fileDir2).split("\n")

    for index in range(int(startFromLine), len(txt1)):
        line = txt1[index]
        textToMerge = ' ' * int(startFromColumn) + txt2[0]
        line = textToMerge + line[len(textToMerge):]
        txt1[index] = line
        
        txt2.pop(0)
        if not txt2:
            break
        
    txt1 = "\n".join(txt1)
    return txt1
        

if __name__ == "__main__":
    try:
        with open("output.txt", 'x') as file:
            file.write(mergeText(input("file 1 directory: "), input("file 1 directory: "), input("start from line: "), input("start from character: ")))
    except:
        with open("output.txt", 'w') as file:
            file.write(mergeText(input("file 1 directory: "), input("file 2 directory: "), input("start from line: "), input("start from character: ")))
