import java.util.Scanner;
import java.util.Stack;

/**
 * Created by davis on 9/23/14.
 */
public class Calculator {

    public static int parse(String s) throws Exception{
        Stack<String> tmp = new Stack<String>();
        s = s.replaceAll(" +", "");
        while (s.contains("(")){
            int indStaPar = s.indexOf("(");
            int indEndPar = s.indexOf(")", indStaPar);
            s = s.substring(0,indStaPar)+parse(s.substring(indStaPar+1, indEndPar))+s.substring(indEndPar+1);
        }
        Stack<String> toproc = tokenize(s);
        while (toproc.size()>1){
            String cur = toproc.pop();
            if (cur.equals("^")){
                toproc.push((int)Math.pow(Integer.parseInt(tmp.pop()),Integer.parseInt(toproc.pop()))+"");
                continue;
            }
            tmp.push(cur);
        }
        while (!tmp.isEmpty()){
            toproc.push(tmp.pop());
        }
        while (toproc.size()>1){
            String cur = toproc.pop();
            if (cur.equals("*")){
                toproc.push(Integer.parseInt(tmp.pop())*Integer.parseInt(toproc.pop())+"");
                continue;
            }if (cur.equals("/")){
                toproc.push(Integer.parseInt(tmp.pop())/Integer.parseInt(toproc.pop())+"");
                continue;
            }if (cur.equals("%")){
                toproc.push(Integer.parseInt(tmp.pop())%Integer.parseInt(toproc.pop())+"");
                continue;
            }
            tmp.push(cur);
        }
        while (!tmp.isEmpty()){
            toproc.push(tmp.pop());
        }
        while (toproc.size()>1){
            String cur = toproc.pop();
            if (cur.equals("+")){
                toproc.push(Integer.parseInt(tmp.pop())+Integer.parseInt(toproc.pop())+"");
                continue;
            }if (cur.equals("-")){
                toproc.push(Integer.parseInt(tmp.pop())-Integer.parseInt(toproc.pop())+"");
                continue;
            }
            tmp.push(cur);
        }
        if (toproc.size()!=1||tmp.size()!=0){
            throw new Exception();
        }
        return Integer.parseInt(toproc.pop());
    }


    public static Stack<String> tokenize(String s){
        Stack<String> st = new Stack<String>();
        boolean hasChanged=false;
        for (int i = s.length()-2; i >= 0 ; i--) {
            String cur = s.substring(i,i+1);
            if (cur.matches("\\D")){
                st.push(s.substring(i+1));
                st.push(s.substring(i,i+1));
                s = s.substring(0, i);
                hasChanged=true;
            }else if (i == 0){
                st.push(s);
                hasChanged=true;
            }
        }
        if (!hasChanged){
            st.push(s);
        }
        return st;
    }

    public static void main(String[] args) {
        System.out.println("Welcome to the int calculator...");
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.print("Enter an equation:  ");
            String inp = sc.nextLine();
            try {
                int res = parse(inp);
                System.out.println(res);
            }catch (Exception e){
                System.out.println("Error on equation:  "+inp);
            }
        }
    }
}
