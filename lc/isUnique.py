# to validate if string consists of unique characterswithout consuming extra space
# 1. sort the characters and check if any subsequent chars match -> complexity nlogn + n
#2. double loop and check char found after thae location of the character. Complexity n2


def isUnique(data):
    char_dict = {}
    for char in data:
        if char_dict.get(char):
            return False
        char_dict[char] = True
    return True


if __name__ == "__main__":
    input_str = "abcdeff"
    print(isUnique(input_str))
