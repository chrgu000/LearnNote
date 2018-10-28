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

#### 7 斐波那契数列 

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

n<=39

数列：0,1,1,2,3,5,8....

思路： F(n) = F(n-1) + F(n-2);

可以使用递归，但是这样如果递归层次太多会出现stackoverflow, 而且效率低，也可以使用一个数组，保存每一次的结果，不用递归计算而是直接从数组中查询，但是这样会比较占用内存空间，所以最佳的策略是使用2个变量保存序列的后2个值，循环求值即可。

```
public class Solution {
    public int Fibonacci(int n) {
    	if (n <= 0) return 0;
    	if (n == 1 || n == 2) return 1;
    	int a1 = 1, a2 = 1, a3 = 0;
    	
    	for (int i = 3; i <= n; i++) {
    		a3 = a2 + a1;
    		a1 = a2;
    		a2 = a3;
    	}
    	return a3;
    }
}
```



#### 8 跳台阶 

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。 

思路：是一个斐波那契数列，推导过程如下：

1. 有2种跳法，一次跳1阶或者2阶，加入第一次跳1阶，那么剩下n-1阶有F(n-1)种跳法，如果第一次跳2阶，那么剩下的n-2阶有F(n-2)种跳法，所以可推导出：

   F(n) = F(n-1) + F(n-2);

   且 F(1) = 1; F(2) = 2.

```
public class Solution {
    public int JumpFloor(int n) {
		if (n <= 0) return 0;
    	if (n == 1) return 1;
    	if (n == 2) return 2;
    	int a1 = 1, a2 = 2, a3 = 0;
    	
    	for (int i = 3; i <= n; i++) {
    		a3 = a2 + a1;
    		a1 = a2;
    		a2 = a3;
    	}
    	return a3; 
    }
}
```



#### 9 变态跳台阶 

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：算是数学推导，第一次分别跳1级，2级，3级......n级。

F(n) = F(n-1) + F(n-2) + F(n-3) + .......+ F(0)

F(n-1) = F(n-2) + ..........+ F(0)

所以， F(n) = F(n-1) + F(n-1) = 2 * F(n-1)。

```
public class Solution {
    public int JumpFloorII(int n) {
		if (n == 0 || n == 1) return 1;
		
		int a = 1;
		for (int i = 2; i <= n; i++) {
			a = a * 2;
		}
		return a;
	}
}
```



#### 10 矩形覆盖 

我们可以用2 * 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？ 

策略：

1.对于n = 0的大矩形，方法有1种。

2.对于n = 1的大矩形 2 * 1，方法有1种

3.对于n = 2的大矩形 2 * 2，方法有2种，小矩形横着放2 * 1或者竖着放 1 * 2。

4.对于n = n的大矩形 2 * n，如果第一次放 1 * 2，则剩下的有F(n-1)种方法，如果第一次放 2 * 1,则剩下的有F(n-2)种方法。

结论： F(n) = F(n-1) + F(n-2)



#### 11 二进制中1的个数 

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。 

思路：一种直观的方法，对整数的32位依次相与，判断结果是否为1，为1就累加一次。这种需要32次循环；另一种方法是，`n & (n -1)`可实现将整数n的二进制表示的最后一个1清零，例如二进制数：n = 101100，减1后的结果是：n - 1 = 101011，相与后 n & (n - 1) 是：101000，最后一个1以及其后的二进制位在减1后相当于在原来的基础上取反了， 100 ----> 011，这样这一部分相与后就变成了 000，很优雅地将最后一个1转换成0.

```
public class Solution {
	public int  NumberOf1(int n) {
		int count = 0;
		while (n != 0) {
			count++;
			n = n & (n -1);
		}
		return count;
	}
}
```

```
public class Solution {
    public int  NumberOf1(int n) {
		int count = 0;
		int flag = 1;
		while (flag != 0) {
			if ((flag & n) != 0) count++;
			flag = flag << 1;
		}
		return count;
	}   
}
```



#### 12 数值的整数次方 

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。 



思路：主要需要考虑几种情况，1. exp = 0;     2. exp > 0;     3. exp < 0;     4. base = 0,且exp < 0无效。

求次方的方法，最简单的是对n次方进行n次循环相乘，

也可以这样：

