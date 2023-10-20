

if __name__ == "__main__" :

    s = "chirag nayak"
    dic = {}
    unique = True
    for c in s:
        if c in dic:
            print("Not Unique")
            unique = False
            break
        else:
            dic[c] = c
    if unique:
        print("Unique")