class Solution:
    def equalFrequency(self, word: str) -> bool:

        count = Counter(word)

        for w, freq in sorted(count.items()):
            hold = count[w]
            count[w] -= 1
            

            if (count[w] == 0):
                count.pop(w)
            
            if len(set(count.values())) == 1:
                return True
            
            count[w] = hold

        return False