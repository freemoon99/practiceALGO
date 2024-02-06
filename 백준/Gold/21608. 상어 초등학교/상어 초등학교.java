import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] order;
	static int[][] like, seats;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
    	n = Integer.parseInt(br.readLine());
    	order = new int[n*n];
    	like = new int[n*n+1][4];
    	seats = new int[n*n][n*n];
        
    	for (int i=0; i<n*n; i++) {
    		String[] str = br.readLine().split(" ");
    		int row = Integer.parseInt(str[0]);
    		order[i] = row;
    		int col = 1;
    		for (int j=0; j<4; j++) {
    			like[row][j] = Integer.parseInt(str[col++]);
    		}
    	}
    	
    	// 다중정렬을 이용한 자리 앉히기
    	sitting();
    	
    	// 점수 계산
    	int sum = 0;
    	for (int i=0; i<n; i++) {
    		for (int j=0; j<n; j++) {
    			int now = seats[i][j];
    			int likeCnt = 0;
    			
    			for (int d=0; d<4; d++) {
    				int nx = i+dx[d];
    				int ny = j+dy[d];
    				
    				if (0<=nx && nx<n && 0<=ny && ny<n) {
						for (int l : like[now]) {
							if (seats[nx][ny] == l) {
								likeCnt++;
							}
						}
    				}
    			}
    			if (likeCnt != 0) {
    			    sum += Math.pow(10 ,likeCnt-1);
    			}
    		}
    	}
    	
    	System.out.print(sum);
    }
    
    private static void sitting() {
    	for (int now : order) {
    		List<int[]> state = new ArrayList<>();
    		
    		for (int i=0; i<n; i++) {
    			for (int j=0; j<n; j++) {
    				if (seats[i][j] == 0) {
    					int likeCnt = 0;
    					int emptyCnt = 0;
    					
    					for (int d=0; d<4; d++) {
    						int nx = i+dx[d];
    	    				int ny = j+dy[d];
    						
    						if (0<=nx && nx<n && 0<=ny && ny<n) {
    							for (int l : like[now]) {
    								if (seats[nx][ny] == l) {
    									likeCnt++;
    								}
    							}
    							if(seats[nx][ny] == 0) {
    								emptyCnt++;
    							}
    						}
    					}
    					state.add(new int[]{likeCnt, emptyCnt, i, j});
    				}
    			}
    		}
    		
    		state.sort((o1, o2) -> {
    		    if (o1[0] != o2[0]) return o2[0] - o1[0]; // 좋아하는 학생수 내림차순
    		    else if (o1[1] != o2[1]) return o2[1] - o1[1]; // 인접한 칸수 내림차순
    		    else if (o1[2] != o2[2]) return o1[2] - o2[2]; // 행 오름차순
    		    else return o1[3] - o2[3]; // 열 오름차순
    		});

    		
    		seats[state.get(0)[2]][state.get(0)[3]] = now;
    	}
    }
}