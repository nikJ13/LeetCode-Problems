class Solution {
    public boolean backspaceCompare(String s, String t) {
        List<Character> stack_s = new ArrayList<>();
        List<Character> stack_t = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)!='#'){
                stack_s.add(s.charAt(i));
            }else{
                if(stack_s.size()==0){
                    continue;
                }
                stack_s.remove(stack_s.size()-1);
            }
        }
        for(int i=0;i<t.length();i++){
            if(t.charAt(i)!='#'){
                stack_t.add(t.charAt(i));
            }else{
                if(stack_t.size()==0){
                    continue;
                }
                stack_t.remove(stack_t.size()-1);
            }
        }
        if(stack_s.size()==stack_t.size()){
            for(int i=0;i<stack_s.size();i++){
                if(stack_s.get(i)!=stack_t.get(i)){
                    return false;
                }
            }
        }else{
            return false;
        }
        return true;
    }
}