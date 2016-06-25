package textTransporter;

import java.util.ArrayList;

public class Main {
	public static void main(String[] args){
		Transposer t = new Transposer();
		ArrayList arr = t.read("/home/nathan/code/git/DailyProgrammerChallenges/TextTransposer/src/textTransporter/test.txt");
		t.print(arr);
	}
}
