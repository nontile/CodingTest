import java.util.Arrays;
class Test {
   public static void main(String[] arg){

       int[] arr = {5, 3, 1,1,3}; 
       int[] dp = new int[arr.length +1];
       
       Arrays.sort(arr);

    //    dp[0] = arr[0]
    //    int k =2;
       for(int i =0; i<arr.length + 1 ; i++){
           if(i+1 < arr.length){

             dp[i] = arr[i +1] - arr[i];
           }
         System.out.println(dp[i]);
       }

       Arrays.sort(dp);
        for(int i =dp.length; i>0 ; i--){
           
         System.out.println(dp[i]);
       }


   }
}
