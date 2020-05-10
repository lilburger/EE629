package util;

import java.util.ArrayList;

public class Teacher {

	public int checkPaper(ArrayList<Question> paper, String[] answers) {
		System.out.println("In batch...");
		try {
			Thread.sleep(5000);
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		int score = 0;
		for (int i = 0; i < paper.size(); i++) {
			Question question = paper.get(i);
			if(question.getAnswer().equalsIgnoreCase(answers[i])) {
				score+=100/paper.size();
			}
		}
		return score;
	}
}
