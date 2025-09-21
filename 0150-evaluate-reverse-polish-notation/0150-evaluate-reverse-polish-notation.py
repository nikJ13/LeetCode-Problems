class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            # print(st)
            if t[0]=="-" and len(t)>1:
                st.append(t)
                continue
            if not t.isnumeric():
                op2 = int(st.pop())
                op1 = int(st.pop())
                if t=="+":
                    ans = op1 + op2
                elif t=="/":
                    ans = int(op1 / op2)
                elif t=="-":
                    ans = op1 - op2
                elif t=="*":
                    ans = op1 * op2
                st.append(str(ans))
            else:
                st.append(t)
        return int(st[-1])