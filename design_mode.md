#### 设计模式的六大基本原则

1.单一职责原则：一个类只负责一项职责，且只有一个引起它变化的原因。职责太多会影响其复用性，且其中一个职责变化时，可能会影响其他职责的正常运行，所以需要将职责分离，封装在不同的类中。例如：实现界面和逻辑功能分离。

2.里氏替换原则：任何父类出现的地方，都可用替换成其子类，子类可以扩展父类功能，但不能改变父类功能。在定义时尽量使用父类，实际使用时再确定具体的子类，是实现开闭原则的重要方法之一。

3.依赖倒置原则：核心思想是面向接口编程，依赖抽象，而不是依赖具体，相对细节的多变性，抽象要稳定很多，以抽象为基础搭建的框架要比以细节为基础搭建起来的框架稳定得多。要对抽象进行编程，不对实现进行编程，降低客户和具体实现模块之间的耦合。

Java排序Collections.sort()方法传入参数List类型，这样就可以对ArrayList和LinkList分别进行排序实现。

4.接口隔离原则：使用多个功能单一的接口，而不是一个总接口，客户不应该依赖那些它不需要的接口。降低依赖，降低耦合，接口要适度，不能太大或者太小。

其一，单一职责原则原注重的是职责；而接口隔离原则注重对接口依赖的隔离。其二，单一职责原则主要是约束类，其次才是接口和方法，它针对的是程序中的实现和细节；而接口隔离原则主要约束接口接口，主要针对抽象，针对程序整体框架的构建。

5.迪米特法则：（最少知道原则）一个软件实体应尽量少和其他软件实体进行交互，使得系统功能模块相对独立，这样当一个模块修改后，就会尽量少的影响到其他模块，扩展也会更容易；即一个对象应该对其他对象保持最少的了解。类之间关系越复杂，耦合度越高，一个类改变时，对其他类的影响也越大。一个类应该尽量把逻辑封装在内部，除了对外提供public方法外，不对外泄露任何信息。

低耦合，高内聚，可以通过中间类来降低多个类之间的耦合度。

6.开闭原则：软件应该尽量在不修改原有代码的情况下，进行扩展实现新的功能。对扩展开发，对修改关闭，实现热插拔的效果，便于维护和升级，用抽象构建框架，用实现扩展细节。用抽象搭建框架，用实现扩展细节。

7.组合/聚合复用原则：尽量使用组合和聚合，少用继承来实现类的复用。在新对象里通过关联关系（成员变量）使用一些已有的对象，新的对象通过委派调用已有对象的方法来实现功能复用的目的。



UML表示方法：

https://www.cnblogs.com/scevecn/p/5663369.html



#### 1 策略模式

定义算法族，将变化的算法抽象封装起来，使其之间可以相互替换，对用户来说它是感知不到算法的变化的。

Demo代码：

```
//抽象行为方法接口
interface IFlyBehavior {
	void fly();
}

//具体实现方法
class FlyWithWings implements IFlyBehavior {
	@Override
	public void fly() {
		System.out.println("fly with wings");
	}
}
 class FlyNoWay implements IFlyBehavior {
	 @Override
	public void fly() {
		 System.out.println("fly no way");
	}
 }
 
 abstract class Duck {
	 IFlyBehavior mFlyBehavior;//持有行为接口引用
	 
	 public void setFlyBehavior(IFlyBehavior flyBehavior) {
		 mFlyBehavior = flyBehavior;
	 }
	 
	 public void fly() {
		 mFlyBehavior.fly();//委托给行为类
	 }
 }
```



#### 2 观察者模式

定义了对象之间一对多的依赖，这样一来，当一个对象改变时，它的所以依赖者都会受到通知并自动更新。更新可以被动接受也可以主动持有subject查询。

1个subject，多个observer， observer向subject订阅，subject内部维护了一个List,用来添加或者移除观察者，当subject的数据改变时，就遍历List, 调用observer的接口，通知他们更新数据了。

```
interface Observer {
	void update(Subject sub);//在子类中去主动查询数据，
	或者此处传入需要通知的参数
}

interface Subject {
	public void registerObserver(Observer ob);
	public void removeObserver(Observer ob);
	public void notifyObservers();
}

class SubjectImpl implements Subject {
	List<Observer> observerList = new ArrayList<>();
	
	public void registerObserver(Observer ob) {
		observerList.add(ob);
	}
	
	public void removeObserver(Observer ob) {
		observerList.remove(ob);
	}
	
	public void notifyObservers() {
		for (Observer observer : observerList) {
			observer.update(this);
		}
	}
}
```



