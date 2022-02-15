import java.util.Scanner;
public class Baek5585 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int change = 1000 - sc.nextInt();

        int[] coins = {500, 100, 50, 10, 5, 1};
        int count = 0;

        for(int i=0; i < coins.length ; i++) {
            if (change >= coins[i]) {
                count += (change / coins[i]);
                change %= coins[i];
            }
            if (change == 0) break;
        }
        System.out.println(count);
    }
}