n 为偶数：x（n） =  x (n/2) * x(n/2)

n为奇数：x（n） =  x (n/2) * x(n/2)  * x

时间复杂度logn

```

import java.util.*;
public class Solution {
	static public double Power(double base, int exponent) {
		if (exponent == 0) return 1;
		if ((base < 0.000001 && base > -0.000001) && exponent < 0) {
			throw new RuntimeException("非法参数");
		}
		int absExp = Math.abs(exponent);
		double ret = getP(base, absExp);
		if (absExp % 2 == 1) ret *= base;
		
		if (exponent > 0) return ret;
		return 1 / ret ;
	}
	
	static double getP(double base, int exp) {
		if (exp == 1) return base;
		double ret = getP(base, exp / 2) * getP(base, exp / 2);
		return ret;
	}
}
```



#### 13 调整数组顺序使奇数位于偶数前面 

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。 

思路：最直观的算法是创建一个大小n的数组，对原数组遍历2次，第一次依次放入奇数到新数组，第二次放偶数。时间复杂度O(n),空间复杂度O(n)。

 另一种算法，遍历数组，找到奇数，然后判断它前面的数是否为偶数，如果是就交互，如果不是就停止，然后继续遍历数组，类似于插入排序。

```
public class Solution {//使用类似插入排序的算法，将奇数一个个向前移动。
    public void reOrderArray(int [] array) {
		for (int i = 1; i < array.length; i++) {
			int k = i;
			for ( ; k >= 1; k--) {
				if (array[k] % 2 == 1 && array[k-1] % 2 == 0) {
					int t = array[k];
					array[k] = array[k-1];
					array[k-1] = t;
				} else {
					break;
				}
			}
		}
	}
}
```



#### 14 链表中倒数第k个结点 

输入一个链表，输出该链表中倒数第k个结点。 

思路：使用2个指针，初始指向头结点，然后让其中一个先走k-1步，然后2个指针同时向后遍历，直到有一个指针走到头，那么另一个指针指向的位置就是倒数第k个节点。

```
/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
		if (head == null || k <= 0) return null;
		
		ListNode fastNode = head;
		ListNode slowNode = head;
		
		for (int i = 0; i < k - 1; i++) {
			if (fastNode.next == null) return null;
			fastNode = fastNode.next;
		}
		
		//fast指向最后一个节点
		while (fastNode.next != null) {
			fastNode = fastNode.next;
			slowNode = slowNode.next;
		}
		return slowNode;
	}
}
```

#### 15 反转链表 

输入一个链表，反转链表后，输出新链表的表头。 

思路：反转链表需要有3个节点配合，上一节点，当前节点，保存下一节点：pre, cur, next；

1. cur的next指向pre,  这一步之前需要用next保存下cur的next节点。
2. pre 指向cur, cur指向之前保存的next. 其实next指针就是用来暂存当前指针的下一节点。
3. 继续1的步骤。直到cur指向null，那么pre就是新的头节点。

```
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null) return null;
		ListNode pre = null;
		ListNode cur = head;
		ListNode next = cur.next;
		
		while (cur != null) {
			next = cur.next;
			cur.next = pre;
			pre = cur;
			cur = next;
		}
		
		//此时cur为空，所以pre才是指向原链表的最后一个节点，也就是新链表的头结点
		return pre;
	}
}
```



#### 16 合并两个排序的链表 

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。 

思路：分别遍历并比较2个链表的节点，先在新链表中插入值小的节点，如果其中一个链表空了，就直接将另一个链表插入到新链表的结尾。可以使用递归和非递归2种算法。

```
// 递归版本
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
		if (list1 == null) { //list1已经遍历结束，没有节点了
			return list2;
		}
		if (list2 == null) { //list2已经遍历结束，没有节点了
			return list1;
		}
		
		ListNode head;
		if (list1.val < list2.val) {
			head = list1;
			head.next = Merge(list1.next, list2);
		} else {
			head = list2;
			head.next = Merge(list1, list2.next);
		}
		
		return head;
	}
}
```

