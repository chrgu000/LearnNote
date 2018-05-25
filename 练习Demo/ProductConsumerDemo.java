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
 * ��Դ���ͣ�ʹ��synchronized������ÿ������һ��������һ����
 * @author Administrator
 *
 */
class Resource1 implements Resource {
	private String name;
	private int count = 1;
	private boolean emptyFlag = true;
	
	public synchronized void put(String n) {
		
		while (emptyFlag == false) { //��Ϊ�վ͵ȴ�
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
		notifyAll(); //�Ѿ����룬֪ͨ����
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
 * ��Դ���ͣ�ʹ��ReentrantLock������ÿ������һ��������һ����
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
			while (emptyFlag == false) { //��Ϊ�վ͵ȴ�
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

			consumerCdt.signalAll(); //֪ͨ�����߿���������
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
 * ��Դ���ͣ�ʹ��ReentrantLock�����������ɶ����Դ��
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
			while (tableId >= table.length - 1) { //���˾͵ȴ�
				try {
					productCdt.await();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			tableId++;//��0���±겻�Ŷ���
			table[tableId] = new String(n);
			System.out.println(Thread.currentThread().getName()+"--put---" + table[tableId] + " tableId:" +tableId);
			

			emptyFlag = false;

			consumerCdt.signalAll(); //֪ͨ�����߿���������
		} finally {
			lock.unlock();
		}
		
		
	}
	
	@Override
	public void get() {
		lock.lock();
		
		try {
			while (tableId == 0) {//��0����ȡ
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
 * �����ߣ�������Դ�Ͳ�������
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
 * �����ߣ�������Դ�Ͳ�������
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