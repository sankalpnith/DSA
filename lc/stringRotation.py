def checkRotation(s1, s2):
    temp = s1+s1
    if temp.count(s2) >= 1:
        return True
    return False


if __name__=="__main__":
    s1 = "sankalp"
    s2= 'kalpsan'
    print(checkRotation(s1,s2))
