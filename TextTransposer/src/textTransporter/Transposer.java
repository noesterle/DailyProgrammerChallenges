package textTransporter;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


public class Transposer {
	public ArrayList<String> read(String filename) {
		ArrayList<String> contents = new ArrayList<String>();
		//read file.
		try{
			File text = new File(filename);
			Scanner in = new Scanner(text);
			while (in.hasNextLine()){
				//Add line in file to line list.
				contents.add(in.nextLine());
			}
			
		}catch (IOException e){
			e.printStackTrace();
		}
		return contents;
	}
	
	public void print(ArrayList<String> arr){
		int count = 0; //Location of character just printed.
		int longest=0; //Length of longest String.
		for(int i = 0; i < arr.size();i++){
			if(longest < arr.get(i).length()){
				longest = arr.get(i).length(); //Find longest string length.
			}
		}
		while( count < longest){
			for(String line:arr){
				if (count < line.length()){ //Keep from printing characters that aren't there.
					System.out.print(line.charAt(count) +" "); //Print the character at location count.
				}
			}
			System.out.println();
			count++; //Move on to the next character.
		}
	}
}
