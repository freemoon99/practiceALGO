import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int n;
	static char[][] grid;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        n = Integer.parseInt(br.readLine());
        grid = new char[n][n];
        
        for (char[] row : grid) {
            Arrays.fill(row, '*');
        }
        
        recursion(0,0,n,false);
        
        for (int i=0; i<n; i++) {
        	for (int j=0; j<n; j++) {
        		sb.append(grid[i][j]);
        	}
        	sb.append('\n');
        }
        System.out.print(sb);
        
    }
    
    private static void recursion(int startX, int startY, int leng, boolean empty) {
//    	비우기
    	if (empty) {
    		for (int i=startX; i<startX+leng; i++) {
        		for (int j=startY; j<startY+leng; j++) {
        			grid[i][j] = ' ';
        		}
    		}
    	}
    	
//    	재귀 종료
    	if (leng == 1) return;
    	
    	int size = leng/3;
    	int number = 0;
    	
    	for (int i=startX; i<startX+leng; i+=size) {
    		for (int j=startY; j<startY+leng; j+=size) {
    			number ++;
    			
    			if (number == 5) {
    				recursion(i, j, size, true);
    			} else {
    				recursion(i, j, size, false);
    			}
    		}
    	}
    	
    	
    }
   
}