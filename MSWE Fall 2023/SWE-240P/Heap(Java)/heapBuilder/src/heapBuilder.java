import java.util.LinkedList;
import java.util.Queue;


public class heapBuilder <T extends Comparable<T>> {
    public void heapifyMax(T[] array, int lenOfArray, int index) {
        int largest = index;
        int leftChild = index * 2 + 1;
        int rightChild = index * 2 + 2;

        if (leftChild < lenOfArray && array[leftChild].compareTo(array[largest]) > 0) {
            largest = leftChild;
        }

        if (rightChild < lenOfArray && array[rightChild].compareTo(array[largest]) > 0) {
            largest = rightChild;
        }

        if (largest != index) {
            T temp = array[index];
            array[index] = array[largest];
            array[largest] = temp;
            heapifyMax(array, lenOfArray, largest);
        }
    }


    public void heapifyMin(T[] array, int lenOfArray, int index) {
        int smallest = index;
        int leftChild = index * 2 + 1;
        int rightChild = index * 2 + 2;

        if (leftChild < lenOfArray && array[leftChild].compareTo(array[smallest]) < 0) {
            smallest = leftChild;
        }

        if (rightChild < lenOfArray && array[rightChild].compareTo(array[smallest]) < 0) {
            smallest = rightChild;
        }

        if (smallest != index) {
            T temp = array[index];
            array[index] = array[smallest];
            array[smallest] = temp;
            heapifyMin(array, lenOfArray, smallest);
        }
    }
    

    public Node1<T> constructBinaryTree(int index, int lenOfArray, T[] array) { //constructing binary tree given array based heap
        if (index < lenOfArray) {
            Node1<T> root = new Node1(array[index]);
            int leftIndex = index * 2 + 1;
            int rightIndex = index * 2 + 2;
    
            if (leftIndex < lenOfArray) {
                root.left = constructBinaryTree(leftIndex, lenOfArray, array);
            }
            if (rightIndex < lenOfArray) {
                root.right = constructBinaryTree(rightIndex, lenOfArray, array);
            }
            return root;
        }
        return null;
    }


    public Node1<T> getRoot(int index, int lenOfArray, T[] array) { //helper function to get root node to use to print out binary tree
        return constructBinaryTree(0, array.length, array);
    }


    public void printBinaryTree(Node1<T> root) { //helper function to print out binary tree in bfs order
        Queue<Node1<T>> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node1<T> n = queue.remove();
            System.out.print(n.data + " ");
            if (n.left != null) {
                queue.add(n.left);
            }
            if (n.right != null) {
                queue.add(n.right);
            }
        }
    }




    public static void main(String[] args) {
        //testing heap with integers
        // heapBuilder<Integer> intHeapBuilder = new heapBuilder<Integer>();
        // Integer[] intArray = {4, 10, 3, 5, 1, 6, 14, 2};
        // for (int i = intArray.length / 2 - 1; i >= 0; i--) { //only considering the parents of the leaf nodes because leaf nodes themselves are already heaps
        // intHeapBuilder.heapifyMax(intArray, intArray.length, i); //working towards root node
        // }
        
        // Node1<Integer> root = intHeapBuilder.getRoot(0, intArray.length, intArray); //getRoot calls constructBinaryTree, creating the binary tree
        // intHeapBuilder.printBinaryTree(root); //print out heap in binary tree nodes bfs


        //testing heap with strings
        heapBuilder<String> stringHeapBuilder = new heapBuilder<String>();
        String[] stringArray = {"apple", "banana", "orange", "grape", "pear"};
        for (int i = stringArray.length / 2 - 1; i >= 0; i--) { //only considering the parents of the leaf nodes because leaf nodes themselves are already heaps
        stringHeapBuilder.heapifyMax(stringArray, stringArray.length, i); //working towards root node
        }

        Node1<String> root = stringHeapBuilder.getRoot(0, stringArray.length, stringArray); //getRoot calls constructBinaryTree, creating the binary tree
        stringHeapBuilder.printBinaryTree(root); //print out heap in binary tree nodes bfs
    }
}


        


