package textTransporter;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


public class Transposer {
	public ArrayList<ArrayList> read(String filename) {
		ArrayList<ArrayList> contents = new ArrayList();
		ArrayList<String> line = new ArrayList();
		//read file.
		try{
			File text = new File(filename);
			Scanner in = new Scanner(text);
			while (in.hasNextLine()){
				//Add line in file to line list.
				line.add(in.nextLine());
				//Add line array to contents array
				contents.add(line);
			}
			
		}catch (IOException e){
			e.printStackTrace();
		}
		return contents;
	}
	
	public void print(ArrayList<ArrayList> arr){
		int count = 0; //Location of character just printed.
		int longest=0; //Length of longest array.
		for(int i = 0; i < arr.size();i++){
			if(longest < arr.get(i).size()){
				longest = arr.get(i).size();
			}
		}
		while( count < longest){
			for(ArrayList line:arr){
				System.out.print(line.get(count)+" ");
			}
			count++;
		}
	}
}
