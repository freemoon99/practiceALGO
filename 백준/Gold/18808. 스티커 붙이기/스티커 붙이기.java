import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	static int n, m, k, ans=0;
	static int[][] grid, stickers;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		grid = new int[n][m];
		
//		1. 스티커를 모눈 종이에서 떼어냄		
		for (int i=0; i<k; i++) {
			st = new StringTokenizer(br.readLine());
			int row = Integer.parseInt(st.nextToken()), col = Integer.parseInt(st.nextToken());
			
			stickers = new int[row][col];
			
			for (int r=0; r<row; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<col; c++) {
					stickers[r][c] = Integer.parseInt(st.nextToken());
				}
			}
//			2. 범위 내 붙일 수 있는 곳 탐색
			search(stickers);
		}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (grid[i][j] == 1) ans++;
			}
		}
		
		System.out.print(ans);
		
	}
	
	private static void search(int[][] sticker) {
		int r = sticker.length, c = sticker[0].length;
		
//		3. 선택한 위치에 스티커 부착 or 최대 4번 회전
		for (int l=0; l<4; l++) {
			if (l!=0) {
				sticker = rotate(sticker, r, c);
				r = sticker.length;
				c = sticker[0].length;
			}
			
//			범위 안이면 부착
			for (int i=0; i<n; i++) {
				for (int j=0; j<m; j++) {
					if (i+r > n || j+c > m) break;
					if (attach(i, j, r, c, sticker)) return; 
				}
			}
		}
		
	}
	
	private static int[][] rotate(int[][] sticker, int r, int c) {
//		시계 방향으로 90도 회전
		int[][] rotatedSticker = new int[c][r];
		
		for (int i=0; i<r; i++) {
			for (int j=0; j<c; j++) {
				rotatedSticker[j][r-i-1] = sticker[i][j];
			}
		}
		
		return rotatedSticker;
	}
	
	private static boolean attach(int left_r, int left_c, int row, int col, int[][] sticker) {
		for (int i=left_r; i<left_r+row; i++) {
			for (int j=left_c; j<left_c+col; j++) {
				if (grid[i][j] == 1 && sticker[i-left_r][j-left_c] == 1) return false;
			}
		}
		
		for (int i=left_r; i<left_r+row; i++) {
			for (int j=left_c; j<left_c+col; j++) {
				if (sticker[i-left_r][j-left_c] == 1) {
					grid[i][j] = 1;
				}
			}
		}
		
		return true;
	}


}
