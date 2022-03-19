import java.util.HashMap;
public class Solution {

    public boolean solution(String[] phone_book){
      
      boolean answer = true;
      HashMap<String, Integer> map = new HashMap<>();
      for (int i = 0; i < phone_book.length; i++)
        map.put(phone_book[i], i);
      System.out.println(map);
      for (int i = 0; i < phone_book.length; i++){
        for (int j = 0; j < phone_book[i].length(); j++){
          System.out.println(phone_book[i].substring(0, j));
          if (map.containsKey(phone_book[i].substring(0,j)))
            return false;
        }
      }
      
      return true;
    }  
  
    public static void main(String[] args) {
      String[] phone_book = {"119", "9764223", "11928372"};
      Solution sol = new Solution();
      
      System.out.println(sol.solution(phone_book));

    }
}