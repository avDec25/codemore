class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        word = []
        words = []
        for c in text:
            if c == ' ':
                if len(word) > 0:
                    words.append(''.join(word))
                    word = []
                spaces += 1
            else:
                word.append(c)

        if len(word) > 0:
            words.append(''.join(word))
        
        if len(words) != 1:
            extra = spaces % (len(words)-1)
            for i in range(spaces - extra):
                words[i % (len(words)-1 or 1)] += ' '        
        
        return ''.join(words).ljust(len(text))

text = "  hello"
Solution().reorderSpaces(text)