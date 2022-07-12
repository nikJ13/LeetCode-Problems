// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int t;
		t = sc.nextInt();
		String s12 = sc.nextLine();
		for(int i=0; i<t; i++){
		    String s1 = sc.nextLine();
		    String s2 = sc.nextLine();
		    
		    Solution obj = new Solution();
		    
		    boolean flag = obj.isRotated(s1, s2);
		    
		    if(flag == true) System.out.println("1");
		    else System.out.println("0");
		    
		}
	}
}// } Driver Code Ends


class Solution
{
    //Function to check if a string can be obtained by rotating
    //another string by exactly 2 places.
    
    private static boolean clock(String str1, String str2){
        for(int i=0;i<str1.length();i++){
            if(str1.charAt(i)!=str2.charAt((i+2)%str1.length())){
                return false;
            }
        }
        return true;
    }
    
    private static boolean antiClock(String str1, String str2){
        for(int i=0;i<str1.length();i++){
            if(str1.charAt((i+2)%str1.length())!=str2.charAt(i)){
                return false;
            }
        }
        return true;
    }
    public static boolean isRotated(String str1, String str2)
    {
        // Your code here
        if(clock(str1,str2) || antiClock(str1,str2)){
            return true;
        }
        return false;
        
    }
    
}