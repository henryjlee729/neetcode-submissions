class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for i in range(0, len(words) - 1):
            firstWord = words[i]
            secondWord = words[i + 1]
            minLength = min(len(firstWord), len(secondWord))
            if firstWord[:minLength] == secondWord[:minLength] and len(firstWord) > len(secondWord):
                return ""

            for j in range(0, minLength):
                if firstWord[j] != secondWord[j]:
                    graph[firstWord[j]].add(secondWord[j])
                    break

        stateMap = {}
        result = []
        for char in graph:
            if char not in stateMap:
                if not self.dfs(char, graph, stateMap, result):
                    return ""

        result = result[::-1]
        return "".join(result)
    
    def dfs(self, char, graph, stateMap, result):
        if char in stateMap:
            if stateMap[char] == "visiting":
                return False
            if stateMap[char] == "completed":
                return True
       
        stateMap[char] = "visiting"
        for neighbor in graph[char]:
            if not self.dfs(neighbor, graph, stateMap, result):
                return False

        stateMap[char] = "completed"
        result.append(char)
        return True