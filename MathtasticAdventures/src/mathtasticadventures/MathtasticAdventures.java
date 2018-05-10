package mathtasticadventures;

import domain.Player;
import domain.Question;
import engine.QuestionBot;
import java.util.Scanner;

/**
 * @author setherith
 */
public class MathtasticAdventures {

    private QuestionBot Qbot;
    
    public static void main(String[] args) {
        MathtasticAdventures game = new MathtasticAdventures();
    }
    
    public MathtasticAdventures() {
        String name = AskQuestion("Enter your name: ");
        System.out.println("Hello " + name);
        
        // check user against register
        Player player = new Player();
        player.Name = name;
        
        // load config if exists
        
        Qbot = new QuestionBot();
        
        String play = AskQuestion("Would you like to play a game? ");
        if (play.equals("yes")) {
            for (int i = 0; i < 10; i++) {
                Question question = Qbot.GetQuestion();
                String answer = AskQuestion(question.Question);
                int ans = Integer.parseInt(answer);
                if (ans == question.Answer) {
                    // correct
                    player.Score++;
                } else {
                    // false
                }
            }
        }
    }
    
    private String AskQuestion(String question) {
        String result = "";
        Scanner reader = new Scanner(System.in);
        System.out.println(question);
        
        while (result.length() == 0) {
            result = reader.hasNext() ? reader.nextLine() : "";
        }
        
        return result;
    }
}
