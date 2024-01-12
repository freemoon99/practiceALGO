import java.util.*;

class Solution {
    static int n, m;
    static Queue<Pair> q = new LinkedList<>();
    static int[][] visited;
    static ArrayList<Integer> counts;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};
    static int[][] land;
    
    public int solution(int[][] land) {
        int answer = 0;
        n = land.length;
        m = land[0].length;
        this.land = land;
        counts = new ArrayList<>();
        
        visited = new int[n][m];
        for (int i=0; i<n; i++){
            Arrays.fill(visited[i], 0);
        }
        counts.add(0);
        
        int num = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (visited[i][j] == 0 && land[i][j] == 1) {
                    num ++;
                    bfs(i, j, num);
                }
            }
        }
        
        for (int col=0; col<m; col++) {
            int sum = 0;
            Set<Integer> set = new HashSet<>();
            for (int row=0; row<n; row++){
               if (land[row][col] == 1) {
                   set.add(visited[row][col]);
               }            
            }
            
            for (int idx : set){
                sum += counts.get(idx);
            }
           
            answer = Math.max(answer, sum);
        }
        
        return answer;
    }
    
    private static void bfs(int x, int y, int num) {
        int temp = 1;
        q.offer(new Pair(x, y));
        visited[x][y] = num;
        
        while(!q.isEmpty()) {
            Pair now = q.poll();
            
            
            for (int i=0; i<4; i++){
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if (0<=nx && nx<n && 0<=ny && ny<m){
                    if (visited[nx][ny] == 0) {
                        if (land[nx][ny] == 1) {
                            temp ++;
                            q.offer(new Pair(nx, ny));
                            visited[nx][ny] = num;
                        }
                    }
                }
            }
        }
        
        counts.add(temp);
    }
    
    static class Pair {
        int x, y;
        
        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}