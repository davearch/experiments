/***
Check if Palindrome – Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
***/
package experiments.src.java;
import java.util.*;

public class checkIfPalindrome {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter word to check if it is a palindrome: ");
		String wordToCheck = input.next();
		input.close();
		char[] charCheck = new char[wordToCheck.length()];
		wordToCheck.getChars(0, 
				     wordToCheck.length(), 
				     charCheck, 
				     0);
		if (isPalindrome(charCheck) == true)
			System.out.println(wordToCheck + 
				" is a Palindrome!");
		else
			System.out.println(wordToCheck + 
				" is NOT a Palindrome!");
	}
	public static boolean isPalindrome(char[] one) {
		int i1 = 0;
		int i2 = one.length-1;
		while(i2 > i1) {
			if (one[i1] != one[i2]){
				return false;
			}
			++i1;
			--i2;
		}
		return true;
	}
}
