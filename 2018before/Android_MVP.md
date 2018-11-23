### MVP模式学习

MVC：

Model:就是JavaBean实体类，用来保存实例数据，以及业务逻辑。

View：程序的UI界面层，负责向用户展示数据以及接收用户的输入（界面展示和用户交互）。

Controller：控制器更新UI界面和数据实例，是2者之间的桥梁。

一般的流程是，View层接收了用户的输入，然后通过Controller去更新实体数据Model，同时，Model的数据有了更新之后也会通过Controller去更新View。(当然有时候View层也可以直接去更新Model）

在MVC中，Activity和Fragment属于View层，用来进行UI界面展示，接受用户的输入，另外还有生命周期的工作，以及一部分业务逻辑，所以经常还承担着一部分Controller的角色，导致V和C耦合在一起，虽然写起来方便，但是维护起来就比较麻烦，而且activity中的业务逻辑代码也不能复用。一般超过1000+的代码维护和功能扩展都比较困难。

以前的activity和Fragment，负责UI刷新和业务交互，同时也会将一些业务逻辑放到activity和Fragment中处理。导致这2个类的代码非常的臃肿和庞大，在进行问题定位和功能扩展时是比较困难的。

MVP做的事情就是将业务逻辑和UI逻辑彻底解耦，核心思想是：

MVP把Activity中的UI逻辑抽象成View接口，把业务逻辑抽象成Presenter接口，Model还是原来的Model。

这样，Activity主要负责响应生命周期，其他主要工作都放到Presenter，和MVC最大的不同就是，Presenter彻底将VIew和Model解耦开，View和Model不会直接打交道，都有经过Presenter这个中间桥梁。

MVP 的Model也用来完成具体的业务操作，网络请求，持久化数据的增删改查等任务，外部数据进行解析转换成APP内部数据，同时Model层不包含任何View的东西。

使用MVP的好处：

1. UI逻辑和业务逻辑分离后acitivity的代码变得简洁，基本只有findview,setListener, init，生命周期处理，以及View接口的实现，activity持有Presenter接口引用，业务功能主要通过是对Presenter接口的调用来实现。代码更易懂，更容易维护，删减功能，业务调整更容易。
2. Presenter可以有多中不太的实现，方便写单元测试的代码，只需要替换Presenter的实现实体类就可以了。
3. 避免Activity的内存泄漏，Android内存泄漏的2大原因：activity和bitmap泄漏。传统的MVC方式，一大堆的异常任务和UI操作都放在Activity，异步任务经常持有activity的引用，这样即使activity已经切到后台，且执行了onDestroy()，但由于引用被异步任务持有，所以无法被GC回收，而activity本身又是占用内存最多的，所以无法回收，可能导致APP内存不够而OOM。



MVP模式的整个核心流程：

（这里Model并没有持有Presenter的引用，而是通过接口回调反馈，接口回调的实现在Presenter）

View与Model并不直接交互，而是使用Presenter作为View与Model之间的桥梁。其中Presenter中同时持有View层的Interface引用以及Model层的引用，而View层持有Presenter层引用，Model层使用了Presenter的一个接口。当View层某个界面需要展示某些数据的时候，首先会调用Presenter层的引用，然后Presenter层会调用Model层请求数据，当Model层数据加载成功之后会调用Presenter层的回调方法通知Presenter层数据加载情况，最后Presenter层再调用View层的接口将加载后的数据展示给用户。



https://juejin.im/post/58870cc2128fe1006c46e39c

http://kaedea.com/2015/10/11/android-mvp-pattern/

https://www.jianshu.com/p/8fb4c0ae006e



