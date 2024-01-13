import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static char[][] grid;
	static boolean[][] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int answer = 0;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        grid = new char[12][6];
        
        for (int i=0; i<12; i++) {
        	String  s= br.readLine();
        	for (int j=0; j<6; j++) {
        		grid[i][j] = s.charAt(j);
        	}
        }
        
        while (true) {
        	boolean isFinished = true;
        	visited = new boolean[12][6];
        	
        	
        	for (int i=0; i<12; i++) {
            	for (int j=0; j<6; j++) {
            		if (grid[i][j] != '.' && !visited[i][j]) {
            			if(bfs(i, j)) {
            				isFinished = false;
            			}
            		}
            	}
            }
            if (isFinished) break;
        	answer ++;
        	
        	
        	
        }
        
        System.out.print(answer);
    }
    
    private static boolean bfs(int x, int y) {
    	ArrayList<Pair> lst = new ArrayList<>();
    	int cnt = 1;
    	boolean isDestroy = false;
    	
    	Queue<Pair> q = new LinkedList<>();
    	q.offer(new Pair(x, y));
    	lst.add(new Pair(x, y));
    	visited[x][y] = true;
    	
    	while (!q.isEmpty()) {
    		Pair now = q.poll();
    		
    		for (int i=0; i<4; i++) {
    			int nx = now.x+dx[i];
    			int ny = now.y+dy[i];
    			
    			if (0<=nx && nx<12 && 0<=ny && ny<6) {
    				if (!visited[nx][ny] && grid[nx][ny] == grid[x][y]) {
    					visited[nx][ny] = true;
    					q.offer(new Pair(nx, ny));
    					lst.add(new Pair(nx, ny));
    					cnt ++;
    				}
    			}
    		}
    	}
    	
    	if (cnt >= 4) isDestroy = true;
    	
    	if (isDestroy) {
    		// 1. 파괴
    		destroy(lst);
    		// 2. 내리기
        	down();
    	}
    	
    	return isDestroy;
    }
    
    private static void destroy(ArrayList<Pair> lst) {
    	for (Pair now : lst) {
    		grid[now.x][now.y] = '.';
    	}
    	
    }
    
    private static void down() {    	
    	for (int j=0; j<6; j++) {
        	for (int i=11; i>=0; i--) {
        		if (grid[i][j] == '.') {
        			for (int k = i-1; k>=0; k--) {
        				if (grid[k][j] != '.') {
        					grid[i][j] = grid[k][j];
        					grid[k][j] = '.';
        					break;
        				}
        			}
        		}
        		
        	}
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