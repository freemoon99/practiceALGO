import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n, k, cnt = 0;
	static int[] a, robot;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        a = new int[2*n];
        robot = new int[n];
        
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<2*n; i++) {
        	a[i] = Integer.parseInt(st.nextToken());
        }
        
        move();
    }
    
    private static boolean isFinished() {
    	int count = 0;
    	for (int i=0; i<a.length; i++) {
    		if (a[i] == 0) {
    			count++;
    		}
    	}
    	
    	return count >= k;
    }
    
    private static void rotate(int[] arr) {
    	int temp = arr[arr.length-1];
    	for (int i=arr.length-1; i>0; i--) {
    		arr[i] = arr[i-1];
    	}
    	arr[0] = temp;
    }
    
    private static boolean isRobot() {
    	int count = 0;
    	for (int i=0; i<n; i++) {
    		if (robot[i] == 1) {
    			count++;
    		}
    	}
    	
    	return count > 0;
    }
    
    private static void move() {
    	while (true) {
    		// 종료 조건 : 내구도가 0인 칸 k개 이상
    		if (isFinished()) {
    			System.out.print(cnt);
    			break;
    		}
    		
    		// 벨트, 로봇 회전
    		rotate(a);
    		rotate(robot);
    		
        	// 로봇 이동
    		robot[n-1] = 0;	// 로봇 내리기
    		
    		if (isRobot()){	// 내리는 위치 제외
    			for (int i=n-2; i>=0; i--) {
    				// 로봇이 존재하고, 다음 칸에 이동할 수 있으면 (내구도, 로봇 존재)
    				if (robot[i] == 1 && robot[i+1] == 0 && a[i+1] > 0) {
    					robot[i+1] = 1;
    					robot[i] = 0;
    					a[i+1]--;
    				}
    			}
    			robot[n-1] = 0;	// 로봇 내리기
    		}
    		
        	// 시작점 로봇 올리기
    		if (robot[0] == 0 && a[0] > 0) {
    			robot[0] = 1;
    			a[0]--;
    		}
    		
    		cnt++;
    	}
    	
    }
}