#### 3 装饰者模式

动态地将职责附加到对象上，如果要扩展功能，提供了比继承更有弹性的替代方案。

需要满足以下条件：

1. 装饰者和被装饰者继承相同的超类Super，原因：因为装饰者内部持有超类的引用，通过该引用委托调用API，如果装饰者也是Super的子类，那么装饰者就可以去装饰其他的装饰者了。
2. 装饰者持有被装饰者的引用，委托调用其API，装饰者在调用API前后可以添加自己的行为。
3. 装饰者可以无限装饰装饰者或者被装饰者。

```
public class DecoratorDemo {
	public static void main(String[] args) {
		IComponet sub = new ComponetImpl(); //被装饰者
		IComponet decoratorA = new ConcreteDecoratorA(sub);
		decoratorA.fun();
		System.out.println("----------");
		IComponet decoratorB = new ConcreteDecoratorB(decoratorA);
		decoratorB.fun();
	}
	
}

abstract interface IComponet {
	void fun();
}

class ComponetImpl implements IComponet {
	@Override
	public void fun() {
		System.out.println("我是被装饰者");
	}
}

abstract class Decorator implements IComponet {
	IComponet obj;
	public Decorator(IComponet obj) {
		this.obj = obj;
	}
	
	//具体的装饰者子类需要覆盖该方法，在obj.fun()之前或之后加入新的逻辑
	@Override
	public void fun() {
		obj.fun();
	}
}

class ConcreteDecoratorA extends Decorator {
	public ConcreteDecoratorA(IComponet obj) {
		super(obj);
	}

	@Override
	public void fun() {
		System.out.println("我是装饰者，前面添加功能----A");
		obj.fun();
	}
}

class ConcreteDecoratorB extends Decorator {
	public ConcreteDecoratorB(IComponet obj) {
		super(obj);
	}

	@Override
	public void fun() {
		obj.fun();
		System.out.println("我是装饰者，后面添加功能----B");
	}
}


输出结果：
我是装饰者，前面添加功能----A
我是被装饰者
----------
我是装饰者，前面添加功能----A
我是被装饰者
我是装饰者，后面添加功能----B
```



#### 4 工厂模式

##### 1 简单工厂模式

简单工厂其实不算是一个设计模式，而是一种编程习惯，就是把一些对象的创建工作移到另一个对象Factory中，由Factory来专职负责创建类，并处理创建对象的细节，对象的使用客户不关心对象的具体创建过程。

1. 创建对象的方法一般声明为static类，
2. 返回的对象类型通常是基类。

```
public class FactoryDemo {
	static CPU createCPU(String mode) {
		if (mode.equals("Intel")) {
			return new IntelCPU();
		} else if (mode.equals("AMD")) {
			return new AMDCPU();
		}
		return null;
	}
}

class CPU {}

class IntelCPU extends CPU {
	
}

class AMDCPU extends CPU {
	
}
```

#####  2 工厂方法模式

定义一个创建对象的工程类抽象接口，让其子类决定实例化哪个类，工厂方法使一个类的实例化延迟到其子类。

简单说就是为每一个产品类都新建一个工厂类，这些工厂类都继承一个父类。优点是降低了客户程序与产品对象之间的耦合，缺点是每新增一个产品类，就需要为其再添加一个工厂子类。

```
public class FactoryDemo {
	public static void main(String[] args) {
		IFactory factory = new IntelFactory();
		CPU cpu = factory.createCPU();
		cpu.cpuRun();
	}
}

interface IFactory {
	CPU createCPU();
}

class IntelFactory implements IFactory {
	@Override
	public CPU createCPU() {
		return new IntelCPU();
	}
}

class AMDFactory implements IFactory {
	@Override
	public CPU createCPU() {
		return new AMDCPU();
	}
}

abstract class CPU {
	abstract void cpuRun();
}

class IntelCPU extends CPU {
	@Override
	void cpuRun() {
		System.out.println("intel cpu run");
	}
}

class AMDCPU extends CPU {
	@Override
	void cpuRun() {
		System.out.println("Amd cpu run");
	}
}
```



##### 3 抽象工厂模式

提供一个创建一系列相关或者相互依赖的对象的工厂类的接口，而不需要指定具体的类。

`IFactory`是一个抽象的工厂接口，包含所有产品（一系列产品族）创建的抽象方法，这样便于交换产品系列。

