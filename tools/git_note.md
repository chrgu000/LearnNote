#### Git使用笔记

在公司期间使用Git进行项目开发，现将一些常用的git命令和操作习惯总结一下。一个git的工作原理示意图。

![QQ截图20181020210345](.\markdown_image\QQ截图20181020210345.jpg)

git 个人信息配置，用户名，密码，key等。

首先需要从远程服务器clone工程代码：

`git clone 远程服务器地址和分支名`

如果是本地新建一个git仓库，可以使用

`git init`



##### 一些经常使用的命令：

`git status`   查看当前分支的状态，一般git 显示3个层次的文件状态：

changes to be committed: 已经被add到暂存区的文件，下一步需要commit到本地仓库

changes not staged for commit : 被add过的文件，又再次被修改，这些修改在工作区，还没有被add到暂存区

untracked files: 尚未被add 过的文件，git 还没有对这些文件建立追踪

```
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   small.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   "git\344\275\277\347\224\250\347\254\224\350\256\260.md"
        modified:   "\345\221\250\350\256\260.xlsx"

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        big.txt
```

`git add filename  filename` 添加工作区指定文件修改到暂存区，并建立git对该文件的追踪。

`git add .` 添加工作区所有的修改到暂存区

`git commit -m "msg"` 将暂存区的修改提交到本地仓库，并添加提交信息。

`git commit --amend`   将暂存区的修改**追加提交**上一次也就是最新的commit，同时再次可以修改commit信息。或者理解为使用一个新的提交来覆盖上一次提交。

`git stash`  将工作区和暂存区的修改保存到缓存区，使得当前的分支看起来是干净的。git reset --hard不会清理掉stash的缓存。stash有个副作用就是，add到暂存区的文件修改记录，在stash,stash pop之后会回退到工作区，后续需要再次add。

`git stash pop/apply`  恢复上一次保存到缓存区的修改，使用pop表示在恢复的同时丢弃该缓存，apply恢复并且不丢弃该缓存。

`git reset commit-id`  将当前分支的HEAD指针回退到指定的版本号commit-id, 同时重置暂存区，但工作区的文件修改还在。

`git reset --soft commit-id`  将当前分支的HEAD指针回退到指定的版本号commit-id, 但暂存区和工作区的文件修改还在。

`git reset --hard commit-id`  将当前分支的HEAD指针回退到指定的版本号commit-id, 并重置暂存区和工作区的修改记录。即当前工程和指定版本号commit-id的状态保持一致。

即可以看出，reset对当前工程的修改程度是： --hard > 默认无参  >  --soft，

即 （不保留暂存区、工作区） >  （保留工作区） > （保留暂存区、工作区）

```
commit-id 是下面看到的提交历史的最前面一串数字，相对于每次提交的版本号，是唯一的，用来标识提交历史。
$ git reflog
e251db6 (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: commit: 添加git使用笔记
d7f3dba HEAD@{1}: commit: 添加周记和计划安排
3729513 HEAD@{2}: commit: 添加剑指offer +15道
618da42 HEAD@{3}: commit: 添加笔记
```

`git reset --soft head~n`  将本地仓库进行回退，回退最近的n次提交，只是回退本地仓库的提交，将已经提交到本地仓库修改撤回到暂存区，也就是commit之前的状态，并且工作区的修改也依然还在。

`git reset --hard head~n` 将本地提交进行回退，回退最近的n次提交，和soft不同的是，会丢弃暂存区和工作区的修改，将整个工程彻底回退到最近n次提交前的一次提交的状态。

`git reset  HEAD <file-name>`  to unstage， 撤销暂存区的提交记录，将暂存区修改放回到工作区，可以认为是add的反向操作。

`git revert commit-id`  新建一次提交，用来撤销或者抵销之前commit-id的提交，reset是直接撤销之前的提交记录，revert则是通过生成新的提交来撤销之前的提交。

`git checkout  [file-name]`  丢弃工作区的修改，也就是没有add到暂存区的本地文件修改被清除。

