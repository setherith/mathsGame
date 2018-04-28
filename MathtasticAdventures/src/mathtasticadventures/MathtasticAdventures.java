package mathtasticadventures;

import java.util.Scanner;

/**
 * @author setherith
 */
public class MathtasticAdventures {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter your name: ");
        String name = reader.next();
        System.out.println("Hello " + name);
        reader.close();
    }
    
}
