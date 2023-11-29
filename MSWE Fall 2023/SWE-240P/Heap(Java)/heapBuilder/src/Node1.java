public class Node1<T extends Comparable<T>> {//student data 
    int studentNumber;
    T data;
    int homeDepartment;
    String program;
    int year;
    //left and right children
    Node1<T> left; 
    Node1<T> right;

    public Node1(int studentNumber, T data, int homeDepartment, String program, int year) {
        this.studentNumber = studentNumber;
        this.data = data;
        this.homeDepartment = homeDepartment;
        this.program = program;
        this.year = year;
        this.left = null;
        this.right = null;
    }

    // default parameters
    public Node1(T data) {
        this(0, data, 0, "", 0);
    }
}
