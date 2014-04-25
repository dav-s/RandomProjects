public class Demo {

    public static void main(String[] args) throws InterruptedException{
        System.out.println("Please enter an input within the next 10 seconds.");//Prompt user to input data

        String str = DavisTimeScanner.getLine(10); //Specify seconds to wait and get input
        /*
        NOTE:This method can throw an InterruptedException and needs to be handled.
             If some people do not want to deal with exceptions, I have provided an alternate method,
                'DavisTimeScanner.getLineNoThrow(seconds)', that silently catches the error.
         */

        //Here we are checking/handling if an answer was provided
        if (str==null){
            System.out.println("No input was provided");
        }else{
            System.out.println("The input is: "+str);
        }



    }

}