# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        Problem: Find all the possible urls that share the same baseurl
        Solution:
        first getUrls(startUrl) => [url1,url2,url3,....]
        now for each url, we should compare if the base url of the start url and urln is the same or not;
        if it is, then call the getUrls method for the matched url
        the rule is that it is not guaranteed that the starturl will return the list of urls with the same base
        we need to have a method to check the same base url
        we need to do a dfs to find all the visited links and compare
        """
        ans = []
        visited = set()
        # scenario 1: there are leaf urls, where they do not return any child urls
        # scenario 2: there are no leaf urls, so all urls return child urls
        #               in this case we need a stopping condition, where if every child has been visited, then you check for the curr_url for base_url; we can do a preorder traversal, checking as we visit down
        def check_base(url,base_url):
            # need to check if the url contains the base url
            # if yes, need to check if there is something after the slash in the url
            # if nothing after the slash, then return False else return True
            if base_url in url:
                return True
            else:
                return False

        def dfs(curr_url,base_url):
            if curr_url not in visited:
                visited.add(curr_url)
                children_url = htmlParser.getUrls(curr_url)
                # print(children_url)
                # print(visited)
                for child in children_url:
                    if child not in visited:
                        #print("checking between", child, base_url)
                        if check_base(child, base_url):
                            #print("inside")
                            ans.append(child)
                            dfs(child,base_url)
        
        """
        "http://news.yahoo.com/news/topics/"
        ['http://news.yahoo.com', 'http://news.yahoo.com/news']


        """
        # need to get the baseurl
        counter = 0
        baseUrl = ""
        for ch in startUrl:
            if ch=="/" and counter==2:
                break
            elif ch=="/":
                counter += 1
            baseUrl += ch
        ans.append(startUrl)
        dfs(startUrl,baseUrl)
        return ans



