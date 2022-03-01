import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1072 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        long X = Integer.parseInt(s[0]);
        long Y = Integer.parseInt(s[1]);
        long Z = Y * 100 / X ;

        long start = 1;
        long end = X;

        while(start <= end) {
            long mid = (start + end) / 2;
            long newZ = (Y + mid) * 100 / (X + mid);

            if(newZ > Z) end = mid - 1;
            else start = mid + 1;
        }

        if (Z >= 99) System.out.print(-1);
        else System.out.print(start);
        br.close();
    }
}
