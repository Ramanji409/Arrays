def polindram(s):
    s1=str(s)
    s2=s1[::-1]
    if s1==s2:
        return "Plindram"
    else:
        return "Not Polindram"
string=1331
print(polindram(string))


