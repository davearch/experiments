package experiments.src;
import java.util.*;

public class ReverseAString{
	public static void main(String args[]){
		
		// enter a string and the program will reverse it and print it out.
		Scanner input = new Scanner(System.in);
		System.out.print("Enter any string that you want:");
		String stringToReverse = input.nextLine();
		
		int length = stringToReverse.length();
		char[] oldString = new char[length];
		char[] newString = new char[length];
		
		// put string into char array
		for (int i = 0; i < length; i++) {
			oldString[i] = stringToReverse.charAt(i);
		}
		
		// reverse string
		for (int i = 0; i < length; i++){
			newString[i] = oldString[length - 1 -i];
		}
		
		// print string
		System.out.println(newString);
	}
}
