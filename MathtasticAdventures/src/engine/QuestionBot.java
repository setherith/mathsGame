package engine;

import domain.Configuration;
import domain.Question;
import java.util.Random;

public class QuestionBot {
    
    private Configuration config;
    
    public QuestionBot() {
        config = new Configuration();
    }
    
    public Question GetQuestion() {
        Question question = new Question();
        
        Random r = new Random();
        int fop = r.nextInt(config.Limit);
        int sop = r.nextInt(config.Limit);
        
        question.Question = String.format("What is %d + %d = ", fop, sop);
        question.Answer = fop + sop;
        
        return question;
    }
}