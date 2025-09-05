class Solution(object):
    def secondHighest(self, s):
        first = second = -1  # store as integers

        for ch in s:
            if ch.isdigit():
                num = int(ch)
                if num > first:
                    second = first
                    first = num
                elif num > second and num != first:
                    second = num

        return second



        