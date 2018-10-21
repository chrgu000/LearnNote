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

