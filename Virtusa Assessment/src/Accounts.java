import java.util.ArrayList;
import java.time.LocalDateTime;
public abstract class Accounts {
    private String account_num;
    private String name;
    private double balance;
    private String username;
    private String password;
    private ArrayList<TransactionHistory> history = new ArrayList<>();

    public Accounts(String account_num, String name, double init_balance, String username, String password) {
        this.account_num = account_num;
        this.name = name;
        this.balance = init_balance;
        this.username = username;
        this.password = password;
    }

    public String getAccount_num() {
        return account_num;
    }
    public String getName() {
        return name;
    }
    public double getBalance() {
        return balance;
    }
    public String getUsername(){
        return username;
    }
    public String getPassword() {
        return password;
    }
    public void deposit(double amount){
      if(amount <= 0){
          System.out.print("Amount should be greater than Rs.0 !");
          return;
      }
      this.balance += amount;
      System.out.println("Amount added to your acc : Rs." +amount);
      addTransaction("Deposit" , amount);
    }
    public void withdraw(double amount){
        if(amount <= 0){
            System.out.println("Amount should be greater than Rs.0 !");

        }else if(this.balance < amount){
            System.out.println("Insufficent Balance!");

        }else{
            this.balance -= amount;
            System.out.println("Amount taken from your acc: Rs."+amount);
            addTransaction("Withdraw" , amount);

        }
    }
    public void transfer(Accounts otherAccount, double amount){
        if(amount <= 0){
            System.out.println("Amount should be greater than Rs.0 !");

        }else if(amount > this.balance){
            System.out.println("Insufficinet balance");

        }else {
            withdraw(amount);
            otherAccount.deposit(amount);
            System.out.println("Rs." + amount + " transferred to " +otherAccount.getName() +" Successfully!");
            addTransaction("Transfer to "+ otherAccount.getName(), amount);
        }

    }

    public void addTransaction(String type, double amount){
        TransactionHistory t = new TransactionHistory(type, amount, LocalDateTime.now());
        history.add(t);
    }
    public void printHistory(){
        if(history.isEmpty()){
            System.out.println("No transactions");
            return;
        }
        for(TransactionHistory t :  history){
            System.out.println(t.printStatement());
        }
    }
}