如一台电脑主要包括的CPU和主板，CPU和主板的品牌都可分为intel和AMD，那么实现抽象工厂模式的代码如下：

```
public class FactoryDemo {
	public static void main(String[] args) {
		IFactory factory = new IntelFactory();
		CPU cpu = factory.createCPU();
		Board board = factory.createBoard();
		cpu.cpuRun();
		board.boardRun();
	}
}

interface IFactory {
	CPU createCPU();
	Board createBoard();
}

class IntelFactory implements IFactory {
	@Override
	public CPU createCPU() {
		return new IntelCPU();
	}
	
	@Override
	public Board createBoard() {
		return new IntelBoard();
	}
}

class AMDFactory implements IFactory {
	@Override
	public CPU createCPU() {
		return new AMDCPU();
	}
	@Override
	public Board createBoard() {
		return new AMDBoard();
	}
}

abstract class CPU {
	abstract void cpuRun();
}

class IntelCPU extends CPU {
	@Override
	void cpuRun() {
		System.out.println("intel cpu run");
	}
}

class AMDCPU extends CPU {
	@Override
	void cpuRun() {
		System.out.println("Amd cpu run");
	}
}

abstract class Board {
	abstract void boardRun();
}

class IntelBoard extends Board {
	@Override
	void boardRun() {
		System.out.println("intel board run");
	}
}

class AMDBoard extends Board {
	@Override
	void boardRun() {
		System.out.println("Amd board run");
	}
}
```



#### 5 单例模式

确保一个类只有一个实例，并提供一个全局的访问API。

保证以下几个条件：

1. 静态的全局变量
2. 构造方法是私有
3. 提供一个静态的公共方法，获取单例：getInstance()

1 饿汉式：在类加载的时候就对单例类进行初始化，如果单例类未被使用，就可能造成资源浪费。

```
public class SingletonDemo {

	private static SingletonDemo mSingleton = new SingletonDemo();
	
	private SingletonDemo() {}
	
	public static SingletonDemo getInstance() {
		return mSingleton;
	}
}
```

2 双重检测加锁：singleton变量需要用volatile

加锁前判断，确保只有在第一次创建时才会被加锁，提高效率。

使用volatile修饰，确保代码不被优化重排，导致异常，如果没有volatile，则可能出现优化重排: 

`mSingleton = new SingletonDemo();` 会先对mSingleton 进行引用赋值，然后再执行 new SingletonDemo()的真正初始化动作，如果初始化时间较长，其当前其他线程调用了`getInstance()`，并使用，此时mSingleton并没有被真正的初始化完成，会出现错误。

```
public class SingletonDemo {

	private volatile static SingletonDemo mSingleton;
	
	private SingletonDemo() {}
	
	public static SingletonDemo getInstance() {
		if (mSingleton == null) {
			synchronized (SingletonDemo.class) {
				if (mSingleton == null) {
					mSingleton = new SingletonDemo();
				}
			}
		}
		return mSingleton;
	}
}
```

3 内部静态类持有

利用JVM加载类的机制保证单例类只会被创建一次，且保证同步问题。

确定是，如果创建时候需要向`getInstance()`传入参数，则无法使用。

```
public class SingletonDemo {
	private SingletonDemo() {}
	
	private static class SingletonHolder {
		private static final SingletonDemo mSingleton = new SingletonDemo();
	}
	
	public static SingletonDemo getInstance() {
		return SingletonHolder.mSingleton;
	}
}
```



#### 6 命令模式

命令模式支持请求调用者和请求接收者之间的解耦，其将请求封装成对象，以便使用不同的请求、队列或者日子来参数化其他对象，命令模式也支持撤销请求的操作。

实例：一个带有7个插槽的遥控器，每个插槽都有对应的开启和关闭按钮，可以在每个插槽插入不同的电器进行控制，如何实现？

将动作的请求者和动作的执行者之间解耦，

