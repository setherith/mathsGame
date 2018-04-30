package domain;

public class Player {
    public String Name;
    public int Score;
    public double AverageScore;
    public double AvgTime;
    
    public Player() {
        Load();
    }
    
    public void Load() {
        System.out.println("Loading Player...[incomplete]");
    }
    
    public void Save() {
        System.out.println("Saving Player...[incomplete]");
    }
}
