    def frequencySort(self, s: str) -> str:
        dictionary = defaultdict(int)
        for char in s:
            dictionary[char] += 1
        sorted_list = sorted(dictionary, key=lambda x:dictionary[x], reverse=True)
        return_val = ""
        for key in sorted_list:
            return_val += key*dictionary[key]
        return return_val

    def frequencySort(self, s: str) -> str:
        counter = Counter(s).most_common()
        return_val = ""
        for key,value in counter:
            return_val += key*value
        return return_val
