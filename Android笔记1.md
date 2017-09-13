##Android中突发情况的数据保存



- **Activity：**
  
	一般Activity意外被销毁时候采用onSaveInstanceState方法来保存数据，然后在onCreate方法中先判断saveInstance参数是否不为空，再取出保存的值。

	注意onSaceInstanceState方法在按back键时是不被调用的，它的调用是在onPause和onStop之间，并且一定在onStop之前被调用，但是否在onPause之前就不保证了。

	onSaveInstanceState用来保存一些临时的、非永久性的数据。View中页实现了该方法，但前提是要给该View指定id,并且不同的widget还不能共用这个id。

	onPause方法，无论程序在什么情况退出，该方法一定会被调用，且onStop和onDestory方法不一定会被调用，这个特性使得我们可以将一些需要永久保存的数据放在onPause方法中进行保存。

- **fragment：**

	它的生命周期：
	
	onAttach->onCreate->onCreateView->onActivityCreated->
	onStart->onResume->onPause->onStop->onDestoryView->onDestory->onDetach。其中除了onActivityCreated方法外其它方法都是一一对应的。当fragment之间使用replace切换且没有设置返回栈时，它会走完完整的生命周期，从create到destory。如果设置了添加返回栈即ft.addToBackStack，则fragment只会调用onPause、onStop、onDestoryView方法。

	突发情况回收fragment时，对fragment的临时数据进行保存，不能仅仅在onSaveInstanceState方法中，还应该在onDestoryView方法中进行保存。

	对持久性的数据，还是要在onPause方法中进行保存。

	如果fragment不需要被频繁地创建和销毁的话应该调用add,show,hide方法。因为replace会先remove当前的fragment然后add一个新的；add则只添加（isAdd先判断），不会删除已有的。并且调用show、hide方法进行fragment切换时不会调用它们的任何生命周期中的函数。

	在使用hide、show进行切换fragment时候，如果fragment的引用被意外回收，但实体还在，则无法对其hide，就会出现画面重叠现象。解决办法是add时候添加tag。然后每次
	`getFragmentManager().findFragmentByTag(TAG)`
	进行判断。

	再加一个Fragment问题的解决，当Fragment的栈里面有几个fragment的时候，会出现，当你触摸当前fragment的时候，下层的fragment的事件被触发，这是由于Touch事件泄露传到了下层中。解决方法就是拦截onTouch事件.记得注册监听事件。

		@Override  
    	public boolean onTouch(View v, MotionEvent event) {  
        	return true;  
    	} 

 

----------
fragment切换参考代码：
				
	public void switchContent(Fragment from, Fragment to) {
        if (mContent != to) {
            mContent = to;
            FragmentTransaction transaction = mFragmentMan.beginTransaction().setCustomAnimations(
                    android.R.anim.fade_in, R.anim.slide_out);
            if (!to.isAdded()) {    // 先判断是否被add过
                transaction.hide(from).add(R.id.content_frame, to).commit(); // 隐藏当前的fragment，add下一个到Activity中
            } else {
                transaction.hide(from).show(to).commit(); // 隐藏当前的fragment，显示下一个
            }
        }
	}
    

----------

##2次返回键退出程序


	/*
   	* 上一次点击 back 键的时间
   	* 用于双击退出的判断
   	*/ 
	private static long lastBackTime = 0;

	@Override
  	public void onBackPressed() {
	    long currentTime = System.currentTimeMillis();
	    if (currentTime - lastBackTime < BACK_INTERVAL) {
	      	super.onBackPressed();
	    } else {
	      	showToast("双击 back 退出");
	    }
	    lastBackTime = currentTime;
	}


##使用内部viewHolder时声明为static

非静态内部类隐试持有外部类的强引用，此时内部类可以随意调用外部类中的方法和成员变量。使用static定义的内部类相对独立，不能访问外部类的非静态成员，占用资源更少。

将viewHolder定义为static，可以将其与外部类解引用，如果不定义为static，当在viewHolder中执行复杂的逻辑或者做一些耗时的操作，就容易出现内存泄漏。如果是static则不能使用外部类资源，也就避免了相互引用造成的内存泄漏。当然，出现内存泄漏的情况是比较少见的。

主要是防止内存泄漏，用static相当于直接写了一个.java文件，与外部类没有了依赖关系。

但是在stackoverflow答案却是另外一回事：

>If you declare the viewholder as static you can reuse it in other adapters. Anyway, I do not recommend to do it, create a new separated class and use it from multiple places, it does make more sense. One class for one purpose.

>In the case of view holders, this classes will be only used inside the adapter, their instances should not go to the fragment or activity or elsewhere just by definition. This means having it static or non-static, in the case of view holders, is the same.

另一个类似的答案
>By using static it just means you can re-use MyVh in other adapters. If you know for certain that you'll only need MyVh in that one adapter, then you should make it non-static.

>If you will need it in other adapters it may even be better to just create it as a separate class entirely, rather than a nested class.

>**There should be no effects on performance for static vs non-static!**


再说明一下内部类的使用：
不常用的语法：`outer.new MyInner()`;

	class MyOuter {
        class MyInner {
        }
    }
    void use() {
        MyOuter outer = new MyOuter();
        MyOuter.MyInner inner = outer.new MyInner();
    }



	public class MyOuter {
	    static class MyInner {
	    }
	    void use() {
	        //MyOuter outer = new MyOuter();
	        MyOuter.MyInner inner = new MyOuter.MyInner();
	    }
	}