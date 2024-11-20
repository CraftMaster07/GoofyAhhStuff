walls = {
    "y=0":"0cDh",
    "x=0":"0bAh",
    "c1":"0bBh",
    "c2":"0c9h",
    "c3":"0c8h",
    "c4":"0bCh",
    "seperator":","
}

def generateRoom(chars, width, height):
    width, height = width - 2, height - 2
    room = []
    
    # generate ceiling
    room.append(chars["c2"] + chars["seperator"] + (chars["y=0"] + chars["seperator"]) * (width) + chars["c1"])
    
    # generate walls
    for i in range(height):
        room.append(chars["x=0"] + chars["seperator"] + "'" + " " * width + "'" + chars["seperator"] + chars["x=0"])
    
    # generate floor
    room.append(chars["c3"]  + chars["seperator"] + (chars["y=0"] + chars["seperator"]) * (width) + chars["c4"])
    
    asmRoom = ["db " + x + ", 10, 13" for x in room]
    asmRoom = "\n".join(asmRoom)
    return asmRoom

if __name__ == "__main__":
    print(generateRoom(walls, 10, 10))
