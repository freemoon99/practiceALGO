import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int t, maxValue = 1299709;
	static boolean[] prime;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        t = Integer.parseInt(br.readLine());
        isPrime();
        
        for (int i=0; i<t; i++) {
        	int k = Integer.parseInt(br.readLine());
        	
        	if (prime[k]) {
        		System.out.println(0);
        	} else {
            	int[] foundValues = find(k);
            	int result = foundValues[1] - foundValues[0];
            	System.out.println(result);
        	}
        	
        }
        
    }
    
    private static int[] find(int x) {
    	int smallValue = 0;
    	int bigValue = 0;

    	for (int i = x; i>=0; i--) {
    		if (prime[i]) {
    			smallValue = i;
    			break;
    		}
    	}
    	
    	for (int j=x; j<maxValue; j++) {
    		if (prime[j]) {
    			bigValue = j;
    			break;
    		}
    	}

    	return new int[] {smallValue, bigValue};
    }
    
    private static void isPrime() {
    	prime = new boolean[maxValue+1];
    	
    	for (int i=0; i<maxValue+1; i++) {
    		prime[i] = true;
    	}
    	
    	prime[0] = prime[1] = false;
    	
    	for (int i=2; i<=Math.sqrt(maxValue); i++) {
    		if (prime[i]) {
    			for (int j=i*i; j<maxValue+1; j+=i) {
    				prime[j] = false;
    			}
    		}
    	}
    	
    }
}