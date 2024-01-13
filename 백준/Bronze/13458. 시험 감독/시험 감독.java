import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, b, c;
    static long answer = 0;
	static int[] a;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        n = Integer.parseInt(br.readLine());
        a = new int[n];
        
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
        	a[i] = Integer.parseInt(st.nextToken());
        }
        
        st = new StringTokenizer(br.readLine());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        for (int i=0; i<n; i++) {
        	int students = a[i];
        	
        	int remain = students - b;
        	answer ++;
        	
        	if (remain > 0) {
        		answer += remain/c;
        		if (remain%c != 0) {
        			answer++;
        		}
        	}
        	
        }
        System.out.print(answer);
        
    }

}