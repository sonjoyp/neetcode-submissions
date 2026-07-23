class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map={
            ')' :'(',
            '}' :'{',
            ']' :'['
        }
        paren_stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                paren_stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(paren_stack) > 0:
                    top_item = paren_stack.pop()
                    print(top_item)
                    if (top_item != bracket_map[char]):
                        return False
                else:
                    return False
        return len(paren_stack) == 0