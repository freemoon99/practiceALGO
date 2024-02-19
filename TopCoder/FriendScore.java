public class FriendScore {
  public int highestScore(String[] friends) {
    int ans = 0;
    
    for (int i=0; i<friends.length; i++) {
      int temp = 0;
      
      for (int j=0; j<friends.length; j++) {
        if (i == j) continue;
        if (friends[i].charAt(j) == 'Y') {
          temp ++;  // 직접 친구
        } else { 
          for (int k=0; k<friends.length; k++) {
            if (friends[j].charAt(k) == 'Y' && friends[k].charAt(i) == 'Y'){  // i와 j를 모두 친구로 두고 있는 k가 존재할 경우
              temp ++;  //간접 친구
              break;
            }
          }
        }
      }
      
      ans = Math.max(ans, temp);
    }
      return ans;
  }
}