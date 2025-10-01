class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        # {"bread":["yeast","flour"], "sandwich":["bread","meat"]}
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        visited = set()
        memory_recipes = {}
        dict_edges = {}
        for idx in range(len(recipes)):
            dict_edges[recipes[idx]] = ingredients[idx]
        # print(dict_edges)
        result = []
        def helper(food):
            if food in supplies_set:
                return True

            if food not in recipes_set:
                return False
            
            if food in memory_recipes:
                return memory_recipes[food]

            if food in visited:
                return False
            visited.add(food)
            for k in dict_edges[food]:
                if not helper(k):
                    memory_recipes[k] = False
                    visited.remove(food)
                    return False
            memory_recipes[food] = True
            visited.remove(food)
            return True
        for r in recipes:
            if helper(r):
                result.append(r)
        # print(visited)
        return result