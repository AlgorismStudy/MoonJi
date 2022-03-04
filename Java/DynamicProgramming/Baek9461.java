import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baek9461 {
    static long[] pado;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int T = Integer.parseInt(s);

        for(int i=0; i<T; i++) {
            s = br.readLine();
            int N = Integer.parseInt(s);
            pado = new long[N+1];
            System.out.println(funcPado(N));
        }


        br.close();
    }
    static long funcPado(int N) {
        for(int i=1; i <= N; i++) {
            if(i == 1 || i == 2 || i == 3) pado[i] = 1L;
            else pado[i] = pado[i-2] + pado[i-3];
        }
        return pado[N];
    }
}
