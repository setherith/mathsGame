package tests;

import domain.Configuration;
import domain.Question;
import engine.QuestionBot;
import org.junit.BeforeClass;
import org.junit.Test;

public class UnitTests {
    
    private static QuestionBot QBot;
    private static Configuration config;
    
    @BeforeClass
    public static void Init() {
        QBot = new QuestionBot();
        config = new Configuration();
    }
    
    @Test
    public void GetAQuestion() {
        Question result = QBot.GetQuestion();
        System.out.println(result.Question);
        assert(result != null);
        assert(result.Question.length() > 0);
    }
    
    @Test
    public void SetGetConfiguration() {
        config.Operations = 0b1111;
        assert(config.Addition());
        assert(config.Division());
        assert(config.Multiplication());
        assert(config.Subtraction());
        config.Operations = 0;
        assert(!config.Addition());
        assert(!config.Division());
        assert(!config.Multiplication());
        assert(!config.Subtraction());
    }
}