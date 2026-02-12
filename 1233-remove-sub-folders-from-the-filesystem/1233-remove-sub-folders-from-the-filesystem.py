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
        dict_folders = {}

        def build(dict_f, arr):
            if len(arr)==0:
                return
            if arr[0] not in dict_f:
                dict_f[arr[0]] = {}
            build(dict_f[arr[0]],arr[1:])
        
        def check(dict_f, arr):
            if len(arr)==0: # if the string ends, that is the parent then, return empty dict
                return {}
            if arr[0] not in dict_f: # if it has wiped clean then return empty dict
                return {}
            dict_f[arr[0]] = check(dict_f[arr[0]],arr[1:])
            return dict_f

        for f in folder:
            f_arr = f.split("/")[1:]
            build(dict_folders, f_arr)
        print(dict_folders)
        for f in folder:
            f_arr = f.split("/")[1:]
            dict_folders = check(dict_folders, f_arr)
        
        ans = []

        def traverse(dict_f,path):
            if len(dict_f)==0:
                ans.append(path[:-1])
                return
            for keys in dict_f:
                traverse(dict_f[keys],path+keys+"/")

        traverse(dict_folders,"/")
        return ans


