import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	static int n, m;
	static int[][] grid;
	static int INF = 1_000_000_000;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		grid = new int[n+1][n+1];
		
//		grid 초기화, 자기 자신을 제외하고는 최댓값으로 갱신
		for (int i=1; i<=n; i++) {
		    for (int j=1; j<=n; j++) {
		        if (i == j) {
		        	grid[i][j] = 0;
		        } else {
		        	grid[i][j] = INF;
		        }
		    }
		}
		
		
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			grid[a][b] = Math.min(grid[a][b], c);
		}
		
//		플로이드 워셜 알고리즘
		for (int k=1; k<=n; k++) {
			for (int i=1; i<=n; i++) {
				for (int j=1; j<=n; j++) {
					grid[i][j] = Math.min(grid[i][j], grid[i][k]+grid[k][j]);
				}
			}
		}
		
//		출력
		for (int i=1; i<=n; i++) {
		    for (int j=1; j<=n; j++) {
		        if (grid[i][j] == INF) grid[i][j] = 0;

		        System.out.print(grid[i][j] + " ");
		    }
		    System.out.println();
		}
	}
}
