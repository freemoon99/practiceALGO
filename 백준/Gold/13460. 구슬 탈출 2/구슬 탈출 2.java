import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[] blue, red;
	static char[][] grid;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	static boolean[][][][] visited;
	
	public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	n = Integer.parseInt(st.nextToken());
    	m = Integer.parseInt(st.nextToken());
    	grid = new char[n][m];
    	
    	for (int i=0; i<n; i++) {
    		String input = br.readLine();
    	
    		for (int j=0; j<m; j++) {
    			grid[i][j] = input.charAt(j);
    			
    			if (grid[i][j] == 'B') {
    				blue = new int[] {i, j};
    			}
    			if (grid[i][j] == 'R') {
    				red = new int[] {i, j};
    			}
    		}
    	}
    	
    	visited = new boolean[n][m][n][m];
    	System.out.print(bfs());
    	
	}
	
	static int bfs() {
		Queue<Marble> q = new LinkedList();
		q.add(new Marble(blue[0], blue[1], red[0], red[1], 1));
		visited[blue[0]][blue[1]][red[0]][red[1]] = true;
		
		while (!q.isEmpty()) {
			Marble now = q.poll();
		
			if (now.count > 10) {
				return -1;
			}
			
			// 기울이기 순회
			for (int i=0; i<4; i++) {
				int redMove = 0;
				int blueMove = 0;
				
				// 빨간색
				int nrx = now.rx + dx[i];
				int nry = now.ry + dy[i];
				
				// 움직일 수 있을 때 까지
				while (true) {
					if (grid[nrx][nry] == '#') {	// 벽
						nrx -= dx[i];
						nry -= dy[i];
						break;
					}
					if (grid[nrx][nry] == 'O') {	// 구멍
						break;
					}
					
					nrx += dx[i];
					nry += dy[i];
					redMove++;
				}
				
				// 파란색
				int nbx = now.bx + dx[i];
				int nby = now.by + dy[i];
				
				// 움직일 수 있을 때 까지
				while (true) {
					if (grid[nbx][nby] == '#') {	// 벽
						nbx -= dx[i];
						nby -= dy[i];
						break;
					}
					if (grid[nbx][nby] == 'O') {	// 구멍
						break;
					}
					
					nbx += dx[i];
					nby += dy[i];
					blueMove++;
				}
				
				if (grid[nbx][nby] == 'O') {	// 파란색이 구멍에 들어갔다면 스킵
					continue;
				}
				
				if (grid[nrx][nry] == 'O') {	// 빨간 구슬만 들어가면 성공
					return now.count;
				}
				
				if (nrx == nbx && nry == nby) {	// 위치가 같으면 안됨
					if (redMove > blueMove) {	// 빨간색이 더 움직였으면 빨간색 후진
						nrx -= dx[i];
						nry -= dy[i];
					} else {
						nbx -= dx[i];
						nby -= dy[i];
					}
				}
				
				if (!visited[nbx][nby][nrx][nry]) {
					visited[nbx][nby][nrx][nry] = true;
					q.add(new Marble(nbx, nby, nrx, nry, now.count+1));
				}
			}
		}
		return -1;
		
	}
	
	static class Marble {
		int bx, by, rx, ry, count;
		
		public Marble(int x1, int y1, int x2, int y2, int c) {
			this.bx = x1;
			this.by = y1;
			this.rx = x2;
			this.ry = y2;
			this.count = c;
		}
	}

}