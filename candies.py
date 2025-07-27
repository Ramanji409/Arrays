def extra_candies(candies,extra):
    new_candies=[]
    max_candies=max(candies)
    for i in range(len(candies)):
        if candies[i]+extra > max_candies:
            new_candies.append("True")
        else:
            new_candies.append("False")
    return new_candies
candies=[2,4,1,6,3]
extra=3
print(extra_candies(candies,extra))