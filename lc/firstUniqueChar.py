def firstUniqChar(self, s: str) -> int:
        return_val = -1
        if len(s) > 0:
            order_dict = OrderedDict(Counter(s))
            for key,value in order_dict.items():
                if value == 1:
                    return_val = s.index(key)
                    break
        return return_val

def firstUniqChar(self,s):
	count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
