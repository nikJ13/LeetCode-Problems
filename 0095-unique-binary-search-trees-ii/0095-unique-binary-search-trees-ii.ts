/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */


function insrtBst(node: TreeNode | null, item: number  ): void {
    if (node === null) {
        return 
    }
    
    if (item < node.val) {
        if (node.left === null) {
            node.left = new TreeNode(item)
            return 
        } else {
            insrtBst( node.left, item)
        }
    } else {
        if (node.right === null) {
            node.right = new TreeNode(item)
            return 
        } else {
            insrtBst( node.right, item)
        }
    }
}

function getInOrderTreversal ( root: TreeNode | null): number[] {
        
    const answer = []
    
    if (root === null) {
        return answer
    }
    
    function _getInOrderTreversal (node: TreeNode | null) {
        
        if (node === null) {
            return 
        }
        
        if (node.left === null && node.right === null) {
            answer.push(node.val)
            return
        }
        
        
        answer.push(node.val)
        _getInOrderTreversal(node.left)
        _getInOrderTreversal(node.right)
    }
    
    
    _getInOrderTreversal(root)
    
    return answer 
}

function generateTrees(n: number): Array<TreeNode | null> {
    const schedules = []
    const uniqueInOrderTreversals = new Set<string>()
    
    
    function dfs (schedule: number[], numsUsed: number, bitmaask: number) { 
        
        if (numsUsed === n) {
            schedules.push([...schedule])
            return
        }
        
        
        for (let i = 1; i <= n; i++) {
            if ((bitmaask & (1 << i) ) === 0) {
                schedule.push(i)
                dfs(schedule, numsUsed +1, (bitmaask |  (1 << i)))
                schedule.pop()
            }
        }
    }
    
    for (let i = 1; i <= n; i++) {
        dfs([i], 1, 1 << i)
    }
    
    const answers = []
    
    for (let schedule of schedules) {
        
        const root  = new TreeNode(schedule[0])
        
        for (let i =1; i < schedule.length; i++ ) {
            insrtBst(root, schedule[i]);
        }
        
        const inorderTreversalKey =  getInOrderTreversal(root).join(",")
        // console.log(inorderTreversalKey)
        if (uniqueInOrderTreversals.has(inorderTreversalKey)) {
            continue
        }
        
        uniqueInOrderTreversals.add(inorderTreversalKey)
        
        // uniqness check 
        answers.push(root)   
    }
    
    
    
    return answers
    
};

/// O(n!n) -> O(n!)

