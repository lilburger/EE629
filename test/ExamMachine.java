package util;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;

/*
 * Design a Exam System
 * Multiple Choice
 * 	1.Which of the following options is not a basic type of Java
 * 		A short	B boolean C String D byte
 * 	2.Which of the following options is the basic type of Java
 * 		A Short B Boolean CString D char
 * Please enter the correct option?
 * 
 * Students need to log in before entering the exam
 * Design a relationship among students,teachers and exam
 * There is a test bank and the questions will be chose randomly from the bank
 * Students use the generated papers for the exam-> Answer 5 options A D B C E
 * The teacher is responsible for changing the final paper
 * 

 */
public class ExamMachine {
	//Record student's account number and password
	private HashMap<String,String> userBox = new HashMap<>();
	{
		userBox.put("Junyan Chen", "123");
		userBox.put("Kenny", "0605");
		userBox.put("Java", "666");
	}
	
	
	

	private HashSet<Question> questionBank = new HashSet<>();
	{
		questionBank.add(new Question("Which of the following options is not a basic type of Java?\n\tA.short\n\tB.boolean\n\tC.String\n\tD.byte","C"));
		questionBank.add(new Question("Which of the following options is the basic type of Java?\n\tA.Byte\n\tB.boolean\n\tC.String\n\tD.Integer","B"));
		questionBank.add(new Question("Which of the following options is a reference type of Java?\n\tA.short\n\tB.boolean\n\tC.String\n\tD.byte","C"));
		questionBank.add(new Question("Which of the following options is not a reference type of Java?\n\tA.Short\n\tB.Integer\n\tC.String\n\tD.byte","D"));
		questionBank.add(new Question("Which of the following options is a class of java.util package?\n\tA.Integer\n\tB.Scanner\n\tC.String\n\tD.Math","B"));
		questionBank.add(new Question("Which of the following options is not a class of java.util package?\n\tA.String\n\tB.Scanner\n\tC.HashSet\n\tD.HashMap","A"));
		questionBank.add(new Question("Which of the following options is not a method in the String class?\n\tA.compareTo\n\tB.append\n\tC.substring\n\tD.concat","B"));
		questionBank.add(new Question("Which of the following options is a method in the String class?\n\tA.put\n\tB.concat\n\tC.delete\n\tD.insert","B"));
		questionBank.add(new Question("Which of the following options is not an interface modifier?\n\tA.public\n\tB.static\n\tC.final\n\tD.abstract","D"));
		questionBank.add(new Question("Which of the following options is not a method of Set collection?\n\tA.set\n\tB.add\n\tC.remove\n\tD.iterator","A"));
	}

	public ArrayList<Question> getPaper(){
		//Randomly select the test paper. The questions are not repeated. First save with set collection and then change back to arraylist
		HashSet<Question> paper = new HashSet<>();
		//Generate a random number to find the problem
		ArrayList<Question> questionBank = new ArrayList<>(this.questionBank);
		while(paper.size()!=5) {
			//Randomly Pick
			int index = new Random().nextInt(this.questionBank.size());//[0-10)
			Question question = questionBank.get(index);
			//Return the question to the HashSet collection
			paper.add(question);
		}
		return new ArrayList<Question>(paper);
	}
	public String login(String username,String password) {
		String realPassword = this.userBox.get(username);
		if(realPassword!=null && realPassword.equals(password)) {
			return "login successful";
		}
		return "Username or password is wrong!";
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
}
