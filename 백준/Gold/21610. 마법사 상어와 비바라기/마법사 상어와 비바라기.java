import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[][] grid;
	static int[] dr = {0, -1, -1, -1, 0, 1, 1, 1};
	static int[] dc = {-1, -1, 0, 1, 1, 1, 0, -1};
	static Queue<Pair> clouds;
	static ArrayList<Pair> removeCloud;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][n];
        
        for (int i=0; i<n; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<n; j++) {
        		grid[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        // 최초 비구름 생성
        clouds = new LinkedList<>();
        clouds.add(new Pair(n-1, 0));
        clouds.add(new Pair(n-1, 1));
        clouds.add(new Pair(n-2, 0));
        clouds.add(new Pair(n-2, 1));
        
        for (int i=0; i<m; i++) {
        	st = new StringTokenizer(br.readLine());
        	
        	int d = Integer.parseInt(st.nextToken())-1;
        	int s = Integer.parseInt(st.nextToken());
        	
        	// 1. 모든 구름 이동
        	move(d, s);
        	
        	// 2. 비가 내리고, 3. 구름 제거
        	rain();
        	
        	// 4. 물복사 버그
        	waterCopy();
        	
        	// 5. 구름 생성
        	makeClouds();
        }
        
        // 계산
        int sum = 0;
    	for (int i=0; i<n; i++) {
        	for (int j=0; j<n; j++) {
        		sum += grid[i][j];
        	}
        }
    	
    	System.out.print(sum);
    	
    }
    private static boolean isNotRemove(int x, int y) {
    	for (Pair now : removeCloud) {
    		if (now.x == x && now.y == y) {
    			return false;
    		}
    	}
    	return true;
    }
    
    private static void makeClouds() {
    	for (int i=0; i<n; i++) {
        	for (int j=0; j<n; j++) {
        		if (grid[i][j] >= 2 && isNotRemove(i, j)) {
        			clouds.add(new Pair(i, j));
        			grid[i][j] -= 2;
        		}
        	}
        }
    }
    
    private static void waterCopy() {
    	// 물 증가한 칸 == 제거 대상인 구름
    	for (Pair now : removeCloud) {
    		int cnt = 0;
    		
    		for (int i=1; i<8; i+=2) {
    			int nr = now.x + dr[i];
    			int nc = now.y + dc[i];
    			
    			if (0<=nr && nr<n && 0<=nc && nc<n) {
    				if (grid[nr][nc] != 0) {
    					cnt++;
    				}
    			}
    		}
    		
    		grid[now.x][now.y] += cnt;
    	}
    	
    }
    
    private static void rain() {
    	removeCloud = new ArrayList<>();	// 제거 대상인 구름 초기화
    	
    	while (!clouds.isEmpty()) {
    		Pair now = clouds.poll();
    		removeCloud.add(now);
    		
    		grid[now.x][now.y]++;
    	}
    }

    
    private static void move(int d, int s) {
    	ArrayList<Pair> temp = new ArrayList<>();
    	while (!clouds.isEmpty()) {
    		Pair now = clouds.poll();
    		
            int nr = (now.x + dr[d]*s % n + n) % n;
            int nc = (now.y + dc[d]*s % n + n) % n;
            
    		temp.add(new Pair(nr, nc));
    	}
    	
    	for (Pair now : temp) {    		
    		clouds.add(now);
    	}
    	
    }
    
    
    static class Pair {
    	int x, y;
    	
    	public Pair(int x, int y) {
    		this.x = x;
    		this.y = y;
    	}
    }
}