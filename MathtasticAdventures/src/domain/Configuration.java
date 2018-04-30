package domain;

import java.io.Serializable;

/**
 * @author setherith
 */
public class Configuration implements Serializable {
    
    public byte Operations;
    public int Limit;
    
    public Configuration() {
        if (!LoadConfiguration()) {
            UseDefaults();
        }
    }

    private void UseDefaults() {
        System.out.println("Using default values");
        Operations = 0b1; // set only addition questions
        Limit = 12; // up to a max. of 12
    }
    
    private boolean LoadConfiguration() {
        System.out.println("Load Configuration [incomplete]");
        return false;
    }
    
    private boolean SaveConfiguration() {
        System.out.println("Save Configuration [incomplete]");
        return false;
    }
    
    private boolean Shifter(int position) {
        return (Operations >> position & 1) == 1;
    }
    
    public boolean Addition() {
        return Shifter(0);
    }
    
    public boolean Subtraction() {
        return Shifter(1);
    }
    
    public boolean Division() {
        return Shifter(2);
    }
    
    public boolean Multiplication() {
        return Shifter(3);
    }
}