```
//递归版本
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
		if (list1 == null) { //list1为空，返回list2
			return list2;
		}
		if (list2 == null) { 
			return list1;
		}
		
		ListNode head, cur;
		
		//确认头结点
		if (list1.val < list2.val) {
			head = list1;
			list1 = list1.next;
		} else {
			head = list2;
			list2 = list2.next;
		}
		
		cur = head;
		
		//遍历2个链表
		while (list1 != null && list2 != null) {
			if (list1.val < list2.val) {
				cur.next = list1;
				cur = cur.next;
				list1 = list1.next;
			} else {
				cur.next = list2;
				cur = cur.next;
				list2 = list2.next;
			}
		}
		
		//插入剩余非空的链表到新链表结尾
		if (list1 == null) {
			cur.next = list2;
		} else if (list2 == null) {
			cur.next = list1;
		}
		
		return head;
	}
}
```



#### 17 树的子结构 

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构） 

思路：首先要有个API（isTree1HasTree2）来判断，tree1是否包含tree2，并且从各种的根节点开始比较，分别遍历其左右子节点，如果遇到不相等的节点，则返回false，如果tree2先遍历完了则说明tree1包含了tree2，返回true, tree1先遍历到空节点则返回false。

之后对TreeA , 遍历各个节点，找到值和TreeB 根节点相等的节点，然后调用API进行判断。

```
public class Solution {
    
	static public boolean HasSubtree(TreeNode root1,TreeNode root2) {
		boolean ret = false;
		// 注意这里的判断算法，之前写错过。对当前节点、左子节点、右子节点 要依次进行判断，不能采用if else的逻辑关系
		if (root1 != null && root2 != null) {
			if (root1.val == root2.val) ret = isTree1HasTree2(root1, root2);
			 
			if (!ret) ret = HasSubtree(root1.left, root2);
			if (!ret) ret = HasSubtree(root1.right, root2);
		}
		
		return ret;
	}
	
	static private boolean isTree1HasTree2(TreeNode tree1, TreeNode tree2) {
		if (tree2 == null) return true;
		if (tree1 == null) return false;
		
		if (tree1.val != tree2.val) return false;
		return isTree1HasTree2(tree1.left, tree2.left)
				&& isTree1HasTree2(tree1.right, tree2.right); 
	}
}
```



#### 18 二叉树的镜像 

题目描述

操作给定的二叉树，将其变换为源二叉树的镜像。

输入描述:

```
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
```
思路：前序遍历树，如果一个节点的左 子树和右子树都不为空，则交换他们。交换完成后就得到了它的镜像。可以使用递归算法和非递归算法。

```
/**
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;
    }

}
*/
//递归算法
public class Solution {
    public void Mirror(TreeNode root) {
		if (root == null) return ;
		if (root.left == null && root.right == null) return;
		
		TreeNode temp = root.left;
		root.left = root.right;
		root.right = temp;
		
		Mirror(root.left);
		Mirror(root.right);
	}
}
```

```
//非递归算法，层次遍历
import java.util.*;
public class Solution {
    public void Mirror(TreeNode root) {
		if (root == null) return;
		Stack<TreeNode> stack = new Stack<>();
		stack.push(root);
		
		while (!stack.isEmpty()) {
			TreeNode cur = stack.pop();
			
			if (cur.left == null && cur.right == null) continue;
			
			TreeNode temp = cur.left;
			cur.left = cur.right;
			cur.right = temp;
			
			if (cur.left != null) stack.push(cur.left);
			if (cur.right != null) stack.push(cur.right);
		}
	}
}
```



#### 19  顺时针打印矩阵

​    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10. 

思路：可以对顺时针遍历矩阵的4个边，做好边界控制，但这个算法实现起来有点复杂，对边界的控制要求比较高。所以可以换一种方式，

1. 每次只打印矩阵的第一行，然后将第一行删除
2. 对矩阵的剩余部分做逆时针90度的选择，之后重复1,2步骤。

但这种算法的缺点是占用一定的内存，每次矩阵变换都要创建新的矩阵。

