
def cube_1(num):
    answer = num*num*num
    print(answer)

def cube_2(num):
    return num*num*num # already break after 'return'
    print("code")

cube_1(3)

print(cube_2(4))