import java.util.*;

/*
 * Takes any word as input and returns the number of vowels.
 */
public class countVowels{
	
	// I used the vowel string often so I made it a final variable
	public static final String VOWELS = "aeiou";
	
	public static void main(String[] args){
		
		System.out.print("Enter a word: ");
		// user input
		try(Scanner input = new Scanner(System.in)){
			String word = input.next();
			System.out.print("Total number of vowels: ");
			System.out.println(vowelCounter(word));
			System.out.println("Number of each vowel: ");
			int[] eachVowel = intArray(word);
			String[] str = strArray(eachVowel);
			for (String a : str){
				System.out.println(a);
			}
		}
	}
	
	/*
	 * Returns an integer of the total number of vowels found in input.
	 */
	private static int vowelCounter(String input){
		
		int vowelCount = 0;
		
		for (int i = 0; i < input.length(); i++){
			for (int j = 0; j < VOWELS.length(); j++){
				if (input.charAt(i) == VOWELS.charAt(j))
					vowelCount++;
			}
		}
		return vowelCount;
	}
	
	/*
	 * Returns integer Array containing the number of every vowel found in the input String.
	 */
	private static int[] intArray(String input){
		int[] vowelArray = new int[VOWELS.length()];
		for (int i = 0; i < input.length(); i++){
			for (int j = 0; j < VOWELS.length(); j++){
				if (input.charAt(i) == VOWELS.charAt(j))
					vowelArray[j]++;
			}
		}
		return vowelArray;
	}
	
	/*
	 * Adds labels to each integer for easier readability.
	 * Transforms integer Array into String Array.
	 */
	private static String[] strArray(int[] arrayOfVowels){
		String[] str = new String[VOWELS.length()];
		for(int i = 0; i < VOWELS.length(); i++){
			str[i] = VOWELS.charAt(i) + "...." + arrayOfVowels[i];
		}
		return str;
	}
}