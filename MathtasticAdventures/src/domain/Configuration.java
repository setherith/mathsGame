package domain;

/**
 * @author setherith
 */
public class Configuration {
    
    public byte Operations;
    public int Limit;
    
    public Configuration() {
        if (!LoadConfiguration()) {
            UseDefaults();
        }
    }

    private void UseDefaults() {
        System.out.println("Using default values");
        Operations = (byte) 1;
        Limit = 12;
    }
    
    private boolean LoadConfiguration() {
        System.out.println("Load Configuration [incomplete]");
        return false;
    }
    
    private boolean SaveConfiguration() {
        System.out.println("Save Configuration [incomplete]");
        return false;
    }
}