`git branch -a`  查看当前所有分支，保存本地分支和远程分支。

`git branch [branch-name]`  新建一个分支，不切到新分支，而是保持在现有分支。

`git checkout -b  branchB`   新建一个名字为branchB, 并切换到该分支。

`git checkout [branch-name]`   切换到[branch-name]这个分支。

`git branch -d [branch-name]`  删除分支[branch-name]。

`git branch --track local-branch  remote-branch`  新建一个本地分支，和远程分支 remote-branch建立追踪关系。

`git log` 查看当前分支的提交记录

`git log --author=name`  查看指定提交者的提交记录

`git log -n 10`  查看当前分支最近10次的提交记录

`git reflog` 查看所有的操作记录（包括commit和reset），比git log 查到更多的信息，log无法查看被删除的commit记录，但reflog则可以，同样支持 -n 参数。`

`git cherry-pick  commit-id`， 一般是将其他分支提交id为： commit-id 的提交合并到当前的分支上，可能会有冲突，修改冲突即可。

`git diff`  查看本地工作区的修改，一般是工作区和暂存区之间的差异

`git diff --cached`   查看暂存区的修改，一般是暂存区和上一次提交之间的差异

`git diff head`  显示工作区和最新commit之间的差异

`git pull`  从远程库读取最新的修改，并合并到本地，如果本地仓库和远程仓库的修改保存一致(3个区一致)，则不会出现合并，而是fast forward, 不一致则会生成一次merge 的commit。

`git push`  将本地仓库的commit 记录更新到远程仓库，前提是本地仓库除了待提交的commit，其他的commit和远程仓库要一致。

`git rm <file-name>` 删除工作区的文件，同时将删除记录同步到暂存区。一般需要加 -f ，强制删除。 对add到暂存区的文件，直接使用git rm 会报错，需要添加 -f 参数。

```
Administrator@ASUS-20161206WK MINGW64 /g/GitHub/LearnNote (master)
$ git add small.txt

Administrator@ASUS-20161206WK MINGW64 /g/GitHub/LearnNote (master)
$ git rm small.txt
error: the following file has changes staged in the index:
    small.txt
(use --cached to keep the file, or -f to force removal)

