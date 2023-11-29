import java.io.File;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BSTToHeapTransformer<T extends Comparable<T>> {
    
    // public ArrayList<T> dfs(Node1<T> root, ArrayList<T> array) { //Inorder traversal of bst to create array which we can then call heap on array
    //     if (root != null) {
    //         dfs(root.left, array);
    //         array.add((T) root.data);
    //         dfs(root.right, array);
    //     }
    //     return array;
    // }

    public ArrayList<T> bfs(Node1<T> root, ArrayList<T> array) { //bfs to create array
        Queue<Node1<T>> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node1<T> n = queue.remove();
            array.add(n.data);
            if (n.left != null) {
                queue.add(n.left);
            }
            if (n.right != null) {
                queue.add(n.right);
            }
        }
        return array;
    }


    public T[] toMaxHeap(Node1<T> root, heapBuilder<T> hB) {
        ArrayList<T> array = bfs(root, new ArrayList<>());
        // In this corrected version, Array.newInstance is used to create a new array of the same type as the elements in the ArrayList. This should resolve the ClassCastException issue.
        // However, note that this approach assumes that the type of elements in the ArrayList is the same as the type of elements in the Node1 objects. If there is any mismatch in types, you might need to handle it accordingly.
        T[] newArray = array.toArray((T[]) Array.newInstance(array.get(0).getClass(), array.size())); //used chat gpt to fix Exception in thread "main" java.lang.ClassCastException: class [Ljava.lang.Object; cannot be cast to class [Ljava.lang.Comparable; ([Ljava.lang.Object; and [Ljava.lang.Comparable; are in module java.base of loader 'bootstrap') error
        
        // Convert ArrayList to max heap directly
        for (int i = newArray.length / 2 - 1; i >= 0; i--) {
            hB.heapifyMax(newArray, newArray.length, i);
        } 
        for (T j: newArray) {
            System.out.print(j + " ");
        }
        return newArray;
    }



    public T[] toMinHeap(Node1<T> root, heapBuilder<T> hB) {
        ArrayList<T> array = bfs(root, new ArrayList<>());
        // In this corrected version, Array.newInstance is used to create a new array of the same type as the elements in the ArrayList. This should resolve the ClassCastException issue.
        // However, note that this approach assumes that the type of elements in the ArrayList is the same as the type of elements in the Node1 objects. If there is any mismatch in types, you might need to handle it accordingly.
        T[] newArray = array.toArray((T[]) Array.newInstance(array.get(0).getClass(), array.size())); //used chat gpt to fix Exception in thread "main" java.lang.ClassCastException: class [Ljava.lang.Object; cannot be cast to class [Ljava.lang.Comparable; ([Ljava.lang.Object; and [Ljava.lang.Comparable; are in module java.base of loader 'bootstrap') error
        
        // Convert ArrayList to max heap directly
        for (int i = newArray.length / 2 - 1; i >= 0; i--) {
            hB.heapifyMin(newArray, newArray.length, i);
        } 
        for (T j: newArray) {
            System.out.print(j + " ");
        }
        return newArray;
    }



    public static void main(String[] args) throws Exception {
        //Testing Strings
        // binarySearchTree<String> bst = new binarySearchTree<>();
        // heapBuilder<String> hB = new heapBuilder<>();
        // BSTToHeapTransformer<String> bstTransformer = new BSTToHeapTransformer<>();
        // Node1<String> root = new Node1<String> (0123, "1", 123, "ASD", 123);
        // Node1<String> n1 = new Node1<String> (987, "11", 4321, "a", 432);
        // Node1<String> n2 = new Node1<String> (987, "6", 4321, "a", 432);
        // Node1<String> n3 = new Node1<String> (987, "9", 4321, "a", 432);
        // Node1<String> n4 = new Node1<String> (987, "3", 4321, "a", 432);
        // Node1<String> root = new Node1<String> (0123, "h", 123, "ASD", 123);
        // Node1<String> n1 = new Node1<String> (987, "c", 4321, "a", 432);
        // Node1<String> n2 = new Node1<String> (987, "j", 4321, "a", 432);
        // Node1<String> n3 = new Node1<String> (987, "a", 4321, "a", 432);
        // Node1<String> n4 = new Node1<String> (987, "b", 4321, "a", 432);
        // Node1<String> n5 = new Node1<String> (987, "e", 4321, "a", 432);
        // Node1<String> n6 = new Node1<String> (987, "d", 4321, "a", 432);
        // Node1<String> n7 = new Node1<String> (987, "f", 4321, "a", 432);
        // bst.insert(root, n1);
        // bst.insert(root, n2);
        // bst.insert(root, n3);
        // bst.insert(root, n4);
        // bst.insert(root, n5);
        // bst.insert(root, n6);
        // bst.insert(root, n7);
        // bst.delete(root, n1);

        //using text file from assignment 4
        // File file = new File("tree-input.txt");
        // Node1<String> root = null;
        // root = bst.readText(file, root, bst);
        // System.out.println(bstTransformer.dfs(root, new ArrayList<>()));


        // Testing int
        binarySearchTree<Integer> bst = new binarySearchTree<>();
        heapBuilder<Integer> hB = new heapBuilder<>();
        BSTToHeapTransformer<Integer> bstTransformer = new BSTToHeapTransformer<>();
        Node1<Integer> root = new Node1<Integer> (0123, 1, 123, "ASD", 123);
        Node1<Integer> n1 = new Node1<Integer> (987, 11, 4321, "a", 432);
        Node1<Integer> n2 = new Node1<Integer> (987, 6, 4321, "a", 432);
        Node1<Integer> n3 = new Node1<Integer> (987, 9, 4321, "a", 432);
        Node1<Integer> n4 = new Node1<Integer> (987, 3, 4321, "a", 432);
        Node1<Integer> n5 = new Node1<Integer> (987, 14, 4321, "a", 432);
        Node1<Integer> n6 = new Node1<Integer> (987, 2, 4321, "a", 432);
        Node1<Integer> n7 = new Node1<Integer> (987, 8, 4321, "a", 432);
        Node1<Integer> n8 = new Node1<Integer> (987, 0, 4321, "a", 432);
        bst.insert(root, n1);
        bst.insert(root, n2);
        bst.insert(root, n3);
        bst.insert(root, n4);
        bst.insert(root, n5);
        bst.insert(root, n6);
        bst.insert(root, n7);
        bst.insert(root, n8);
        // bst.delete(root, n1);
        bstTransformer.toMaxHeap(root, hB);
        System.out.println();
        bstTransformer.toMinHeap(root, hB);
    }
}