```
public class CommandDemo {

	public static void main(String[] args) {
		RemoteControl remoteControl = new RemoteControl();
		
		Light light = new Light();
		remoteControl.setCommand(0, new LightOnCommand(light), new LightOffCommand(light));
		remoteControl.onButtonPressed(0);
		remoteControl.offButtonPressed(0);
		remoteControl.offButtonPressed(3);
	}
}


interface Command {
	void execute();
}

class Light {
	public void on() { System.out.println("light on"); }
	public void off() { System.out.println("light off"); }
}

class LightOnCommand implements Command {
	Light light;
	
	public LightOnCommand(Light light) {
		this.light = light;
	}
	@Override
	public void execute() {
		light.on();
	}
}

class LightOffCommand implements Command {
	Light light;
	
	public LightOffCommand(Light light) {
		this.light = light;
	}
	@Override
	public void execute() {
		light.off();
	}
}

//NoCommand是一种空对象的例子，将处理null的责任转移给空对象，空对象本身也算是一种设计模式
class NoCommand implements Command {
	@Override
	public void execute() {
		System.out.println("no command, do noting");
	}
}

class RemoteControl {
	Command[] onCommands;
	Command[] offCommands;
	
	public RemoteControl() {
		onCommands = new Command[7];
		offCommands = new Command[7];
		
		Command noCommand = new NoCommand();
		for (int i = 0; i < 7; i++) {
			onCommands[i] = noCommand;
			offCommands[i] = noCommand;
		}
	}
	
	public void setCommand(int slot, Command onCommand, Command offCommand) {
		onCommands[slot] = onCommand;
		offCommands[slot] = offCommand;
	}
	
	public void onButtonPressed(int slot) {
		onCommands[slot].execute();
	}
	
	public void offButtonPressed(int slot) {
		offCommands[slot].execute();
	}
}
```



#### 7 适配器模式

将一个接口转换成另一个接口，以符合客户的期望。

定义：将一个类的接口，转换成客户期望的另一额接口，适配器让原本不兼容的类可以合作无间。

使用组合

例子：鸟类有飞`fly()`这个行为，鸭子类不能飞，有快走`quickRun()`这个行为，现在假设缺少鸟类对象，要使用一些鸭子来冒充。需要一个适配器

```
public class AdapterDemo {
	public static void main(String[] args) {
		Bird bird = new WildBird();
		bird.fly();
		
		bird = new DuckAdapter(new WildDuck());
		bird.fly();
	}
}

abstract class Bird {
	abstract void fly();
}

class WildBird extends Bird {
	@Override
	void fly() {
		System.out.println("wildbird fly");
	}
}

abstract class Duck {
	abstract void quickRun();
}

class WildDuck extends Duck {
	@Override
	void quickRun() {
		System.out.println("WildDuck quickRun");
	}
}

class DuckAdapter extends Bird {
	Duck mDuck;
	
	public DuckAdapter(Duck duck) {
		mDuck = duck;
	}
	
	@Override
	void fly() {
		mDuck.quickRun();
	}
}
```



#### 8 外观模式

提供一个统一的接口，用来访问子系统中的一群接口。外观定义了一个高层接口，让子系统更容易使用。

如看家庭影院电影的步骤有很多，有开灯、打开DVD，插入影碟，打开屏幕，开始播放等等，所以我们需要提供一个`startMovie()`API，提供给客户使用，将复杂的细节封装起来。

#### 9 模板方法模式

模板方法定义了一个算法的步骤，并允许子类为一个或多个步骤提供实现，如java中的排序算法，主体的算法步骤已经写好，只需要传入一个Comparable对象，定义排序的规则。还有其他的钩子函数和回调接口。

模板方法模式在一个方法中定义一个算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤。

```java
abstract class AbstractClass {
	final void templateMethod() {
		primitiveOperation1();
		primitiveOperation2();
		concreteOperation();
		hook();
	}
	
	abstract void primitiveOperation1();
	abstract void primitiveOperation2();
	
	void concreteOperation() {
		//具体实现
	}
	
	void hook() {
		//这是一个具体的方法，但它什么都不做
		//默认什么都不做，子类可以根据实际情况决定要不要重写它
	}
}

class ConcreteClass extends AbstractClass {
	@Override
	void primitiveOperation1() {
		//具体实现
	}
	
	@Override
	void primitiveOperation2() {
		//具体实现
	}
}
```



#### 10 迭代器与组合模式

迭代器模式：提供一种方法顺序访问一个集合对象中的各个元素，而又不暴露其内部的表示。

把元素之间游走的任务交给迭代器，而不是集合，这样简化了集合的接口和实现，也让责任各得其所。

#### 11 责任链模式

责任链模式是一种对象的行为模式。在责任链模式里，很多对象由每一个对象对其下家的引用而连接起来形成一条链。请求在这个链上传递，直到链上的某一个对象决定处理此请求。发出这个请求的客户端并不知道链上的哪一个对象最终处理这个请求，这使得系统可以在不影响客户端的情况下动态地重新组织和分配责任。

