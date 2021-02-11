public class Person {

    String name;
    String telNum;
    String email;
    String address;

    public Person(String name, String telNum, String email, String address) {
        this.name = name;
        this.telNum = telNum;
        this.email = email;
        this.address = address;
    }

    public String toString() {
        String output = ("Their name is: " + name + "\n");
        output += ("Their telephone number is: " + telNum + "\n");
        output += ("Their e-mail is: " + email + "\n");
        output += ("Their address is: " + address + "\n");

        return output;
    }
}
