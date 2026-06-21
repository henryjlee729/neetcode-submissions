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
            delimPos = s.find('#', i)            
            length = int(s[i : delimPos])
            i = delimPos + 1            
            result.append(s[i : i + length])
            i += length

        return result