创建多个对象，使这些对象形成一条链，并沿着这条链传递请求，直到链上的某一个对象决定处理此请求。

1）接收请求的对象连接成**一条链**，对象之间存在层级关系。

2）这些对象可处理请求，也可传递请求，直到有对象处理该请求。

定义：一个请求沿着一条“链”传递，直到该“链”上的某个处理者处理它为止。

纯责任链模式和不纯的责任链模式
如果一个类要么承担责任处理请求要么将请求踢给下一个皮球，则被称为纯责任链模式。
如果一个类承担了一部分责任，还将请求踢给下一个皮球，则被称为不纯的责任链模式。

一般来说，日常开发中不纯的责任链模式用的比较多一点。

![1556187069182](C:\Users\geb9wx\AppData\Roaming\Typora\typora-user-images\1556187069182.png)

上图中Handler类的聚合关系给出了具体子类对下家的引用，抽象方法handleRequest()规范了子类处理请求的操作。具体处理者接到请求后，可以选择将请求处理掉，或者将请求传给下家。由于具体处理者持有对下家的引用，因此，如果需要，具体处理者可以访问下家。

举一个简单的例子，部门办活动需要报销。报销处职员可以处理单次`500`元以下的业务，超过500需要和处长联系。而处长只能处理单次`1000`元一下的业务，再高就只能找老大报了。但是老大目前只能处理单次`1500`元以下的业务，再高目前只能拒绝报销了。

```java
public abstract class Handler {
    private Handler nextHandler;

    public Handler getNextHandler() {
        return nextHandler;
    }

    public void setNextHandler(Handler nextHandler) {
        this.nextHandler = nextHandler;
    }

    abstract public String process(String name , double fee);
}



class StaffMember extends Handler {

    @Override
    public String process(String name, double fee) {
        if (fee <= 500) {
            return "StaffMember give " + name + " money:" +fee;
        } else if (getNextHandler() == null) {
            return "nobody can process it";
        } else {
            return  getNextHandler().process(name, fee);
        }
    }
}

class BigMember extends Handler {

    @Override
    public String process(String name, double fee) {
        if (fee <= 1000) {
            return "BigMember give " + name + " money:" +fee;
        } else if (getNextHandler() == null) {
            return "nobody can process it";
        } else  {
            return getNextHandler().process(name, fee);
        }
    }
}

class Boss extends Handler {

    @Override
    public String process(String name, double fee) {
        if (fee <= 1500) {
            return "Boss give " + name + " money:" +fee;
        } else if (getNextHandler() == null) {
            return "nobody can process it";
        } else  {
            return getNextHandler().process(name, fee);
        }
    }
}

public class Demo {

    public static void main(String[] args) {
        StaffMember staffMember = new StaffMember();
        BigMember bigMember = new BigMember();
        Boss boss = new Boss();

        staffMember.setNextHandler(bigMember);
        bigMember.setNextHandler(boss);

        System.out.println( staffMember.process("jack", 400) );
        System.out.println( staffMember.process("lily", 800) );
        System.out.println( staffMember.process("dave", 1222) );
        System.out.println( staffMember.process("king", 4000) );

    }
}
```



还有一种责任链模式的实现方式，如实现一个字符串处理器：我们在处理字符串的时候，需要转换大小写，替换特殊字符等，如果将功能写死的话，后续扩展就比较麻烦，比如要加个功能：在字符串的后面加上特定字符。

实现代码如下：

```java
import java.util.ArrayList;
import java.util.List;

public interface Process {
    String process(String msg);
}

class LowerProcess implements Process {

    @Override
    public String process(String msg) {
        return msg.toLowerCase();
    }
}

class FilterProcess implements Process {

    @Override
    public String process(String msg) {
        return msg.replace("fuck", "fun");
    }
}

class SignProcess implements Process {

    @Override
    public String process(String msg) {
        msg = msg + " ,by lester";
        return msg;
    }
}

class ProcessChain {
    private List<Process> list = new ArrayList<>();

    public ProcessChain addChain(Process process) {
        list.add(process);
        return this;
    }

    public String process(String msg) {
        String str = msg;
        for (Process ps : list) {
            str = ps.process(str); //上一次的输出作为下一次的输入
        }
        return str;
    }


    public static void main(String[] args) {
        ProcessChain chain = new ProcessChain();
        chain.addChain(new LowerProcess())
                .addChain(new FilterProcess())
                .addChain(new SignProcess());

        String msg = chain.process("this is a fuck DAY");
        System.out.println(msg);
    }
}
```

