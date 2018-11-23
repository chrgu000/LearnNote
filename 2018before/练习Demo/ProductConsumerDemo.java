import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProductConsumerDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Resource resource1 = new Resource1();
		Resource resource2 = new Resource2();
		Resource resource3 = new Resource3();
		
		Product product = new Product(resource3, 20);
		Consumer consumer = new Consumer(resource3, 30);
		
		new Thread(product).start();
		new Thread(product).start();
		new Thread(product).start();
		new Thread(consumer).start();
		new Thread(consumer).start();
	}

}

interface Resource {
	void put(String name);
	void get();
}

/**
 * 资源类型：使用synchronized方法，每次生产一个，消费一个。
 * @author Administrator
 *
 */
class Resource1 implements Resource {
	private String name;
	private int count = 1;
	private boolean emptyFlag = true;
	
	public synchronized void put(String n) {
		
		while (emptyFlag == false) { //不为空就等待
			try {
				wait();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		name = n+count;
		count++;
		System.out.println(Thread.currentThread().getName()+"--put---" + name);
		
		emptyFlag = false;
		notifyAll(); //已经放入，通知消费
	}
	
	public synchronized void get() {
		while (emptyFlag == true) {
			try {
				wait();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		System.out.println(Thread.currentThread().getName()+"--get---" + name);
		
		emptyFlag = true;
		notifyAll();
	}
}

/**
 * 资源类型：使用ReentrantLock方法，每次生产一个，消费一个。
 * @author Administrator
 *
 */
class Resource2 implements Resource{
	private String name;
	private int count = 1;
	private boolean emptyFlag = true;
	
	private Lock lock = new ReentrantLock();
	private Condition consumerCdt = lock.newCondition();
	private Condition productCdt = lock.newCondition();
	
	
	@Override
	public void put(String n) {
		
		lock.lock();
		
		try {
			while (emptyFlag == false) { //不为空就等待
				try {
					productCdt.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			name = n+count;
			count++;
			System.out.println(Thread.currentThread().getName()+"--put---" + name);
			
			emptyFlag = false;

			consumerCdt.signalAll(); //通知消费者可以消费了
		} finally {
			lock.unlock();
		}
		
		
	}
	
	@Override
	public void get() {
		lock.lock();
		
		try {
			while (emptyFlag == true) {
				try {
					consumerCdt.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			System.out.println(Thread.currentThread().getName()+"--get---" + name);
			
			emptyFlag = true;
			productCdt.signalAll();
		} finally {
			// TODO: handle exception
			lock.unlock();
		}
		
		
	}
}

/**
 * 资源类型：使用ReentrantLock方法，可容纳多个资源。
 * @author Administrator
 *
 */
class Resource3 implements Resource{
	private String name;
	private boolean emptyFlag = true;
	
	private Lock lock = new ReentrantLock();
	private Condition consumerCdt = lock.newCondition();
	private Condition productCdt = lock.newCondition();
	
	String[] table = new String[20];
	int tableId, putId, getId;
	@Override
	public void put(String n) {
		
		lock.lock();
		
		try {
			while (tableId >= table.length - 1) { //满了就等待
				try {
					productCdt.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			tableId++;//第0个下标不放东西
			table[tableId] = new String(n);
			System.out.println(Thread.currentThread().getName()+"--put---" + table[tableId] + " tableId:" +tableId);
			

			emptyFlag = false;

			consumerCdt.signalAll(); //通知消费者可以消费了
		} finally {
			lock.unlock();
		}
		
		
	}
	
	@Override
	public void get() {
		lock.lock();
		
		try {
			while (tableId == 0) {//第0个不取
				try {
					consumerCdt.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			System.out.println(Thread.currentThread().getName()+"--get---" + table[tableId] + " tableId:" +tableId);
			tableId--;


			productCdt.signalAll();
		} finally {
			// TODO: handle exception
			lock.unlock();
		}
		
		
	}
}

/**
 * 生产者，传入资源和操作次数
 * @author Administrator
 *
 */
class Product implements Runnable {
	Resource mResource;
	int times ;
	public Product(Resource resource, int times) {
		// TODO Auto-generated constructor stub
		mResource = resource;
		this.times = times;
	}
	public void run() {
		for (int i=0; i<10; i++) {
			mResource.put("bread"+i);
			try {
				Thread.sleep(3);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}

/**
 * 消费者，传入资源和操作次数
 * @author Administrator
 *
 */
class Consumer implements Runnable {
	Resource mResource;
	int times;
	public Consumer(Resource resource, int times) {
		// TODO Auto-generated constructor stub
		mResource = resource;
		this.times = times;
	}
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for (int i=0; i<times; i++) {
			mResource.get();
			try {
				Thread.sleep(3);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
}