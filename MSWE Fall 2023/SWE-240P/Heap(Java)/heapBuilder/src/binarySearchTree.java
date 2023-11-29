import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.LinkedList;
import java.util.Queue; //Imports queue for task 3 bfs


public class binarySearchTree<T extends Comparable<T>>{
  public Node1<T> insert(Node1<T> root, Node1<T> node) {
    if (root == null) {
        return node;
    }
    else {
      // System.out.println(root.data + " " + node.data + " " + root.data.compareTo(node.data));
      int comparison = root.data.compareTo(node.data);
      if (comparison > 0) {
          root.left = insert(root.left, node);
      }
      else if (comparison < 0) {
          root.right = insert(root.right, node);
      }
    }
    return root;
}



  public Node1<T> delete(Node1<T> root, Node1<T> node) {
    if (root == null) {
      return node;
    }
    int comparison = root.data.compareTo(node.data);
    if (comparison > 0) {
        root.left = delete(root.left, node);
    }
    else if (comparison < 0) {
        root.right = delete(root.right, node);
    }
    else { //comparison equal 0 which means the current node is the node we want to delete
      //node 0 or 1 child
      if (root.left == null) {
        return root.right;
      }
      else if (root.right == null) {
        return root.left;
      }

      //node has 2 children, we find min of right subtree - min of right subtree will maintain the bst hierarchical order
      else {
        Node1<T> replace = root.right; //going to right subtree from root, and finding the min
        while (replace.left != null) {
          replace = replace.left; //similar to LL traversal
        }

        root.studentNumber = replace.studentNumber; //deletion: attaching max of right subtree to the root of the deleted node
        root.data = replace.data; 
        root.homeDepartment = replace.homeDepartment; 
        root.program = replace.program; 
        root.year = replace.year; 
        root.right = delete(root.right, replace);
      }
    }
    return root;
  }



    //**TASK 2 DFS In-Order Traversal**
    public void dfs(Node1<T> root) throws IOException { 
    if (root == null) {
      return;
    }
    dfs(root.left); //dfs left

    try {
      FileWriter writer = new FileWriter("task2.txt", true);

      writer.write(Integer.toString(root.studentNumber)+ " " +root.data+ " " +
      Integer.toString(root.homeDepartment)+ " " +root.program+ " " +Integer.toString(root.year) + "\n");

      writer.close();
    }
    catch (IOException e) {
      System.out.println("cannot write to file");
      e.printStackTrace();
    }

    dfs(root.right); //dfs right
    }



    //**TASK 3 BFS Traversal**
    public void bfs(Node1<T> root) {
      Queue<Node1<T>> queue = new LinkedList<>();
      queue.add(root); //add root to queue
      while (!queue.isEmpty()) { //while queue isnt empty, we add the children of current node to end of queue
        Node1<T> n = queue.remove();

        try {
          FileWriter writer = new FileWriter("task3.txt", true);

          writer.write(Integer.toString(n.studentNumber)+ " " +n.data+ " " +
          Integer.toString(n.homeDepartment)+ " " +n.program+ " " +Integer.toString(n.year) + "\n");

          writer.close();
        }
        catch (IOException e) {
          System.out.println("cannot write to file");
          e.printStackTrace();
        }

        if (n.left != null) { //checking if current node has left and/or right child to add to queue
          queue.add(n.left);
        }
        if (n.right != null) {
          queue.add(n.right);
        }
      }
    }



    public  Node1<T> readText(File file, Node1<T> root, binarySearchTree<T> bst) throws Exception {
      try { //https://www.w3schools.com/java/java_files_read.asp: reading files
      Scanner myReader = new Scanner(file);

      while (myReader.hasNextLine()) {
        String data = myReader.nextLine().toString(); //assign text line to data and slice data to assign to correct variables for student data
        int stuNum = Integer.parseInt(data.substring(1, 8));
        T stuLastName = (T) data.substring(8, 33).strip();
        int homeDepart = Integer.parseInt(data.substring(33, 37));
        String pgram = data.substring(37, 41).strip();
        int y = Integer.parseInt(data.substring(41, 42));
        Node1<T> node = new Node1<T>(stuNum, stuLastName, homeDepart, pgram, y);

        if (data.substring(0, 1).equals("I") && root == null) {
          root = node;
        }
        else if (data.substring(0, 1).equals("I")) {
          bst.insert(root, node);
        }
      }
      myReader.close();
    } 
    catch (FileNotFoundException e) {
      System.out.println("file not found");
      e.printStackTrace();
    }
    return root;
  }



