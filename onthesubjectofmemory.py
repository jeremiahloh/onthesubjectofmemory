code = [[1,3,2,4,1],[3,1,2,4,3],[2,3,4,1,2],[2,1,4,3,1],[4,1,2,3,4]]

def stage1(code) :
    prompt = code[0][-1]
    if prompt == 1:
        return code[0][1]
    elif prompt == 2:
        return code[0][1]
    elif prompt == 3:
        return code[0][2]
    elif prompt == 4:
        return code[0][3]

def stage2(code) :
    prompt = code[1][-1]
    if prompt == 1:
        return 4
    elif prompt == 2:
        temp = stage1(code)
        code1 = code[0].index(temp)
        return code[1][code1]
    elif prompt == 3:
        return code[1][0]
    elif prompt == 4:
        temp = stage1(code)
        code1 = code[0].index(temp)
        return code[1][code1]

def stage3(code) :
    prompt = code[2][-1]
    if prompt == 1:
        return stage2(code)
    elif prompt == 2:
        return stage1(code)
    elif prompt == 3:
        return code[2][2]
    elif prompt == 4:
        return 4

def stage4(code) :
    prompt = code[3][-1]
    if prompt == 1:
        temp = stage1(code)
        code1 = code[0].index(temp)
        return code[3][code1]
    elif prompt == 2:
        return code[3][0]
    elif prompt == 3:
        temp = stage2(code)
        code1 = code[1].index(temp)
        return code[3][code1]
    elif prompt == 4:
        temp = stage2(code)
        code1 = code[1].index(temp)
        return code[3][code1]

def stage5(code) :
    prompt = code[4][-1]
    if prompt == 1:
        temp = stage1(code)
        code1 = code[0].index(temp)
        return code[4][code1]
    elif prompt == 2:
        temp = stage2(code)
        code1 = code[1].index(temp)
        return code[4][code1]
    elif prompt == 3:
        temp = stage3(code)
        code1 = code[2].index(temp)
        return code[4][code1]
    elif prompt == 4:
        temp = stage4(code)
        code1 = code[3].index(temp)
        return code[4][code1]

pin = []
pin.append(stage1(code))
pin.append(stage2(code))
pin.append(stage3(code))
pin.append(stage4(code))
pin.append(stage5(code))

for num in pin:
    print(num, end="")