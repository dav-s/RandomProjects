/**
 * @author Davis Robertson
 */

public class FullAdder {

    public static void main(String[] args) {
        System.out.printf("%d + %d = %d%n", 9, 5, fullAdderRecursive(9, 5));
        System.out.printf("%s + %s = %s%n", Integer.toBinaryString(9),
                                            Integer.toBinaryString(5),
                                            Integer.toBinaryString(fullAdderRecursive(9, 5)));
    }


    /**
     * Calls fullAdderRecursive(int x, int y, int carryin) with carrying being default 0.
     * @param x first number to add
     * @param y second number to add
     * @return sum of x and y
     */
    public static int fullAdderRecursive(int x, int y){
        return fullAdderRecursive(x, y, 0);
    }

    /**
     * Recursively calculates the sum of two numbers using a full adder paradigm.
     * @param x remaining first number to add
     * @param y remaining second number to add
     * @param carryin the carry-in (default should be 0)
     * @return sum of x and y and carryin
     */
    public static int fullAdderRecursive(int x, int y, int carryin){
        if (x==0 && y==0){   // Base Case: Checks if x and y are both zero
            return carryin;  // It returns the carry-in, if the above is true
        }
        // Takes the last bit of x and y respectively
        // EX: Base 10: 23 % 2 = 1
        //     Base 2: 10111's last bit is 1
        int a = x % 2;
        int b = y % 2;

        // Finds the sum of the current adder according to the logic gate diagram
        // ^ == XOR in Java
        int sum = a ^ b ^ carryin;

        // Calculates the carry-out for the current adder according to the logic-gate diagram
        // & == AND and | == OR in Java
        int carryout = (a ^ b) & carryin | a & b;

        // Here is the recursive call.
        // The sum is the resultant sum of the current adder (the result of the adder on the last bits of each x and y).
        // x and y are divided by 2 in order to eliminate the last bits (a and b).
        // The carry-out of the current adder becomes the carry-in of the next adder.
        // The result of the recursive call is shifted over in order to retain place values.
        // EX: fAR()==fullAdderRecursive())
        //   fAR(9,5,0) We want to add 9 and 5 (BINARY: 1001 + 0101) = 14
        //      a = 1, b = 1, carryin = 0
        //      sum = 1 ^ 1 ^ 0 = 0
        //      carryout = (1 ^ 1) & 0 | 1 & 1 = 1 (REMEMBER: Order of Operations apply here)
        //      return 0 + (fAR(4,2,1)<<1) = 0 + (7<<1) = 0 + 14 = 14
        //         fAR(4,2,1) = 7
        //            a = 0, b = 0, carryin = 1
        //            sum = 0 ^ 0 ^ 1 = 1
        //            carryout = (0 ^ 0) & 1 | 0 & 0 = 0
        //            return 1 + (fAR(2,1,0)<<1) = 1 + (3<<1) = 1 + 6 = 7
        //               fAR(2,1,0) = 3
        //                  a = 0, b = 1, carryin = 0
        //                  sum = 0 ^ 1 ^ 0 = 1
        //                  carryout = (0 ^ 1) & 0 | 0 & 1 = 0
        //                  return 1 + (fAR(1,0,0)<<1) = 1 + (1<<1) = 1 + 2 = 3
        //                     fAR(1,0,0) = 1
        //                        a = 1, b = 0, carryin = 0
        //                        sum = 1 ^ 0 ^ 0 = 1
        //                        carryout = (1 ^ 0) & 0 | 1 & 0 = 0
        //                        return 1 + (fAR(0,0,0)<<1) = 1+(0<<1) = 1 (Alternatively, you can use *2 instead of <<1)
        //                           fAR(0,0,0) = 0
        //                              x and y are 0. Return 0.
        return sum +(fullAdderRecursive(x/2, y/2, carryout) << 1);
    }
}
