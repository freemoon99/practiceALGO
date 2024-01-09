import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static HashMap<String, Pair> map;
	static int n, m, cnt = 0;
	static char[][] grid;
	static int[][] visited;
	static int area = 1;
	
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        map = new HashMap<>();
        map.put("U", new Pair(-1, 0));
        map.put("D", new Pair(1, 0));
        map.put("L", new Pair(0, -1));
        map.put("R", new Pair(0, 1));
        
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new char[n][m];
        
        for (int i=0; i<n; i++) {
        	String str = br.readLine();
        	for (int j=0; j<m; j++) {
        		grid[i][j] = str.charAt(j);
        	}
        }
        
		visited = new int[n][m];
		
        for (int i=0; i<n; i++) {
        	for (int j=0; j<m; j++) {
        		if (visited[i][j] == 0) {
        			dfs(i, j);
        		}
        	}
        }

        System.out.println(cnt);
    }
    
    private static void dfs(int x, int y) {
    	visited[x][y] = 1;
    	
    	Pair direction = map.get(Character.toString(grid[x][y]));
    	
    	int nx = x + direction.x;
        int ny = y + direction.y;
        
        if (visited[nx][ny] == 0) {
            dfs(nx, ny);
        } else if (visited[nx][ny] == 1) {
        	cnt++;
        }
        visited[x][y] = 2;
    }
    
	
	static class Pair {
		int x, y;
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
   
}