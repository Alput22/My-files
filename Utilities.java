package Ut;
import java.util.Scanner;
import java.io.*;
public class Utilities {
    //#1
    public int OneTwo() {
        Scanner s = new Scanner(System.in);
        int p = s.nextInt();//input the length of array
        int[] a = new int[p + 1];
        int[] b = new int[p + 1];

        for (int i = 0; i < p; i++) {
            a[i] = s.nextInt();//input the numbers IN the array
        }
        int highest = a[0];

        for (int i = 0; i < p; i++) {
            if (a[i] > highest) {//search the highest value in the array
                highest = a[i];
            }

        }

        int nextHighest = 0;
        for (int k = 0; k < p; k++) {//search the next highest value
            if (a[k] < highest) {
                nextHighest = a[k];
                break;
            }
        }
        for (int i = 0; i < p; i++) {
            if (a[i] > nextHighest && a[i] < highest) {//still searching
                nextHighest = a[i];
            }
        }
        int x = highest;//storing the values
        int y = highest - nextHighest;
        int z = nextHighest;

        for (int i = 0; i < p + 1; i++) {
            int z1 = p;
            if (a[i] != x) {
                System.out.print(a[i] + " ");
            } else {
                a[i] = z;
                System.out.print(a[i] + " ");
                while (z1 > i) {
                    a[z1] = a[z1 - 1];
                    z1--;
                }
                a[i + 1] = y;
                System.out.print(a[i + 1] + " ");
                i++;
            }
        }
        return 0;
    }

    //#2
    public int MoveRight(int[] arr, int d, int n) { //rotate arr[] of size n by d
        for (int i = n - 1; i > d; i--) {
            int temp;
            temp = arr[n - 1];
            for (i = n - 1; i > 0; i--)
                arr[i] = arr[i - 1];
            arr[i] = temp;//for some reason only move by 1
        }
        for (int i = 0; i < n; i++) {//printing the array
            System.out.print(arr[i] + " ");
        }
        return 0;
    }

    public int multiMat(int mat[][],int N) {
        int MAX = 100;

        // Returns true if mat[N][N] is symmetric, else false
        int tra[][] = new int[N][MAX];
        for (int i = 0; i < N; i++) {// Fills transpose of mat[N][N] in tr[N][N]
            for (int j = 0; j < N; j++) {
                tra[i][j] = mat[j][i];
            }
        }boolean x;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (mat[i][j] != tra[i][j]) {
                 x = false;
                }
            }
            x = true;
            if (x ==true) {
                System.out.println("Yes");
            } else {
                System.out.println("No");// I think there's something wrong with the code
            }
        }
    return 0;
    }

        // Function to generate odd sized magic squares
        public int Square(int n){
            int[][] magicS = new int[n][n];

            // Initialize position for 1
            int i = n/2;
            int j = n-1;

            // One by one put all values in magic square
            for (int num=1; num <= n*n; )
            {
                if (i==-1 && j==n) //3rd condition
                {
                    j = n-2;
                    i = 0;
                }
                else
                {
                    //1st condition helper if next number
                    // goes to out of square's right side
                    if (j == n)
                        j = 0;

                    //1st condition helper if next number is
                    // goes to out of square's upper side
                    if (i < 0)
                        i=n-1;
                }

                //2nd condition
                if (magicS[i][j] != 0){
                    j -= 2;
                    i++;
                    continue;
                }
                else {
                    //set number
                    magicS[i][j] = num++;
                }
                //1st condition
                j++;  i--;
            }

            // print magic square
            System.out.println("The Magic Square for "+n+":");
            System.out.println("Sum of each row or column "+n*(n*n+1)/2+":");
            for(i=0; i<n; i++)
            {
                for(j=0; j<n; j++)
                    System.out.print(magicS[i][j]+" ");
                System.out.println();
            }
        return 0;}


}



