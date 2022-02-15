import java.util.Scanner;

public class Baek1541 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] arr = str.split("-");

        int result = 0;
        for(int i=0; i < arr.length; i++) {
            String[] num = arr[i].split("\\+");
            int tmp = 0;
            for(int j=0; j < num.length; j++) {
                tmp += Integer.parseInt(num[j]);
            }
            if(i == 0) result += tmp;
            else result -= tmp;
        }
        System.out.println(result);
    }
}