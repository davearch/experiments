import java.util.*;

/*
 * Takes any valid word and translates it into Pig Latin.
 * If a word is not valid it reports an error.
 */
public class pigLatin{
	
	public static void main(String args[]){
		
		Scanner input = new Scanner(System.in);
		System.out.print("enter word to piggify: ");
		String original = input.next();
		System.out.println(piggify(original));
		
		
	}
	// Pig Latin translator method
	private static String piggify(String input){
		
		String vowels = new String("aeiou");
		String result = null;
		
		for(int i = 0; i < input.length(); i++){
			for (int j = 0; j < vowels.length(); j++){
				if (input.charAt(i) == vowels.charAt(j)){
					result = input.substring(i) + input.substring(0, i) + "ay";
					return result;
				}
			}
		}
		return "Error: please pick a different word";
	}
}