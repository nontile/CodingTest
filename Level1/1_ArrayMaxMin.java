import java.util.Arrays;

/**
  배열의 최대값, 최소값, 중간값을 구하라  
*/ 
class ArrayMaxMin {
    public static void main(String args[]){
        int[] arr = {1, 9, 12, 5, 2};
        Arrays.sort(arr);
        System.out.println("Max: " + arr[arr.length -1]);
        System.out.println("Min: " + arr[0]);
        System.out.println("Mid: " + arr[arr.length/2]);
    }
}