  public static void main(String[] args) throws Exception {
    // //testing ints
    // binarySearchTree bst = new binarySearchTree();
    // Node1 root = new Node1(0123, 10, 123, "ASD", 123);
    // Node1 n1 = new Node1(987, 6, 4321, "a", 432);
    // Node1 n2 = new Node1(987, 14, 4321, "a", 432);
    // Node1 n3 = new Node1(987, 4, 4321, "a", 432);
    // Node1 n4 = new Node1(987, 8, 4321, "a", 432);
    // Node1 n5 = new Node1(987, 12, 4321, "a", 432);
    // Node1 n6 = new Node1(987, 16, 4321, "a", 432);
    // Node1 n7 = new Node1(987, 3, 4321, "a", 432);
    // Node1 n8 = new Node1(987, 5, 4321, "a", 432);
    // Node1 n9 = new Node1(987, 7, 4321, "a", 432);
    // Node1 n10 = new Node1(987, 9, 4321, "a", 432);
    // Node1 n11 = new Node1(987, 11, 4321, "a", 432);
    // Node1 n12 = new Node1(987, 13, 4321, "a", 432);
    // Node1 n13 = new Node1(987, 15, 4321, "a", 432);
    // Node1 n14 = new Node1(987, 17, 4321, "a", 432);
    // bst.insert(root, n1);
    // bst.insert(root, n2);
    // bst.insert(root, n3);
    // bst.insert(root, n4);
    // bst.insert(root, n5);
    // bst.insert(root, n6);
    // bst.insert(root, n7);
    // bst.insert(root, n8);
    // bst.insert(root, n9);
    // bst.insert(root, n10);
    // bst.insert(root, n11);
    // bst.insert(root, n12);
    // bst.insert(root, n13);
    // bst.insert(root, n14);
    // bst.delete(root, n1);
    // bst.delete(root, root);
    // bst.bfs(root);


    //testing strings
    // binarySearchTree bst = new binarySearchTree();
    // Node1 root = new Node1(0123, "g", 123, "ASD", 123);
    // Node1 n1 = new Node1(987, "c", 4321, "a", 432);
    // Node1 n2 = new Node1(987, "j", 4321, "a", 432);
    // Node1 n3 = new Node1(987, "b", 4321, "a", 432);
    // Node1 n4 = new Node1(987, "e", 4321, "a", 432);
    // Node1 n5 = new Node1(987, "i", 4321, "a", 432);
    // Node1 n6 = new Node1(987, "k", 4321, "a", 432);
    // Node1 n7 = new Node1(987, "a", 4321, "a", 432);
    // Node1 n8 = new Node1(987, "d", 4321, "a", 432);
    // Node1 n9 = new Node1(987, "f", 4321, "a", 432);
    // Node1 n10 = new Node1(987, "h", 4321, "a", 432);
    // bst.insert(root, n1);
    // bst.insert(root, n2);
    // bst.insert(root, n3);
    // bst.insert(root, n4);
    // bst.insert(root, n5);
    // bst.insert(root, n6);
    // bst.insert(root, n7);
    // bst.insert(root, n8);
    // bst.insert(root, n9);
    // bst.insert(root, n10);
    // bst.delete(root, n1);
    // bst.delete(root, root);
    // bst.bfs(root);


    binarySearchTree<String> bst = new binarySearchTree<String>();
    Node1<String> root = null;
    File file = new File("tree-input.txt");
    root = bst.readText(file, root, bst); //reading text
    
  
    bst.dfs(root); // using function to print out all nodes
    bst.bfs(root);
  }
}