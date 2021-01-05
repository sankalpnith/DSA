def compress(chars):
    count = 1
    index = 0
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            count += 1
        else:
            chars[index] = chars[i]
            index += 1
            if count > 1:
                chars[index] = count
                index += 1
                count = 1
    chars[index] = chars[-1]
    if count > 1:
        index += 1
        chars[index] = count
    print(index)
    return chars[:index+1]


if __name__ == "__main__":
    str1 = ['a','b','c','d','d']
    print(compress(str1))

