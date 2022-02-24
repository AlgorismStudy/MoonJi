import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Baek2110 {
    static int[] house;
    static int N, C;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);

        house = new int[N];
        for(int i=0; i<N; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(house);
        int start = 1;
        int end = house[N-1];
        int max_d = 0;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(cal_distance(mid)) {
                if(mid > max_d) max_d = mid;
                start = mid + 1;
            }
            else end = mid - 1;
        }

        System.out.println(max_d);
        br.close();
    }

    static boolean cal_distance(int mid) {
        List<Integer> wifi = new ArrayList<>();
        wifi.add(0);
        int d = 0;
        for(int i=1; i<N; i++) {
            d += house[i] - house[i-1];
            if(d >= mid) {
                wifi.add(i);
                d = 0;
            }
        }
        if(wifi.size() >= C) return true;
        else return false;
    }
}