```
import java.util.*;

public class Main {
	public static void main(String[] args) {
		print(matrix);
		print(convertMatrix(matrix));
		System.out.println(printMatrix(matrix2));
	}
	
	static int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
	static int[][] matrix2 = {{1,2},{3,4}};
	static void print(int[][] matrix) {
		if (matrix == null) return;
		for (int[] row : matrix) {
			System.out.println(Arrays.toString(row));
		}
	}
	
	static ArrayList<Integer> ret;
	static public ArrayList<Integer> printMatrix(int [][] matrix) {
		if (matrix == null || matrix.length == 0) return null;
		
		ret = new ArrayList<>();
		int[][] tempM = matrix;
		while (tempM != null && tempM.length > 0) {
			popFirstRow(tempM);
			tempM = convertMatrix(tempM);
		}
		return ret;
	}
	
	/**
	 * 读取第一行
	 * @param matrix
	 */
	static private void popFirstRow(int [][] matrix) {
		if (matrix == null || matrix.length == 0) return;
		int row = matrix.length;
		int column = matrix[0].length;
		
		if (matrix.length > 0) {
			for (int i = 0; i < column; i++) {
				ret.add(matrix[0][i]);
			}
		}
	}
	
	/**
	 * 矩阵转换：删除第一行，然后将矩阵逆时针旋转90
	 * 1 2 3
	 * 4 5 6
	 * 7 8 9 
	 * 转成
	 * 6 9
	 * 5 8
	 * 4 7
	 * @param matrix
	 * @return
	 */
	static private int[][] convertMatrix(int [][] matrix) {
		if (matrix == null || matrix.length <= 1) return null;
		int row = matrix.length;
		int column = matrix[0].length;
		
		int newColumn = row - 1;
		int[][] retM = new int[column][newColumn];
		
		int id = 0;
		for (int i = column - 1; i >= 0; i--) {//从最后一列开始遍历，忽略第一行
			for (int j = 1; j < row; j++) {
				retM[id/newColumn][id%newColumn] = matrix[j][i];
				id++;
			}
		}
		return retM;
	}	
}
```

上一个算法对空间比较浪费，那么边界遍历算法如下：

```
import java.util.ArrayList;
public class Solution {
    static ArrayList<Integer> ret = new ArrayList<>();
	
    static public ArrayList<Integer> printMatrix(int [][] matrix) {
		if (matrix == null || matrix.length == 0) return null;
		
		ret = new ArrayList<>();
		int row = matrix.length;
		int column = matrix[0].length;
		
		travelMatix(matrix, 0, 0, row-1, column-1);
		return ret;
	}
	
	//注意x并不对应行，column,y也并不对应列row
	static void travelMatix(int[][] matrix, int top, int left,
			 int bottom, int right) {
		if (top > bottom || left > right) return;
		
		//保存行不变，列递增
		for (int i = left; i <= right; i++) ret.add(matrix[top][i]);
		
		//保存列不变，行递增
		for (int i = top + 1; i <= bottom; i++) ret.add(matrix[i][right]);
		
		//保存行不变，列递减, 注意需要加约束条件：top < bottom
		for (int i = right - 1; i >= left && top < bottom; i--) ret.add(matrix[bottom][i]);
		
		//保存列不变，行递减  注意需要加约束条件：left < right
		for (int i = bottom - 1; i >= top + 1 && left < right; i--) ret.add(matrix[i][left]);
		
		travelMatix(matrix, top+1, left+1, bottom-1, right-1);
	}
}
```

其中后面的一个递归可以改成非递归

```
static void travelMatix(int[][] matrix, int top, int left,
		 int bottom, int right) {
	while (top <= bottom && left <= right) {
		//保存行不变，列递增
		for (int i = left; i <= right; i++) ret.add(matrix[top][i]);
		
		//保存列不变，行递增
		for (int i = top + 1; i <= bottom; i++) ret.add(matrix[i][right]);
		
		//保存行不变，列递减, 注意需要加约束条件：top < bottom
		for (int i = right - 1; i >= left && top < bottom; i--) ret.add(matrix[bottom][i]);
		
		//保存列不变，行递减  注意需要加约束条件：left < right
		for (int i = bottom - 1; i >= top + 1 && left < right; i--) ret.add(matrix[i][left]);
		top++; left++; bottom--; right--;
	}
}
```



#### 20 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。 

 思路：使用2个栈，一个正常使用，另一个放置当前的最小值，push的时候先判断待存入的数值和当前最小栈的栈顶值的关系，如果小于就直接压人，如果大于则将栈顶值重复压入。

