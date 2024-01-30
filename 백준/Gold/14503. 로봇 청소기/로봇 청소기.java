import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m, sx, sy, sd, cnt = 0;
	static int[] start;
	static int[][] map;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        sx = Integer.parseInt(st.nextToken());
        sy = Integer.parseInt(st.nextToken());
        sd = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        
        for (int i=0; i<n; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<m; j++) {
        		map[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        
        clean(sx, sy, sd);
        System.out.print(cnt);
    }
    private static boolean inRange(int x, int y) {
    	return (0<=x && x<n && 0<=y && y<m);
    }
    
    private static boolean around(int x, int y) {
    	int temp = 0;
    	for (int i=0; i<4; i++) {
    		int nx = x + dx[i];
    		int ny = y + dy[i];
    		
    		if (inRange(nx, ny) && map[nx][ny] == 0) temp++;
    	}
    	
    	return temp > 0;
    }
    
    // 청소
    private static void clean(int x, int y, int d) {
    	// 현재 칸이 청소되어있지 않다면 청소한다
    	if (map[x][y] == 0) {
    		map[x][y] = -1;
        	cnt ++;
    	}
    	
    	// 4방향 중 빈칸이 없는 경우
    	if (!around(x, y)) {
    		// 후진 할 수 있다면 후진
    		int bx = x - dx[d];
    		int by = y - dy[d];
    		
    		if (map[bx][by] != 1) {
    			clean(bx, by, d);
    		} else {	// 후진할 수 없다면 작동 종료
    			return;
    		}
    	} else {	// 빈칸이 있을 경우
    		while (true) {
    			d = (d + 3) % 4;	// 반시계 90도
        		int nx = x + dx[d];
        		int ny = y + dy[d];
        		
        		if (inRange(nx, ny) && map[nx][ny] == 0) {
        			clean(nx, ny, d);
        			break;
        		}
    		}
    		
    	}
    }
    
}