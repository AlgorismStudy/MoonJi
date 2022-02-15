import java.util.Scanner;
import java.util.Arrays;
public class Baek2217 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] w = new int[N];

        for(int i=0; i < N; i++) {
            w[i] = sc.nextInt();
        }

        Arrays.sort(w);
        int result = 0;
        for(int i=0; i < N; i++) {
            int tmp = w[i] * (N - i);
            if (tmp > result) result = tmp;
        }

        System.out.println(result);
    }

}
