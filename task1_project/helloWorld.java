import java.util.Scanner;

public class helloWorld {

	public static void main(String[] args)  
	{  
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);    //System.in is a standard input stream  
		System.out.print("What is your name?: ");  
		String a = sc.nextLine();
		
		System.out.println(a); 

	}

}
