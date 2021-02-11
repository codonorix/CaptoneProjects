public class Project {

    String projectNum;
    String projectName;
    String houseType;
    String address;
    String erfNum;
    double totalFee;
    double currentPaid;
    String deadline;


    public Project(String projectNum, String projectName, String houseType, String address, String erfNum, double totalFee, double currentPaid, String deadline) {

        this.projectNum = projectNum;
        this.projectName = projectName;
        this.houseType = houseType;
        this.address = address;
        this.erfNum = erfNum;
        this.totalFee = totalFee;
        this.currentPaid = currentPaid;
        this.deadline = deadline;
    }

    public String toString() {
        String output = ("The project number is: " + projectNum + "\n");
        output += ("The project name is: " + projectName + "\n");
        output += ("The house type is: " + houseType + "\n");
        output += ("The address is: " + address + "\n");
        output += ("The ERF number is: " + erfNum + "\n");
        output += ("The total fee is: " + totalFee + "\n");
        output += ("The amount currently paid off is: " + currentPaid + "\n");
        output += ("The project deadline is: " + deadline + "\n");

        return output;
    }
}
