import java.util.Scanner;

public class PoisedMain {
    public static void main(String[] args) {


        //======================================| Variables|======================================\\
        boolean customer = false;       //All of these are going to be used inside a while loop
        boolean contractor = false;     //Filled with if statements, we set them to false so that
        boolean architect = false;      //When the data will be filled we'll change them to 'True'
        boolean project = false;        //And then the program will know we've entered the data for
        boolean allComp = false;        //that.
        boolean exit = false;

        //======================================| Classes |======================================\\

        Person customerOut =  new Person("","","","");      //All of these are from our persons
        Person architectOut =  new Person("","","","");     //and project class, we used it to creates
        Person contractorOut =  new Person("","","","");    //The basics of the objects
        Project projectOut =  new Project("","","","", "", 0, 0, "");

        //======================================| Creating the information |======================================\\
        Scanner input = new Scanner(System.in); //We create a new scanner that will be called input to allow the user to enter their data

        while (allComp == false) {      //While allComp is false (which by default it is) this section of code will run


            //======================================| Customer Data |======================================\\
            if (customer == false) {    //If the customer is equal to false we'll run this if block

                System.out.println("+--------------| Customer Data |--------------+");
                System.out.println();
                System.out.println("Please enter the customer name: ");           //Each of these lines asks a question and then waits for the users input
                String custName = input.nextLine();                             //We store the user input in their own variable which will be used later

                System.out.println("Please enter the customer telephone number: ");
                String custTelNum = input.nextLine();

                System.out.println("Please enter the customer e-mail: ");
                String custEmail = input.nextLine();

                System.out.println("Please enter the customers address: ");
                String custAddress = input.nextLine();

                customerOut = new Person(custName, custTelNum, custEmail, custAddress); //We then take all the data and place it in the "customerOut" variable we created at the start of the program
                customer = true;    //We then set customer to true so we don't keep repeating this block of code

                //======================================| Contractor Information |======================================\\

            }else if(contractor == false){

                System.out.println("+--------------| Contractor Information |--------------+");
                System.out.println();
                System.out.println("Please enter the contractor name: ");     //Please refer back to the start of "customer information" same thing done there is done here but for the contractor
                String contractName = input.nextLine();

                System.out.println("Please enter the contractor telephone number: ");
                String contractTelNum = input.nextLine();

                System.out.println("Please enter the contractor e-mail: ");
                String contractEmail = input.nextLine();

                System.out.println("Please enter the contractor address: ");
                String contractAddress = input.nextLine();

                contractorOut = new Person(contractName, contractTelNum, contractEmail, contractAddress);
                contractor = true;


                //======================================| architect Data |======================================\\
            }else if(architect == false){

                System.out.println("+--------------| Architect Information |--------------+");
                System.out.println();
                System.out.println("Please enter the architect name: ");      //Please refer back to the start of "customer information" same thing done there is done here but for the architect
                String archiName = input.nextLine();

                System.out.println("Please enter the architect telephone number: ");
                String archiTelNum = input.nextLine();

                System.out.println("Please enter the architect e-mail: ");
                String archiEmail = input.nextLine();

                System.out.println("Please enter the architect address: ");
                String archiAddress = input.nextLine();

                architectOut = new Person(archiName, archiTelNum, archiEmail, archiAddress);
                architect = true;


                //======================================| Project Data |======================================\\
            }else if (project == false){        //We check if the project is 'false' which by default it is
                System.out.println("+--------------| Project Information |--------------+");
                System.out.println();

                System.out.println("Please enter the project number: ");  //We request the data we need the user to enter
                String projectNum = input.nextLine();                   //We then wait for them to input the data and store it in a variable

                System.out.println("Please enter the project name: ");
                String projectName = input.nextLine();

                System.out.println("Please enter the type of house it will be: ");
                String houseType = input.nextLine();

                System.out.println("Please enter the address the house will be built: ");
                String address = input.nextLine();

                System.out.println("Please enter the erf Number: ");
                String erfNum = input.nextLine();

                System.out.println("Please enter the total fee: ");
                double totalFee = input.nextDouble();

                System.out.println("Please enter how much has currently been paid: ");
                double currentPaid = input.nextDouble();

                System.out.println("Please enter the deadline of the project: ");
                String deadline = input.nextLine();

                projectOut = new Project(projectNum, projectName, houseType, address, erfNum, totalFee, currentPaid, deadline); //We then create the new project with the new data entered
                project = true;     //Sets the project to 'true' so we don't enter this block again
                allComp = true;     //Sets allComp to 'true' so that we leave the while loop


                //======================================| Output data |======================================\\
                while (exit == false) { //While exit is equal to false this while loop will start

                    System.out.println("#==============| CLIENT INFO |==============#");    //The next 11 lines just print out the data so the user can see the data they have entered to double check it's right
                    System.out.println(customerOut);
                    System.out.println();
                    System.out.println("#==============| CONTRACTOR INFO |==============#");
                    System.out.println(contractorOut);
                    System.out.println();
                    System.out.println("#==============| Archetect INFO |==============#");
                    System.out.println(architectOut);
                    System.out.println();
                    System.out.println("#==============| Project INFO |==============#");
                    System.out.println(projectOut);


                    System.out.println("+--------------| Please enter a value |--------------+");   //We then promt the user to select one of the 4 options
                    System.out.println("1 - Change due date of the project");
                    System.out.println("2 - Change the total amount paid");
                    System.out.println("3 - Update contractors details");
                    System.out.println("4 - Finalise the project.");
                    System.out.println("+----------------------------------------------------+");

                    int option = input.nextInt();       //We then wait for the user to select what option they want

                    //======================================| edit data |======================================\\
                    if (option == 1){   //If the user selects 1 we let them change the due date
                        System.out.println("Please enter the new due date: ");
                        deadline = input.nextLine();    //We then wait for them to enter their information
                        projectOut = new Project(projectNum, projectName, houseType, address, erfNum, totalFee, currentPaid, deadline); //We then take all the previous variables and pu tthem in here but replace the duedate with the new entered date

                    }else if (option == 2){
                        System.out.println("Please enter the total amount that has been paid: ");
                        currentPaid = input.nextDouble();   //We wait for the user to enter the new total paid
                        projectOut = new Project(projectNum, projectName, houseType, address, erfNum, totalFee, currentPaid, deadline); //We then replace the current paid with the new paid

                    }else if (option == 3){
                        System.out.println("Please enter the contractor name: ");   //This is just requesting the user to enter the contractors details
                        String contractName = input.nextLine();

                        System.out.println("Please enter the contractor telephone number: ");
                        String contractTelNum = input.nextLine();

                        System.out.println("Please enter the contractor e-mail: ");
                        String contractEmail = input.nextLine();

                        System.out.println("Please enter the contractor address: ");
                        String contractAddress = input.nextLine();

                        contractorOut = new Person(contractName, contractTelNum, contractEmail, contractAddress);   //We reprint all their data

                    }else if (option == 4){ //if the user enters 4 we will finiliase the project and see if they need to be invoiced
                        if (totalFee > currentPaid) {   //We check if the total fee is more than what's currently been paid
                            System.out.println("+------------ Poised Invoices ------------+");
                            System.out.println(customerOut);
                            System.out.println("+-----------------------------------------+");
                            System.out.println("Total Fee - "  + totalFee);
                            System.out.println("Currently Paid - " + currentPaid);
                            System.out.println("Total to pay - " + (totalFee - currentPaid));
                            System.out.println("+-----------------------------------------+");
                        }else{
                            System.out.println("Account has been paid. No invoice to be generated.");   //If the full amount is paid we will tell them no invoice will be generated
                        }
                        exit = true;    //We then exit the program
                    }else{
                        System.out.println("That's an invalid option.");
                    }
                }
            }


        }


    }
}
