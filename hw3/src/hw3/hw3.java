package hw3;

import java.io.File;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class hw3 {
	public static void main(String[] args) {
		try {
			File text = new File("Text.txt");
			Scanner scanner = new Scanner(text);
			Set theSet = new HashSet();
			while (scanner.hasNextLine()) {
				theSet.add(scanner.nextLine());
			}
			String string = Arrays.toString(args);
			int a = 0;
			int b = string.length();
			String ans = "";
			while (a != b) {
				if(search(string.substring(a, b), theSet) == false) {
					if(b - a == 1) {
						ans += (string.substring(a, b) + " ");
						++a;
						b = string.length();
					}
					else {
						--b;
					}
				}
				else {
					ans += (" " + string.substring(a, b) + " ");
					a = b;
					b = string.length();
				}
			}
			System.out.println(ans);
		} catch (Exception e) {
			System.out.println("no");
		}
	}
	
	public static boolean search(String string, Set theSet) {
		if(theSet.contains(string))
			return true;
		else
			return false;
	}
}
