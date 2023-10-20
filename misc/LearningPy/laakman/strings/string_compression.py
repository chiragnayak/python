
if __name__ == "__main__":

    str1 = "chirag nayak"
    count = {}
    compressed = False
    for c in range(0, len(str1)):
        c = str1[c]
        if c == " ":
            continue
        if c in count:
            compressed = True
            count[c] = count[c] + 1
        else:
            count[c] = 1
    if not compressed:
        print (str1)
    else:
        result = ""
        for k, v in count.items():
            append = k + str(v)
            result += append
        print(result)
