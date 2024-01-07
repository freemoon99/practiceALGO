import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int max = 0, answer=0;
	static ArrayList<Integer> plusBooks, minusBooks;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        plusBooks = new ArrayList<Integer>();
        minusBooks = new ArrayList<Integer>();
        
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
        	int num = Integer.parseInt(st.nextToken());
        	
        	if (Math.abs(num) > max) {
        		max = Math.abs(num);
        	}
        	
        	if (num>0) {
        		plusBooks.add(num);
        	} else {
        		minusBooks.add(Math.abs(num));
        	}
        }
        
        plusBooks.sort(Comparator.reverseOrder());
        minusBooks.sort(Comparator.reverseOrder());
        
        for (int i=0; i<plusBooks.size(); i++) {
        	if (i%m == 0) {
        		if (plusBooks.get(i) == max) {
        			answer += plusBooks.get(i);
        		} else {
        			answer += (plusBooks.get(i)*2);
        		}
        	}
        }
        
        for (int i=0; i<minusBooks.size(); i++) {
        	if (i%m == 0) {
        		if (minusBooks.get(i) == max) {
        			answer += minusBooks.get(i);
        		} else {
        			answer += (minusBooks.get(i)*2);
        		}
        	}
        }
        
        System.out.print(answer);
    }
   
   
}