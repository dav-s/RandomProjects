import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


/**
 * Contains methods to simplify reading timed input.
 * @author Davis Robertson
 * @version 1.0
 */
public class DavisTimeScanner {

    private static Thread t;
    private static String ans;

    private static void resetScanner(){
        ans=null;
        t = new Thread(new Runnable() {
            @Override
            public void run() {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                while (ans==null){
                    try {
                        while (!br.ready()){
                            Thread.sleep(200);
                        }
                        ans=br.readLine();
                    }catch (InterruptedException e){
                        return;
                    } catch (IOException e) {
                        System.err.println("An unexpected error has occurred.");
                        return;
                    }
                }
            }
        });
    }

    /**
     * Waits a specified amount of time for an String input.
     * @param seconds the number of seconds to wait for input
     * @return null if no input is provided, otherwise returns the input
     * @throws InterruptedException if sleep is interrupted
     */
    public static String getLine(int seconds) throws InterruptedException {
        resetScanner();
        t.start();
        for (int i = 0; i < seconds*2; i++) {
            Thread.sleep(500);
            if (ans!=null){
                break;
            }
        }
        t.interrupt();
        return ans;
    }

    /**
     * Calls getLine(int seconds) but catching the InterruptedException.
     * @param seconds the number of seconds to wait for input
     * @return null if no input is provided or call is interrupted, otherwise returns the input
     * @see #getLine(int)
     */
    public static String getLineNoThrow(int seconds){
        try {
            return getLine(seconds);
        }catch (InterruptedException e){
            return null;
        }
    }

}