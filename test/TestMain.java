package testmain;

import java.util.ArrayList;
import java.util.Scanner;

import util.*;

public class TestMain {
	public static void main(String[] args) {
		ExamMachine machine = new ExamMachine();
		//Create student objects
		Scanner input = new Scanner(System.in);
		System.out.println("Please enter your account number");
		String username = input.nextLine();
		System.out.println("Please enter your password");
		String password = input.nextLine();
		Student student = new Student(username,password);
		String result = machine.login(username,password);
		if(result.equals("login successful")) {
			System.out.println(result+"\n"+student.getUsername()+" Have fun!");
			ArrayList<Question> paper = machine.getPaper();
			String[] answers = student.exam(paper);
			Teacher teacher = new Teacher();
			int score = teacher.checkPaper(paper, answers);
			System.out.println(student.getUsername()+"grade is"+score);
		}else {
			System.out.println(result);
		}
		input.close();
		
//		String s;
//		s.equals(anObject)
	}
}
