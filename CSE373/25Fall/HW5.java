public class HW5 {
    public static void main(String[] args) {
        run("watch the movie raising arizona?", "watch da mets raze arizona?");
        run("this is what happens when I type slow", "htishisth whaty havpens when ui type fasht");
        run("leonard skiena", "lynard skynard");
    }

    public static void run(String a, String b) {
        int n = a.length();
        int m = b.length();
        int[][] d = new int[n + 1][m + 1];

        for (int i = 0; i <= n; i++) d[i][0] = i;
        for (int j = 0; j <= m; j++) d[0][j] = j;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int same = (a.charAt(i - 1) == b.charAt(j - 1)) ? 0 : 1;
                int min = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1);
                d[i][j] = Math.min(min, d[i - 1][j - 1] + same);
            }
        }

        String outA = "";
        String outB = "";
        int i = n, j = m;

        while (i > 0 || j > 0) {
            int same = (i > 0 && j > 0 && a.charAt(i - 1) == b.charAt(j - 1)) ? 0 : 1;
            
            if (i > 0 && j > 0 && d[i][j] == d[i - 1][j - 1] + same) {
                outA = a.charAt(i - 1) + outA;
                outB = b.charAt(j - 1) + outB;
                i--; j--;
            } else if (i > 0 && d[i][j] == d[i - 1][j] + 1) {
                outA = a.charAt(i - 1) + outA;
                outB = "-" + outB;
                i--;
            } else {
                outA = "-" + outA;
                outB = b.charAt(j - 1) + outB;
                j--;
            }
        }

        System.out.println(outA);
        System.out.println(outB);
        System.out.println(d[n][m]);
        System.out.println();
    }
}