Administrator@ASUS-20161206WK MINGW64 /g/GitHub/LearnNote (master)
$ git rm -f small.txt
rm 'small.txt'
```

`git rm --cached <file-name>`  停止追踪文件，但文件会保留在工作区，相当于add的反向操作。

`rm <file-name>`  删除工作区的文件，是原生Dos命令。





##### 不常用命令

`git pull 远程主机名  远程分支名：本地分支名` pull 命令的完整格式，取回远程主机某个分支的内容，和本地指定分支进行合并。

如果当前分支和远程分支存在追踪关系，并且当前分支只对应了一个追踪分支，那么就可以简化为 `git pull`

`git push 远程主机名  本地分支：远程分支` push命令的完整格式，将本地分支的更新推送到远程主机的指定分支，如果省略远程分支名，则表示将本地分支推送到与之有追踪关系的远程分支，一般2者同名，如果后者即远程分支不存在，则会新建一个， 如下：

`git push origin master`  将本地master分支推送到与之有追踪关系远程主机分支上，如果远程分支不存在，就创建一个。

如果本地分支不存在，则表示要删除指定的远程分支，相当于推送了一个空分支到远程分支，如下：

`git push origin  :master` 删除远程的master分支。

如果当前本地分支有存在追踪关系的远程，且只有一个远程分支，那么该命令可简化为 `git push`



##### 提交代码

一般我在将本地代码提交到远程仓库的时候，会先不commit到本地，最好本地提交和远程仓库一致，这样在git pull的时候可以fast foward。如果已经本地提交了，则需要使用 `git reset --soft head~n`，先将本地commit回退，将修改记录放在暂存区和工作区。然后，使用`git stash` 将工作区和暂存区的修改保存到缓存区，使得当前的分支看起来是干净的，和远程库保持一致，如果之前有和远程库不一致本地提交，并且不需要保留，则需要使用 `git reset --hard head~n`，将分支回退n个本地提交， 然后在git pull 这时候会出现fast forward。

接下来依次 `git stash pop,  git add , git commit ,git push` 即可。



##### 不同分支的反合代码方法

需求：需要将本地分支master的某次提交合并远程仓库的dev分支。

首先确认是否有本地分支和待反合的远程分支呈追踪关系，如果没有则新建本地分支并建立追踪关系：

`git branch --track <local-branch>  <romote-branch>`  

这里本地分支也命名为 dev， 通过git log 或者 git reflog（可以借助 --author=name） 查看master分支需要返合的提交，记录对应的commit-id, 切换到本地dev 分支，

`git cherry-pick commit-id`

将标记位commit-id的提交合并到dev 分支上，如果有冲突则处理冲突，如果没有冲突会自动生成一次新的提交。



##### 修改冲突方法

修改合并提交冲突的原因是本次提交的修改和已有的提交修改了同一处代码，git 不知道要按照哪一次的修改为准，所以产生了冲突，修改冲突的过程如下：

git status 查看是哪些文件被同时修改并产生冲突。

找到冲突文件，搜索 >>>  符合，一般是这样的格式：

```
<<<<<<< HEAD
Creating a new branch is quick & simple. //表示原来本地的代码
=======
Creating a new branch is quick AND simple. //表示新的commit修改的代码
>>>>>>> feature1
```

根据实际需求将冲突修改，然后 git add , commit 。



##### 将本地的git仓库push到gitHub:

1. 首先将本机的ssh key添加到gitHub的ssh key设置中

    C:\Users\\{username}\\.ssh\id_rsa.pub ---> gitHub--ssh---key

2. 在gitHub中新建一个仓库，复制其https的链接地址

3. 在本地git仓库中，绑定远程仓库地址

    `git remote add origin https://github.com/zhhtao89/MavenSpringBootLearn.git`

   如果绑定错了，重新绑定前需要先接触之前的绑定：

   `git remote remove origin`

4. 在push前，如果远程仓库不是空的，那么需要先rebase： `git pull --rebase origin master`

5. push并进行分支绑定，不然无法push: `git push --set-upstream origin master`

   ​	（PS:网上使用`git push -u master origin`）

6. 之后即可正常操作。



#### Git merge

有2种场景，

第一种，只修改指针，不创建新的`commit`：

当我们创建新的分支，例如`dev`时，Git新建了一个指针叫`dev`，指向`master`相同的提交，再把`HEAD`指向`dev`，就表示当前分支在`dev`上：

![1542359635018](.\markdown_image/1542359635018.png)

你看，Git创建一个分支很快，因为除了增加一个`dev`指针，改改`HEAD`的指向，工作区的文件都没有任何变化！

不过，从现在开始，对工作区的修改和提交就是针对`dev`分支了，比如新提交一次后，`dev`指针往前移动一步，而`master`指针不变：

![微信截图_20181116171810](.\markdown_image/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181116171810.png)

假如我们在`dev`上的工作完成了，就可以把`dev`合并到`master`上。Git怎么合并呢？最简单的方法，就是直接把`master`指向`dev`的当前提交，就完成了合并：

![微信截图_20181116171934](.\markdown_image/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181116171934.png)



第二种，要合并的分支和当前分支有差异，需要新建一个提交。

假设下面的历史节点存在，并且当前所在的分支为`master`：

![微信截图_20181116172254](.\markdown_image/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181116172254.png)

那么

```
git merge topic
```

命令将会把在master分支上二者共同的节点（E节点）之后分离的节点（即topic分支的A B C节点）重现在master分支上，直到topic分支当前的commit节点（C节点），并位于master分支的顶部。并且沿着master分支和topic分支创建一个记录合并结果的新节点，该节点带有用户描述合并变化的信息。

> 即下图中的H节点，C节点和G节点都是H节点的父节点。

![1542360212219](.\markdown_image/1542360212219.png)





参考链接：

http://www.ruanyifeng.com/blog/2014/06/git_remote.html

http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html