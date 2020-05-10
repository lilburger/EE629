package util;

public class Question {
	//Treat the question of the test paper as the object
	private String title;
	private String answer;
	public Question(String title,String answer) {
		this.title = title;
		this.answer = answer;
	}
	public String getTitle() {
		return this.title;
	}
	public String getAnswer() {
		return this.answer;
	}
	public boolean equals(Object obj) {
		if(this == obj) {
			return true;
		}
		if(obj instanceof Question) {
			Question anotherQuestion = (Question)obj;
			if(anotherQuestion.title.equals(this.title)) {
				return true;
			}
		}
		return false;
	}
	public int hashCode() {
		return this.title.hashCode();
	}
}
