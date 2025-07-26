def arm_strong(n):
    number_str=str(n)
    power=len(number_str)
    result=0
    for i in number_str:
        result+=int(i)**power
    if result == n:
        print("Arm Strong")
    else:
        print("Not Arm Strong")
number=153
arm_strong(number)