```
import java.util.Stack;

public class Solution {
	Stack<Integer> minStack = new Stack<>();
	Stack<Integer> mainStack = new Stack<>();
	
	public void push(int node) {
        mainStack.push(node);

        if (minStack.isEmpty()) {
        	minStack.push(node);
        	return;
        }
        
        int curMin = minStack.peek();
        if (node < curMin) {
        	minStack.push(node);
        } else {
			minStack.push(curMin);
		}
    }
    
    public void pop() {
        if (!mainStack.isEmpty()) {
        	mainStack.pop();
        	minStack.pop();
        }
    }
    
    public int top() {
        return mainStack.peek();
    }
    
    public int min() {
        return minStack.peek();
    }
}
```



#### 21 栈的压入 弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的） 

思路：模拟栈的压入和弹出过程即可，对序列A {1,2,3,4,5}，依次入栈，并每次将栈顶值和序列B {4,5,3,2,1}的首个数字比较，如果不相等则A继续入栈，如果相等，则A的栈顶值出栈，同时将B中刚才判断相等的值从B序列移除。并继续比较栈顶和B序列的值，直到栈为空，如果此时B序列也空了则表示B是弹出序列，否则不是。

举例：

入栈1,2,3,4,5

出栈4,5,3,2,1

首先1入辅助栈，此时栈顶1≠4，继续入栈2

此时栈顶2≠4，继续入栈3

此时栈顶3≠4，继续入栈4

此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，,辅助栈里面是1,2,3

此时栈顶3≠5，继续入栈5

此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，,辅助栈里面是1,2,3

```
import java.util.*;

public class Solution {
    static public boolean IsPopOrder(int [] pushA, int [] popA) {
		if (pushA == null || popA.length == 0) return false;
		Stack<Integer> stack = new Stack<>();
		
		int idPop = 0;

		for (int i = 0; i < pushA.length; i++) {
			stack.push(pushA[i]);
			
			while (!stack.empty() && stack.peek() == popA[idPop]) {
				idPop++;
				stack.pop();
			}
		}
		return stack.empty();
	} 
}
```

#### 22 从上往下打印二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。 

思路：借助一个队列，

1. 先将根节点入队，然后依次取出队列的头节点，打印

2. 之后将取出头结点的子节点插入到队列后面即可。 重复1,2

```
public class Solution {
    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
		ArrayList<Integer> ret = new ArrayList<>();
		if (root == null) return ret;
		
		Queue<TreeNode> queue = new ArrayDeque<>();
		queue.offer(root);
		while (!queue.isEmpty()) {
			TreeNode node = queue.poll();
			ret.add(node.val);
			
			if (node.left != null) queue.offer(node.left);
			if (node.right != null) queue.offer(node.right);
		}
		
		return ret;
	}
}
```



#### 23 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。 

树的相关概念：

二叉树（Binary tree）：一种特殊的树类型，每个节点最多有2个子节点，满二叉树，完全二叉树。

满二叉树：一颗深度为n，节点数为2的n次方 - 1 的树是满二叉树。

完全二叉树：树中每个节点的编号和相同深度的满二叉树中节点编号一一对应

二叉搜索树/查找树（BST  binary search tree）的特征：左子节点 <  根节点 < 右子节点，任意2个节点值不相等。

自平衡二叉查找树 （self-balancing Binary search tree）：一种改进的二叉查找树，其左右子树的高度差绝对值不超过1。常用的实现方法用：AVL、红黑树（Red-black tree）。

二叉搜索树的后序遍历序列满足：最后一个值是根节点，根节点之前的序列可分为2个部分，左子树和右子树，其中左子树的值都要小于根节点，而根节点的值小于右子树的值。根据这个条件可以判断是否为合法序列。

实现方：

1. 找出根节点值root
2. 找出根节点前面序列中第一个大于root的值value，即为右子树的第一个值
3. 判断value之后的序列中是否有小于等于root的值，存在则返回false.

```
public class Solution {
    static public boolean VerifySquenceOfBST(int [] sequence) {
        if (sequence == null || sequence.length == 0) return false;
        
        return isSeqOfBst(sequence, 0, sequence.length - 1);
	}
	
	static public boolean isSeqOfBst(int[] seq, int left, int right) {
		if (left >= right) return true;
		int root = seq[right];
		
		int rId = left; //对rId进行自增，如果没有右子树，rId应该指向最后
		for ( ; rId < right; rId++) {
			if (seq[rId] >= root) {
				break;
			}
		}
		
		for (int i = rId; i < right; i++) {
			if (seq[i] <= root) {
				return false;
			}
		}
		
		return isSeqOfBst(seq, left, rId - 1) && isSeqOfBst(seq, rId, right - 1);
	}
}
```



