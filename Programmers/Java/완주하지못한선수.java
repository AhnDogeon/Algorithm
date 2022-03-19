import java.util.HashMap;
public class Solution {

    public String solution(String[] participant, String[] completion){
      
      String answer = "";
      HashMap<String, Integer> map = new HashMap<>();
      
      for (String player : participant)
        map.put(player, map.getOrDefault(player,0)+1);
      System.out.println(map);
      
      for (String player : completion)
        map.put(player, map.get(player) -1);
      System.out.println(map);
      
      
      return answer;
    }  
  
    public static void main(String[] args) {
      String[] part = {"leo", "kiki", "eden"};
      String[] comp = {"leo", "eden"};
      Solution sol = new Solution();
      
      System.out.println(sol.solution(part, comp));

    }
}