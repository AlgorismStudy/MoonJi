import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baek1003 {
    static int[][] fibo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int T = Integer.parseInt(s);

        for(int i=0; i<T; i++) {
            s = br.readLine();
            int N = Integer.parseInt(s);
            fibo = new int[N+1][2];
            func_fibo(N);
            System.out.println(fibo[N][0] + " " + fibo[N][1]);
        }


        br.close();
    }

    static void func_fibo(int N) {
        for(int i=0; i<= N; i++) {
            if(i == 0) {
                fibo[i][0] = 1;
                fibo[i][1] = 0;
            } else if(i == 1) {
                fibo[i][0] = 0;
                fibo[i][1] = 1;
            } else {
                fibo[i][0] = fibo[i-1][0] + fibo[i-2][0];
                fibo[i][1] = fibo[i-1][1] + fibo[i-2][1];
            }
        }
    }
}
