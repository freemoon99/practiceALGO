import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int a, b, ans = 0;
	static ArrayList<Integer>[] primeNumbers;
	static boolean[] prime;
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
    	
        primeNumbers = new ArrayList[b+1];
    	
    	for (int i=0; i<=b; i++) {
        	primeNumbers[i] = new ArrayList<>();
        }
    	
        isPrime(b);
        
        for (int i=a;i<=b;i++) {
        	factorization(i);
        }
        
        for (int i=a; i<=b; i++) {
        	int s = primeNumbers[i].size();
        	if (prime[s]) {
        		ans ++;
        	}
        }
        
        System.out.print(ans);
        
    }
    
    private static void factorization(int num) {
    	int temp = num;
    	for (int i=2; i<=Math.sqrt(num); i++) {
    		while (temp % i == 0) {
    			if (prime[i]) {
    				primeNumbers[num].add(i);
    			}
    			temp/=i;
    		}
    	}
    	if (temp > 1 && prime[temp]) primeNumbers[num].add(temp);
    }
    
    private static void isPrime(int x) {
    	prime = new boolean[b+1];
    	
    	for (int i=0; i<=b; i++) {
    		prime[i] = true;
    	}
    	
    	prime[0] = prime[1] = false;
    	
    	for (int i=2; i<=Math.sqrt(b);i++) {
    		if (prime[i]) {
    			for (int j=i*i; j<=b; j+=i) {
    				prime[j] = false;
    			}
    		}
    	}
    }
}
