import java.util.ArrayList;
import java.util.Scanner;

public class Bank {

    ArrayList<Accounts> acclist = new ArrayList();


    public void createAccount(String name, double balance, String username, String password, String account_type) {
        Accounts acc;
        String account_num = "MDID00" + (acclist.size() + 1);
        if (account_type.equals("Savings")) {
            acc = new SavingsAccount(account_num, name, balance, username, password);
        } else if (account_type.equals("Current")) {
            acc = new CurrentAccount(account_num, name, balance, username, password);
        } else if (account_type.equals("Student")) {
            acc = new StudentAccount(account_num, name, balance, username, password);
        }else{
            System.out.println("Invalid Account type!");
            return;
        }
        acclist.add(acc);
    }

    public Accounts login (String username, String password){
       for(Accounts a : acclist){
           if((a.getUsername().equals(username)) && (a.getPassword().equals(password))){
               System.out.println("login successful!");
               return a;
           }
       }
        System.out.println("login failed!");
       return null;
    }

    public Accounts findbyaccnum (String account_num){
        for(Accounts a : acclist){
            if(a.getAccount_num().equals(account_num)){
                return a;
            }
        }
        System.out.println("no user found!");
        return null;
    }
}

