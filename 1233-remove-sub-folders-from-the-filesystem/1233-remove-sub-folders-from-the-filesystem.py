class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Problem: need to return all the subfolders and return the folders
        Solution:
        Need to first determine what is a subfolder here:
        /a
        so in a path /x/y/z, if the folder list contains any of the parents, then remove z

        we could use a trie data structure?
        we could mark the nodes as parents
        or instead store the parent for every starting folder
        {a:["/a"]}
        for each iteration:
            check the starting folder
            check if it is present in the dictionary or not
                if it is not in the dictionary, add entry
                if it is in the dictionary, then
                    check length with the parent (meaning number of folders with the parent)
                        if the number of folders is the same then add to the list
                        if number of folders is lesser than that of the parent, check if the last folder in the entry is same as that position entry in the parent
                            if it is the same, then replace the parent, else, add this to the list
        we might need some sort of a tree traversal
        trie would work here
        """
        folder.sort()
        ans = [folder[0]]
        for f in folder[1:]:
            last = ans[-1]
            if not f.startswith(last) or f[len(last)]!="/":
                ans.append(f)
        return ans

