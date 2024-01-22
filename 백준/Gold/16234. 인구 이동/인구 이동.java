import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, l, r, cnt = 0;
	static int[][] grid, visited;
	static ArrayList<Pair> list;
	static boolean flag;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        grid = new int[n][n];
        visited = new int[n][n];
        list = new ArrayList<>();
        
        for (int i=0; i<n; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<n; j++) {
        		grid[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        canMove();
        System.out.print(cnt);
    }
   
    private static void bfs(int x, int y) {
    	Queue<Pair> q = new LinkedList<>();
    	q.offer(new Pair(x, y));
    	visited[x][y] = 1;
    	list.add(new Pair(x,y));
    	
    	while (!q.isEmpty()) {
    		Pair now = q.poll();
    		
    		for (int i=0; i<4; i++) {
    			int nx = now.x + dx[i];
    			int ny = now.y + dy[i];
    			
    			if (0<=nx && nx<n && 0<=ny && ny<n) {
    				if (visited[nx][ny] == 0) {
    					int compare = Math.abs(grid[now.x][now.y]-grid[nx][ny]);	// 이동을 비교할 인구수 차
    					if (l<=compare && compare<=r) {
    						flag = true;	// 인구 이동 존재
    						visited[nx][ny] = 1;
    						q.offer(new Pair(nx, ny));
    						list.add(new Pair(nx, ny));
    					}
    				}
    			}
    		}
    	}
    	
//    	이동 결과 합 구하기
    	int sum = 0;
    	for (Pair p : list) {
    		sum += grid[p.x][p.y];
    	}
//    	이동 결과 덮어씌우기
    	for (Pair p : list) {
    		grid[p.x][p.y] = sum / list.size();
    	}
    	
    	list.clear();
    }
    
    private static void canMove() {
//    	더이상 불가능할 때까지 반복
    	while (true) {
    		flag = false;
            for (int[] row : visited) Arrays.fill(row, 0);	// 매 이동 체크 시 방문 배열 초기화
            
    		for (int i=0; i<n; i++) {
            	for (int j=0; j<n; j++) {
            		if(visited[i][j] == 0) {
            			bfs(i, j);
            		}
            	}
            }
    		
//    		종료 조건 : 이동이 없다면
    		if (flag) cnt++;
    		else break;
    	}
    }
    
    static class Pair{
    	int x, y;
    	
    	public Pair(int x, int y) {
    		this.x = x;
    		this.y = y;
    	}
    }
}
