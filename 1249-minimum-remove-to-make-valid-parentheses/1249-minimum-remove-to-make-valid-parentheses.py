class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        answer = []

        for i in range(len(s)):
            if s[i] == ')':
                if not stack:
                    remove.append(i)
                else:
                    stack.pop()
            elif s[i] == '(':
                stack.append(i)
        remove.extend(stack)

        to_be_deleted = set(remove)
        for i in range(len(s)):
            if i not in to_be_deleted:
                answer.append(s[i])
        return ''.join(answer)
        