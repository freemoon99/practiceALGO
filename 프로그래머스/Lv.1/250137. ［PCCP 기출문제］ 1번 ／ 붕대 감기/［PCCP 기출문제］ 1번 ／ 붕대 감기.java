class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int maxHealth = health;
        int endTime = attacks[attacks.length-1][0];
        int nowIdx = 0;
        int continuity = -1;
        
        for (int i=0; i<=endTime; i++) {
            
            if (attacks[nowIdx][0] == i) {
                health -= attacks[nowIdx][1];
                continuity = 0;
                nowIdx ++;
                
                if (health <= 0){
                    return -1;
                }
                
            } else {
                health = Math.min(maxHealth, health + bandage[1]);
                continuity ++;
            }
            
            if (bandage[0] == continuity) {
                health = Math.min(maxHealth, health + bandage[2]);
                continuity = 0;
            } 
        
            
        }
        
        answer = health;
        return answer;
    }
    
}