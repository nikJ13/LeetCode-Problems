class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0

        # /home/
        # i = 0,1,2,3,4
        # directory = home
        while i<len(path):
            # iterate through the string
            if path[i]=="/":
                i += 1
                continue
            directory = ""
            while i<len(path) and path[i]!="/":
                print(i)
                directory += path[i]
                i += 1
            # add the directory to the stack
            if directory=="..":
                if stack:
                    stack.pop()
            elif directory!=".":
                stack.append(directory)
            i += 1
        if not stack:
            return "/"
        ans = ""
        for names in stack:
            ans += "/"
            ans += names
        return ans


                