#### 24 二叉树中和为某一值的路径 

输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前) 

思路：采用dfs算法，递归每一个路径，计算每个路径的和，然后判断是否和目标值相等。

```
public class Solution {
    ArrayList<ArrayList<Integer>> listAll = new ArrayList<>();
	ArrayList<Integer> list = new ArrayList<>();
	
	public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
        if (root == null) return listAll;
        list.add(root.val);
        target -= root.val;
        
        if (target == 0 && root.left == null && root.right == null) {
        	listAll.add(new ArrayList<>(list));
        }
        FindPath(root.left, target);
        FindPath(root.right, target);
        list.remove(list.size() - 1);
        return listAll;
    }
}
```

dfs显示算法：

```
public class Solution {
    ArrayList<ArrayList<Integer>> listAll = new ArrayList<>();
	ArrayList<Integer> list = new ArrayList<>();
	
	public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
        if (root == null) return listAll;
        dfs(root, target);
        
        return listAll;
    }
	
	void dfs(TreeNode node, int target) {
		if (node == null) return;
		
		target -= node.val;
		list.add(node.val);
		if (target == 0 && node.left == null && node.right == null) {
			if (target == 0) listAll.add(new ArrayList<>(list));
			//这里不能直接return，需要remove叶节点
		}
		
		dfs(node.left, target);
		dfs(node.right, target);
		
		list.remove(list.size() - 1);
	}
}
```



#### 25  复杂链表的复制 

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空） 

思路：

1. 复制链表中的每个节点，在旧节点后插入一个新节点。
2. 复制每个旧节点的random指针，clone.random = old.random.next；
3. 拆分链表，将1中复制的新节点拆分成一个新的链表。

代码：

```
public class Solution {
    public RandomListNode Clone(RandomListNode pHead)
    {
		if (pHead == null) return null;
		
        //1. 再旧链表中复制新的链表：A ---> A1 ---> B ---> B1,A1 B1为复制的节点
		RandomListNode node = pHead;
		while (node != null) {
			//node复制
			RandomListNode cloneNode = new RandomListNode(node.label);
			RandomListNode tmpNext = node.next;
			
			node.next = cloneNode;
			cloneNode.next = tmpNext;
			
			//node后移，遍历
			node = tmpNext;
		}
		
		//2. 设置 A1 B1的随机节点  A1.random = A.random.next
		node = pHead;
		while (node != null) {
			RandomListNode rNode = node.random;
			
			//随机节点赋值
			node.next.random = (rNode == null ? null : rNode.next);
			
			//node后移，遍历
			node = node.next.next;
		}
		
		
		//3、拆分链表，将链表拆分为原链表和复制后的链表
        node = pHead;
        RandomListNode pNewHead = node.next;
        while (node != null) {
        	RandomListNode cloneNode = node.next;
        	node.next = cloneNode.next;
        	cloneNode.next = (cloneNode.next == null ? null : cloneNode.next.next);
        	
        	node = node.next;
        }
         
        return pNewHead;
    }
}
```



#### 26 二叉搜索树与双向链表 

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。 

思路：对二叉搜索树，进行中序遍历，其序列就是一个递增的排序序列，所以需要对二叉树进行中序遍历，在遍历的同时，将其改成双向链表即可。需要保存上一个链表节点。

```
public class Solution {
    //二分二叉树的中序遍历结果就是一个递增序列，只需要保存上一次节点即可
	TreeNode head,  pre;
	public TreeNode Convert(TreeNode pRootOfTree) {
		if (pRootOfTree == null) return null;
		
		converTree(pRootOfTree);
		return head;
	}
	
	public void converTree(TreeNode node) {
		if (node == null) return;
		
		converTree(node.left);
		if (head == null) {//设定链表头部
			head = node;
			pre = node;
		} else {
			node.left = pre;
			pre.right = node;
			pre = node;
		}
		converTree(node.right);
	}
}
```

