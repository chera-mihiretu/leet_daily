class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ']':
                subs = ""

                while stack[-1] != '[':
                    subs = stack.pop() + subs
                stack.pop()

                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * subs)
            else:
                stack.append(i)
        return ''.join(stack)

