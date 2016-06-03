##git中fetch和pull的区别
git中fetch是将远程分支的最新内容拉到了本地，但是fetch后是看不到变化的，switch/checkout查看当前分支，发现此时后本地多了一个`FETCH_HEAD`的指针，checkout到该指针后可以查看远程分支的最新内容。然后checkout到master分支，执行metch,选中`FETCH_HEAD`指针,合并后如果出现冲突则解决冲突，最后commit。

pull的作用就相当于fetch和merge，自动合并：
	
	git fetch origin master
	git merge FETCH_HEAD
然后需要手动解决冲突，并commit。

----------

分支的概念：
分支是用来标记特定代码的提交，每一个分支通过SHA1sum值来标识，所以对分支的操作是轻量级的，你改变的仅仅是SHA1sum值。

如下图所示，当前有2个分支，A,C,E属于master分支，而A,B，D,F属于dev分支。

	A----C----E（master）
     \
	  B---D---F(dev)

它们的head指针分别指向E和F，对上述做如下操作：
	
	git checkout master
	git merge dev

之后的情形是这样的：

	A---C---E---G(master)
	 \         /
      B---D---F（dev）

现在A，B,C,D,E,F,G属于master，G是一次合并后的结果，是将E和Ｆ的代码合并后的结果，可能会出现冲突。而A,B，D,F依然属于dev分支。可以继续在dev的分支上进行开发:

	A---C---E---G---H(master)
	 \         /
      B---D---F---I（dev）
 
理解git`fetch`,关键是理解`FETCH_HEAD`，`FETCH_HEAD`指的是：某个branch在服务器上的最新状态。

一般来说，存在2种情况：

如果没有显示地指定远程分支，则远程分支的master将作为默认的FETCH_HEAD。
如：`git fetch origin`或者`git fetch origin master`

如果指定了远程分支，则将这个远程分支作为`FETCG_HEAD`。
如：`git fetch origin dev`设定当前分支的`FETCG_HEAD`为远程服务器的dev分支。它就相当于`git pull origin dev`的第一步，并不会在本地创建新的分支。另外`git fetch origin dev`这个命令可以用来测试远程分支dev是否存在。

	git fetch origin dev :branch1

上面这个命令的执行过程如下

1. 首先执行上面的fetch操作
2. 使用远程dev分支在本地创建branch1分支（但不会切换到该分支）
3. 如果本地不存在branch1分支，则会自动创建一个新的branch1分支，如果存在branch1分支，并且是`fast forward`，则会自动合并这2个分支，否则会阻止以上的操作。