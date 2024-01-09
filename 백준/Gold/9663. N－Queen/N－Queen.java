import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int n, cnt = 0;
	static int[] grid;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        grid = new int[n];
        
        backtracking(0);
        System.out.print(cnt);
    }
    
    private static void backtracking(int row) {
    	if (row == n) {
    		cnt ++;
    		return;
    	}
    	
    	for (int i=0; i<n; i++) {
    		grid[row] = i;
    		if (isPossible(row)) {
    			backtracking(row+1);
    		}
    	}
    	
    }
    
    private static boolean isPossible(int col) {
    	for (int i=0; i<col; i++) {
//    		행과 열이 같은 경우
    		if (grid[i] == grid[col]) {
    			return false;
    		}
//    		대각선 상에 놓이는 경우
    		else if (Math.abs(col-i) == Math.abs(grid[col]-grid[i])) {
    			return false;
    		}
    	}
    	return true;
    }
   
   
}