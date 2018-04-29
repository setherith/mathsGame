package tests;

import domain.Question;
import engine.QuestionBot;
import org.junit.BeforeClass;
import org.junit.Test;

public class UnitTests {
    
    private static QuestionBot QBot;
    
    @BeforeClass
    public static void Init() {
        QBot = new QuestionBot();
    }
    
    @Test
    public void GetAQuestion() {
        Question result = QBot.GetQuestion();
        System.out.println(result.Question);
        assert(result != null);
        assert(result.Question.length() > 0);
    }
    
    @Test
    public void ReadConfiguration() {
        byte test = 0b1010;
        
        assert(test >> 1 == 1);
        assert(test >> 2 == 0);
    }
}