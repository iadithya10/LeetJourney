class Solution(object):
    def fullJustify(self, words, maxWidth):
    
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

     
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i

            
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                
                total_spaces = maxWidth - sum(len(word) for word in line_words)
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                line = ""
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += " " * (space_between + (1 if k < extra_spaces else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res

        