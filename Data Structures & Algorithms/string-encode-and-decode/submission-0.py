class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delim_pos = s.find('#', i)            
            length = int(s[i : delim_pos])
            i = delim_pos + 1            
            result.append(s[i : i + length])
            i += length

        return result