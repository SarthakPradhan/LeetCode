class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        num2let = {"2":["a","b","c"],
                  "3":["d","e","f"],
                  "4":["g","h","i"],
                  "5":["j","k","l"],
                  "6":["m","n","o"],
                  "7":["p","q","r","s"],
                  "8":["t","u","v"],
                  "9":["w","x","y","z"]}
        
        first = num2let[digits[0]]
        
        for i in range(1,len(digits)):
            temp = []
            second = num2let[digits[i]]
            for c in first:
                for d in second:
                    temp.append(c+d)
                    
            first = temp
            
            
        return first
                    