import java.time.LocalDateTime;
public class TransactionHistory {
    private String action;
    private double amount;
    private LocalDateTime date;

    public TransactionHistory(String action, double amount, LocalDateTime date){
        this.action = action;
        this.amount = amount;
        this.date = date;
    }

    public String printStatement(){
            return "[" +date+ "]" + " "+action+  " - Rs."+amount;

    }
}


