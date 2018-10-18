## 剑指offer刷题Java笔记

#### 1 二维数组中的查找 

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。 

解题思路：根据数组规律，可将数组右上角的元素作为搜索的起点，如果目标大于当前元素，则下标下移，如果小于当前元素，则目标上移。   PS：也可以将起点定在左下角。

```
public class Solution {
    public boolean Find(int [][] array,int target) {
        int row = array.length, column = array[0].length;
                 int r = 0, c = column - 1;

                 while (r < row && c >= 0) {
                     if (array[r][c] > target) {
                         c--;
                     } else if (array[r][c] < target) {
                         r++;
                     } else {
                         return true;
                     }
                 }
		 
		 return false;
    }
}
```



#### 2 替换空格 

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。 

思路：先遍历字符串，求出空格的个数，然后计算新字符串需要的数组长度，并分配空间，遍历数组，如果是非空格将将字符放入数组，如果是空格在数组放入 %20.

```
public class Solution {
    public String replaceSpace(StringBuffer str) {
    	StringBuilder res = new StringBuilder();
    	for (int i=0; i<str.length(); i++) {
    		if (str.charAt(i) == ' ') {
    			res.append("%20");
    		}
    		else {
    			res.append(str.charAt(i));
    		}
    	}
    	return res.toString();
    }
}
```



#### 3 从尾到头打印链表 

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。 

思路： 1. 递归写法，先遍历链表，后打印。 2. 遍历链表，将值插入到List头部。

```
/**
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
         ArrayList<Integer> list = new ArrayList<>();
        while (listNode != null) {
        	list.add(0, listNode.val);
        	listNode = listNode.next;
        }
        return list;
        

    }
}

//递归法
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> list = new ArrayList<>();
        pList(listNode, list);
        return list;
	}
	
	private void pList(ListNode listNode, ArrayList<Integer> list) {
		if (listNode == null)  return;
		pList(listNode.next, list);
		list.add(listNode.val);
	}
}
```



#### 4 重建二叉树 

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。 

思路：根据二叉树的遍历特点重建，二叉树前序遍历 :根节点---左节点---右节点，根节点在前，后面是左子树和右子树； 中序遍历:左节点---根节点---右节点， 后序遍历：左节点---右节点---根节点。 其实前后中的区分就是根节点的位置， 左右节点的相对位置是不变的，左节点一直在前。

对前序序列：{1,2,4,7,3,5,6,8}，可得知根节点是1， 中序遍历序列{4,7,2,1,5,3,8,6}，找到根节点1的位置，1的左边4,7,2, 是左子树，右边5,3,8,6是右子树；对子序列4,7,2，其前序遍历为2,4,7，根节点是2，然后根据前面的规则对子序列递归分割即可。



```
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
	static public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
		 if (pre == null || in == null) return null;
		 return getTreeNode(pre, 0, pre.length - 1, in, 0, in.length - 1);
	}

	//pre:{1,2,4,7,3,5,6,8},  in:{4,7,2,1,5,3,8,6}
	static TreeNode getTreeNode(int [] pre,int preLeft, int preRight, 
						int [] in, int inLeft, int inRight) {
		if (preLeft > preRight) return null;
		
		int root = pre[preLeft];
		TreeNode rootNode = new TreeNode(root);
		int rId = 0; //root在in序列中的下标
		for (int i = inLeft; i <= inRight; i++) {
			if (in[i] == root) {
				rId = i;
				break;
			}
		}
		
		int leftSubLen = rId - inLeft;//左子树的长度
		rootNode.left = getTreeNode(pre, preLeft + 1, preLeft + leftSubLen, 
								   in, inLeft, rId - 1);
		rootNode.right = getTreeNode(pre, preLeft + leftSubLen + 1, preRight,
									in, rId + 1, inRight);
		return rootNode;
	}
}
```



#### 5 用两个栈实现队列 

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。 

思路：栈的特点是先进后出，FILO， 队列的特点是先进先出FIFO。使用栈A进行入队操作，使用栈B进行出队操作，且当栈B为空时，将栈A的元素依次压如栈B。



```
import java.util.Stack;

public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        if (stack1 != null) {
        	stack1.push(node);
        }
    }
    
    public int pop() {
    	if (!stack2.isEmpty()) {
    		return stack2.pop();
    	} else {
    		while (!stack1.isEmpty()) {
    			stack2.push(stack1.pop());
    		}
    		return stack2.pop();
    	}
    }
}
```



#### 6 旋转数组的最小数字 

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路：二分搜索的变化版本，找出数组中递减出现的地方。根据头尾找中间节点，比较中间节点和头尾的大小，{3,4,5,1,2}如果中间值大于左边的节点或者大于右边的节点（考虑到可能会和一端相等）， 则说明最小节点在中间值的右侧，否则在左侧，直到剩下最后2个，返回其中的最小值即可。

1,2,3,3,3,3,3,3,3,4 -----> 3,3,3,3,3,3,4,1,2,3

考虑一种特殊情况， 原数列：1,1,1,1,1,1，2,3，旋转后：1，2,3，1,1,1,1,1。此时，头尾和中间值相等，刚才的算法无法执行，这种情况下要逐个遍历查询，找出第一个递减序列的地方。

```
import java.util.ArrayList;
public class Solution {
    
	static public int minNumberInRotateArray(int [] array) {
		int left = 0, right = array.length - 1;
		int mid = 0;
		
		while (left < right) {
			if (left + 1 == right) return Math.min(array[left], array[right]);
			mid = left + (right - left) / 2;
			
			//先判断特殊情况
			if (array[mid] == array[left] && array[mid] == array[right]){
				return getMinInOrder(array, left, right);
			}
			
			if (array[mid] > array[left] || array[mid] > array[right]) {
				left = mid;
			} else {
				right = mid;
			}  
		}
		return 0;
	}

	//找到第一个递减序列
	private static int getMinInOrder(int[] array, int left, int right) {
		for (int i = left; i + 1 <= right; i++) {
			if (array[i] > array[i + 1]) {
				return array[i+1];
			}
		}
		return 0;
	}

}
```

