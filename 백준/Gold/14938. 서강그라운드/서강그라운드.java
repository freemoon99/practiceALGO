import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m, r, ans = 0;
	static int[] items;
	static int[][] grid;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        
        items = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<n+1; i++) {
        	items[i] = Integer.parseInt(st.nextToken());
        }
        
        grid = new int[n+1][n+1];
        for (int i=0; i<r; i++) {
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	int l = Integer.parseInt(st.nextToken());
        	
        	grid[a][b] = l;
        	grid[b][a] = l;
        }
        
     // 원래 값이 0인 경우, 연결이 없다는 의미이므로 매우 큰 값으로 초기화
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) {
                    continue;
                }
                if (grid[i][j] == 0) {
                    grid[i][j] = 10001;
                }
            }
        }

        // 플로이드 와샬 알고리즘
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (grid[i][j] > grid[i][k] + grid[k][j]) {
                        grid[i][j] = grid[i][k] + grid[k][j];
                    }
                }
            }
        }

        // 거리가 m 이하인 곳에 있는 아이템의 수를 모두 더함
        for (int i = 1; i <= n; i++) {
            int temp = 0;
            for (int j = 1; j <= n; j++) {
                if (grid[i][j] <= m) {
                    temp += items[j];
                }
            }
            ans = Math.max(ans, temp);
        }

        System.out.print(ans);

    }
}
