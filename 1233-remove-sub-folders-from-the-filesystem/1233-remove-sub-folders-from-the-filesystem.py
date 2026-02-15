class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sorted_folder = sorted(folder)
        ans = [sorted_folder[0]]
        for f in sorted_folder[1:]:
            last = ans[-1]
            # check if the current folder does not start with the last ancestor folder and if 
            # the current folder does not contain a "/" in the last ancestor folder's length's position
            if not f.startswith(last) or f[len(last)]!="/":
                ans.append(f)
        return ans
            