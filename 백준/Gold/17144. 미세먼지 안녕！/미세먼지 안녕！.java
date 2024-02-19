import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int r, c, t;
    static int[][] grid, copy;
    static Queue<int[]> q;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static ArrayList<Integer> airCleaner;
	public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	r = Integer.parseInt(st.nextToken());
    	c = Integer.parseInt(st.nextToken());
    	t = Integer.parseInt(st.nextToken());
    	
    	grid = new int[r][c];
    	copy = new int[r][c];
    	airCleaner = new ArrayList<>();
    	
    	for (int i=0; i<r; i++) {
    		st = new StringTokenizer(br.readLine());
    		for (int j=0; j<c; j++) {
    			grid[i][j] = Integer.parseInt(st.nextToken());
    			
    			if (grid[i][j] == -1) {
    				airCleaner.add(i);
    			}
    		}
    	}
    	
    	for (int k=0; k<t; k++) {
    		q = new LinkedList();
    		// 1. 미세먼지 확산
    		for (int i=0; i<r; i++) {
        		for (int j=0; j<c; j++) {
        			copy[i][j] = grid[i][j];	// 변화하는 copy 복사하기
        			
        			if (grid[i][j] >= 5) {
        				q.add(new int[] {i, j});	// 확산 대상 추가하기
        			}
        		}
        	}
    		
    		spread();
    		
    		// 2. 공기청정기 동작
    		work();
    	}
    	
    	// 3. 남아있는 미세먼지 양
		int sum = 0;
		for (int i=0; i<r; i++) {
    		for (int j=0; j<c; j++) {
    			if (grid[i][j] > 0) {
    				sum += grid[i][j];
    			}
    		}
    	}
		
		System.out.print(sum);
    }
	
	private static void work() {
	    // 공기청정기 위쪽 반시계 방향 순환
	    for (int i = airCleaner.get(0); i > 0; i--) {	// 아래 방향 (가장 왼쪽)
	        grid[i][0] = grid[i - 1][0];
	    }
	    for (int i = 0; i < c - 1; i++) {	// 왼쪽 방향 (가장 위쪽)
	        grid[0][i] = grid[0][i + 1];
	    }
	    for (int i = 0; i < airCleaner.get(0); i++) {	// 위쪽 방향 (가장 오른쪽)
	        grid[i][c - 1] = grid[i + 1][c - 1];
	    }
	    for (int i = c - 1; i > 1; i--) {	// 오른쪽 방향 (가장 아래쪽)
	        grid[airCleaner.get(0)][i] = grid[airCleaner.get(0)][i - 1];
	    }
	    grid[airCleaner.get(0)][0] = -1;	// 공기청정기 위치
	    grid[airCleaner.get(0)][1] = 0;		// 바람이 밀어낸 부분

	    // 공기청정기 아래쪽 시계 방향 순환
	    for (int i = airCleaner.get(1); i < r - 1; i++) {	// 위쪽 방향 (가장 왼쪽)
	        grid[i][0] = grid[i + 1][0];
	    }
	    for (int i = 0; i < c - 1; i++) {	// 오른쪽 방향 (가장 아래쪽)
	        grid[r - 1][i] = grid[r - 1][i + 1];
	    }
	    for (int i = r - 1; i > airCleaner.get(1); i--) {	// 아래쪽 방향 (가장 오른쪽)
	        grid[i][c - 1] = grid[i - 1][c - 1];
	    }
	    for (int i = c - 1; i > 1; i--) {	// 왼쪽 방향 (가장 위쪽)
	        grid[airCleaner.get(1)][i] = grid[airCleaner.get(1)][i - 1];
	    }
	    grid[airCleaner.get(1)][0] = -1;	// 공기청정기 위치
	    grid[airCleaner.get(1)][1] = 0;		// 바람이 밀어낸 부분
	}
	
	private static void spread() {
		while (!q.isEmpty()) {
			int[] now = q.poll();
			int cnt = 0;
			int spreadNum = grid[now[0]][now[1]] / 5;
			
			for (int i=0; i<4; i++) {
				int nx = now[0] + dx[i];
				int ny = now[1] + dy[i];
				
				if (0<=nx && nx<r && 0<=ny && ny<c) {
					if (grid[nx][ny] != -1) {
						copy[nx][ny] += spreadNum;
						cnt++;
					}
				}
			}
			copy[now[0]][now[1]] -= spreadNum * cnt;
			
		}
		
		// 원본에 덮어씌우기
		for (int i=0; i<r; i++) {
    		for (int j=0; j<c; j++) {
    			grid[i][j] = copy[i][j];
    		}
    	}
	}

}