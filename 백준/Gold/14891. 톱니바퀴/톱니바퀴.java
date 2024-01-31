import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int k;
	static int[][] gear;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        gear = new int[4][8];
        
        // 처음 톱니 입력 받기
        for (int i=0; i< 4; i++) {
        	String input = br.readLine();
        	for (int j=0; j<8; j++) {
        		gear[i][j] = input.charAt(j)-'0';
        	}
        }
        
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        // k번 회전
        for (int i=0; i<k; i++) {
        	st = new StringTokenizer(br.readLine());
        	int gearNum = Integer.parseInt(st.nextToken())-1;
        	int direction = Integer.parseInt(st.nextToken());
        	
        	compareToGear(gearNum, direction);
        }
        
        // 모든 기어의 0번 인덱스 더하기
        int result = 0;
        for (int i=0; i<4; i++) {
        	result += Math.pow(2, i)*gear[i][0];
        }
        System.out.print(result);
        
    }
    private static void rotate(int idx, int d) {
    	if (d == 1) {
    		int temp = gear[idx][7];
    		for (int i=7; i>0; i--) {
    			gear[idx][i] = gear[idx][i-1];
    		}
    		gear[idx][0] = temp;
    	} else {
    		int temp = gear[idx][0];
    		for (int i=0; i<7; i++) {
    			gear[idx][i] = gear[idx][i+1];
    		}
    		gear[idx][7] = temp;
    	}
    }
    private static void compareToGear(int n, int d) {
        int[] direction = new int[4];
        direction[n] = d;

        // 오른쪽 톱니바퀴 검사
        for (int i = n; i < 3; i++) {
            if (gear[i][2] != gear[i + 1][6]) {
                direction[i + 1] = -direction[i];
            } else {
                break;
            }
        }

        // 왼쪽 톱니바퀴 검사
        for (int i = n; i > 0; i--) {
            if (gear[i][6] != gear[i - 1][2]) {
                direction[i - 1] = -direction[i];
            } else {
                break;
            }
        }

        // 톱니바퀴 회전
        for (int i = 0; i < 4; i++) {
            if (direction[i] != 0) {
                rotate(i, direction[i]);
            }
        }
    }    
}