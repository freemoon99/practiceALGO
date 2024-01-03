import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static char[][] grid;
	static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static Node[] coins;
    static Queue<startCoin> q;
    static boolean[][][][] visited;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        grid = new char[n][m];
        coins = new Node[2];
        
        int coinIdx = 0;
        for (int i=0; i<n; i++) {
            String element = br.readLine();
        	for (int j=0; j<m; j++){
        		grid[i][j] = element.charAt(j);
        		
        		if (grid[i][j] == 'o') {
        			coins[coinIdx++] = new Node(i, j);
        		}
        	}
        }
        
        visited = new boolean[n][m][n][m];
        int result = bfs();
        System.out.print(result);
    }
    
    private static int bfs() {
        q = new LinkedList<>();
        q.add(new startCoin(coins[0].x, coins[0].y, coins[1].x, coins[1].y, 0));
        visited[coins[0].x][coins[0].y][coins[1].x][coins[1].y] = true;
    	
    	while (!q.isEmpty()) {
    		startCoin now = q.poll();
    		
    		if (now.cnt >= 10) {
    			break;
    		}
    		
    		for (int i=0; i<4; i++) {
    			int nx1 = now.x1 + dx[i];
    			int ny1 = now.y1 + dy[i];
    			int nx2 = now.x2 + dx[i];
    			int ny2 = now.y2 + dy[i];
    			
    			if (!canMove(nx1, ny1)) {
    				nx1 = now.x1;
    				ny1 = now.y1;
    			}
    			if (!canMove(nx2, ny2)) {
    				nx2 = now.x2;
    				ny2 = now.y2;
    			}
    			
    			int liveCoin = 0;
    			if (isInRange(nx1, ny1)) liveCoin++;
    			if (isInRange(nx2, ny2)) liveCoin++;
    			
    			if (liveCoin == 1) return now.cnt+1;
    			else if ((liveCoin == 2) && (!visited[nx1][ny1][nx2][ny2])) {
    				visited[nx1][ny1][nx2][ny2] = true;
    				q.add(new startCoin(nx1, ny1, nx2, ny2, now.cnt+1));
    			}
    		}
    		
    	}
    	return -1;
    	
    }
    
    private static boolean isInRange(int x, int y) {
    	return 0<=x && 0<=y && x<n && y<m;
    }
    
    private static boolean canMove(int x, int y) {
    	if (isInRange(x, y) && grid[x][y] == '#') {
    		return false;
    	}
    	return true;
    }
    
    static class startCoin{
    	int x1, y1, x2, y2, cnt;
    	public startCoin(int x1, int y1, int x2, int y2, int cnt) {
    		this.x1 = x1;
    		this.y1 = y1;
    		this.x2 = x2;
    		this.y2 = y2;
    		this.cnt = cnt;
    	}
    }
    
    static class Node {
    	int x,y;
    	public Node(int x, int y) {
    		this.x = x;
    		this.y = y;
    	}
    }
}
