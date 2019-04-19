### MySql从零开始

##### 1 mysql基本使用

1. 安装MySQL，一般是一个mysql-installer-community-version.msi的安装文件。

   安装过程中配置选择，如安装内容，端口号（3306），用户名（root)和密码(root)，windows服务名字：MySql56

   配置环境变量，将mysql安装包的bin目录加入path

   登录mysql,  在命令行界面输入：mysql  -u root -p，回车，输入密码，然后提示：

   提示“Welcome to the MySQL monitor.” 说明安装成功。

   修改密码：

   ```sql
   mysqladmin -u root -p password 新密码
   回车后输入旧密码即可
   ```

   服务的启动和停止：

   ```cmake
   net start mysql56 (cmd里不区分大小写)
   
   net stop mysql56
   
   sc delete mysql56 卸载
   ```

   win+R 输入 services.msc，可以查看系统服务。

   登录制定主机的mysql:

   ```
   mysql -h 主机名 -u 用户名 -p ；如果没有密码，则不需要 -p
   ```

   或者 `mysql -D 所选择的数据库名 -h 主机名 -u 用户名 -p`

2. 使用mysql

   > show databases;  查看当前有哪些数据库，注意命令要以  ;  结尾

   `desc tabl_name;` 查看表结构

   `show create table 表名字`   查看生产表的语句；



   可以将多条mysql语句写到一个文件，以.sql 结尾，执行这个文件即可。

   文件的执行方式，首先登入mysql控制台：mysql -h 主机名 -u 用户名 -p

   然后： source  sql文件名

   创建数据库：

   create database samp_db character set gbk;

   使用数据库：

   use samp_db ;

   建表：

   ```sql
   create table students
   (
       id int unsigned not null auto_increment primary key,
       name char(8) not null,
       sex char(4) not null,
       age tinyint unsigned not null,
       tel char(13) null default "-"
   );
   ```

   "auto_increment" 需在整数列中使用, 其作用是在插入数据时若该列为 NULL, MySQL将自动产生一个比现存值更大的唯一标识符值。在每张表中仅能有一个这样的值且所在列必须为索引列。

   "primary key" 表示该列是表的主键, 本列的值必须唯一, MySQL将自动索引该列。

插入数据：

```sql
insert [into] 表名 [(列名1, 列名2, 列名3, ...)] values (值1, 值2, 值3, ...);
[]内的内容可以省略
```

查询：

```sql
select 列名称 from 表名称 [查询条件];
select 是最复杂的
```

更新：

```sql
update 表名称 set 列名称=新值 where 更新条件;
```

删除：

```sql
delete from 表名 where 删除条件
```

对数据表的修改如下：

添加列：

```sql
alert table 表名 add 列名 列数据类型 [after 插入位置列名]
```

更改列：

```sql
alert table 表名 change 列名称 列新名称 新数据类型
```

删除列：

```sql
alert table 表名 drop 列名称
```

重命名数据表：

```sql
alert table 表名 rename 新表名
```

删除数据表：

```sql
drop table 表名
```

删除数据库：

```sql
drop database 数据库名
```

退出：exit 或者 quit



##### 2 spring boot之JPA

在springboot工程添加相关依赖：

```xml
	<dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-jdbc</artifactId>
    </dependency>
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <scope>runtime</scope>
    </dependency>
```

添加了依赖之后，启动应用，此时会报错，dataSource的url无法连接，所有下一步需要配置数据源。

在application.properties中配置如下：

```java
spring.datasource.url=jdbc:mysql://localhost:3306/jpa_db
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

#设置执行的SQL是否显示
spring.jpa.show-sql=true

#create：每次加载hibernate时都会删除上一次的生成的表，然后根据你的model类再重新来生成新表
每次应用启动会先drop,然后新建表
#create-drop：每次加载hibernate时根据model类生成表，但是sessionFactory一关闭,表就自动删除。
应用关闭之后，表就被删除了。
#update：最常用的属性，第一次加载hibernate时根据model类会自动建立起表的结构（前提是先建立好数据库），
# 以后加载hibernate时根据model类自动更新表结构，即使表结构改变了但表中的行仍然存在不会删除以前的行。
# 要注意的是当部署到服务器后，表结构是不会被马上建立起来的，是要等应用第一次运行起来后才会。
应用停止后，表还在，下次应用起来，表也不会被删除重建。
# validate：每次加载hibernate时，验证创建数据库表结构，只会和数据库中的表进行比较，不会创建新表，但是会插入新值。
spring.jpa.hibernate.ddl-auto=create

#将默认的存储引擎切换为 InnoDB 用的
spring.jpa.database-platform=org.hibernate.dialect.MySQL5InnoDBDialect
```

此处配置的数据库名字是：jap_db, 要保证配置的数据库是存在的，否则报错。

接下来创建一个model类`User.java`，对应数据的一张table表。

```java
@Entity
@Table(name = "my_user")
@Data
@AllArgsConstructor
//需要有默认的构造函数
public class User {
    
	protected User() {}
    
    @Id
    @GeneratedValue
    private Long id;

    @Column(nullable =  false, length = 32)
    private String name;

    @Column(nullable = false)
    private Integer age;
}
```

1. @Entity是必选的，表明这个POJO类对应了数据库的数据表；
2. @Table是可选的，可以自定义表名，此处自定义为“my_user", 如果没有的话则根据java类名自动生成，如”user“。
3. @Id 注解声明了实体唯一标识对应的属性。
4. @Column(length = 32) 用来声明实体属性的表**字段的定义**。默认的实体每个属性都对应了表的一个字段。字段的名称默认和属性名称保持一致（并不一定相等）。字段的**类型根据实体属性类型自动推断**。这里主要是声明了字符字段的长度。如果不这么声明，则系统会采用 255 作为该字段的长度。
5. 主键扩展：<https://blog.csdn.net/tracycater/article/details/78319021>

还有要有构造函数和get、set方法。

> 注意：一定要有一个默认的构造方法，否则在数据库find查询返回结果时候会报错
>
> The default constructor only exists for the sake of JPA. You won’t use it directly, so it is designated as `protected`

此时，运行应用，会看到在jap_db数据库创建了一个新的数据表。

然后新建一个数据库的DAO操作类`UserRepo.java`：

```java
public interface UserRepo extends JpaRepository<User, Long> {

    User findByName(String name);

    User findByAgeAndName(int age, String name);

    //JPQL查询
    @Query(value = "from User u where u.name=:name")
    User findUser(@Param("name") String name);

    //SQL查询
    @Query(nativeQuery = true, value = "select * FROM USER where age < :age")
    List<User> findUserSmallAge(@Param("age") int age);
}
```

JpaRepository<User, Long>中User是数据库表对应的java类， Long 是指主键id的类型。

`JpaRepository`该接口本身已经实现了创建（save）、更新（save）、删除（delete）、查询（findAll、findOne）等基本操作的函数，因此对于这些基础操作的数据访问就不需要开发者再自己定义。

另外该接口也实现了通过解析方法名来创建查询，如findByName、findByAgeAndName；其中Name和Age是java类中的成员变量，还可以有and or之类的条件组合。

还有第三种查询方法，提供通过使用@Query 注解来创建查询，您只需要编写JPQL语句，并通过类似“`:name`”来映射@Param指定的参数，就像例子中的findUser函数一样。

在 @Query 注解中增加一个 nativeQuery = true 的属性，就可以采用原生 SQL 语句的方式来编写查询。

如涉及到删除和修改在需要加上 @Modifying，也可以根据需要添加 @Transactional 对事物的支持，查询超时的设置等。如 `@Transactional(timeout = 10)`

最后，用测试类来测试该DAO操作：

```java

@RunWith(SpringRunner.class)
@SpringBootTest
public class JpaDemoApplicationTests {
    @Autowired
    private UserRepo userRepo;

    @Test
    public void test_jpa() {
        // 插入 10 条数据
        for (int i = 0; i < 10; i++) {
            String name = "name_" + i;
            int age = 10 + i;
            userRepo.save(new User(null, name, age));
        }

        System.out.println(userRepo.findAll());
        Assert.assertEquals(userRepo.findAll().size(), 10);

        System.out.println(userRepo.findByName("name_3"));
        Assert.assertEquals(userRepo.findByName("name_3").getAge().intValue(), 13);

        System.out.println(userRepo.findById(5L));
        Assert.assertEquals(userRepo.findById(5L).get().getName(), "name_4");

        System.out.println(userRepo.findByAgeAndName(15, "name_5"));
        System.out.println(userRepo.findByAgeAndName(16, "name_5"));

        assertNotNull(userRepo.findByAgeAndName(15, "name_5"));
        assertNull(userRepo.findByAgeAndName(16, "name_5"));

        Assert.assertEquals(userRepo.findUser("name_6").getAge().intValue(), 16);

        System.out.println(userRepo.findUserSmallAge(15));
        Assert.assertEquals(userRepo.findUserSmallAge(15).size(), 5);
    }
}
```

build jar包： 

```
./gradlew build   ./mvnw clean package   windows下不加 ./
java -jar jar包名字 执行jar包
```

EntityManager详解 ：<https://www.jianshu.com/p/091360c47e6b>

EntityManager是JPA中用于增删改查的接口，它的作用相当于一座桥梁，连接内存中的java对象和数据库的数据存储。其主要的方法定义如下：

```java
public interface EntityManager {
    void persist(Object var1);

    <T> T merge(T var1);

    void remove(Object var1);

    <T> T find(Class<T> var1, Object var2);
    .................
    .................
}
```

既然EntityManager只是一个**接口**，那么谁来负责实现它呢？就是实现了JPA的厂商，例如EclipseLink，Hibernate等等。那么如何获得EntityManager对象呢？这取决于你的EntityManger对象的托管方式，主要有以下两种方式：

- 容器托管的EntityManager对象
- 应用托管的EntityManager对象

受到容器托管的EntityManager可以直接通过注解@PersistenceContext注入的方式来获得：

```java
@PersistenceContext
private EntityManager em;
```

应用托管的EntityManager对象，程序员需要手动地控制它的释放和连接、手动地控制事务等。

通过EntityManagerFactory的createEntityManager()来获得，那么EntityManagerFactory又是通过何种方法得到的呢？这得分两种环境来讨论

```java
Java EE
@PersistenceUnit(unitName="jpa-1")
private EntityManagerFactory emf;

java SE
EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpa-1");
```

其中“jpa-1"是配置的持久化单元名字，持久化单元是一个用于控制如何生产的配置场所，一般是在MRTA-INF文件夹中创建persistence.xml文件中定义：

```xml
<persistence version="2.0" xmlns="http://java.sun.com/xml/ns/persistence"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
   xsi:schemaLocation="http://java.sun.com/xml/ns/persistence 
   http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
   
   <persistence-unit name="jpa-1" transaction-type="RESOURCE_LOCAL">
   
   	<!-- 配置使用说明ORM产品 -->
   	  <!-- 1.实现ORM策略是继承javax.persistence.spi.PersistenceProvider接口 -->
   	  <!-- 2.如果项目中只有一个JPA实现产品，那么不指定也是可以的 -->
   	  <provider>org.hibernate.ejb.HibernatePersistence</provider>
   	  
   	  <!-- 添加持久化类 -->
      <class>com.tutorialspoint.eclipselink.entity.Employee</class>

      <properties>
         <property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/jpadb"/>
         <property name="javax.persistence.jdbc.user" value="root"/>
         <property name="javax.persistence.jdbc.password" value="root"/>
         <property name="javax.persistence.jdbc.driver" value="com.mysql.jdbc.Driver"/>
         
         <!-- 配置jpa实现产品 -->
         <property name="hibernate.show_sql" value="true"/>
         <property name="hibernate.hbm2ddl.auto" value="update"/>
         <property name="hibernate.format_sql" value="true"/>
      </properties>
      
   </persistence-unit>
</persistence>
```

参考：

<https://segmentfault.com/a/1190000015047290>

<http://blog.didispace.com/springbootdata2/>

<https://spring.io/guides/gs/accessing-data-jpa/>



##### 3 java JDBC

JDBC是连接java应用程序和数据库之间的桥梁。

JDBC (Java Database Connectivity) API，即Java数据库编程接口，是**一组标准的Java语言中的接口和类**，使用这些接口和类，Java客户端程序可以**访问各种不同类型的数据库**。比如建立数据库连接、执行SQL语句进行数据的存取操作。

![1555468117716](.\assets\1555468117716.png)



JDBC代表Java数据库连接。

JDBC库中所包含的API任务通常与数据库使用：

- 连接到数据库
- 创建SQL或MySQL语句
- 在数据库中执行SQL或MySQL查询
- 查看和修改记录

JDBC基本步骤：

```java
		//1.加载驱动程序
        Class.forName("com.mysql.jdbc.Driver");
        //2.获得数据库的连接
        Connection conn = DriverManager.getConnection(URL, NAME, PASSWORD);
        //3.通过数据库的连接操作数据库，实现增删改查
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("select user_name,age from imooc_goddess");
        //选择import java.sql.ResultSet;
        while(rs.next()){//如果对象中有数据，就会循环打印出来
            System.out.println(rs.getString("user_name")+","+rs.getInt("age"));
        }
```

示例代码：

```java

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import lombok.AllArgsConstructor;
import lombok.Data;

public class JDBCDemo {

    public static void main(String[] args) {
        System.out.println("hi");

        JDBCDemo dbDemo = new JDBCDemo();
//        dbDemo.simpleTestDB();

        dbDemo.createTable();
        dbDemo.inserStudent();
        dbDemo.seletAll();
        dbDemo.selectScoreBigThen(80);

        dbDemo.updateName("lester");
        dbDemo.seletAll();

//        dbDemo.deleteName("lester");
        dbDemo.deleteName2("lester");
        dbDemo.seletAll();
    }


    private static final String URL = "jdbc:mysql://localhost:3306/zhtdb";
    private static final String NAME = "root";
    private static final String PASSWORD = "root";

    void simpleTestDB() {
        try {
            //1 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("load class...");

            //2 获取数据库连接
            Connection connection = DriverManager.getConnection(URL, NAME, PASSWORD);
            System.out.println("connect to database...");

            //3 开始操作数据库
            Statement statement = connection.createStatement();

            String query = "select prod_name,prod_price from products";
            ResultSet resultSet = statement.executeQuery(query);

            while (resultSet.next()) {
                System.out.println("prod_name:" + resultSet.getString("prod_name")
                        + ", prod_price:" + resultSet.getDouble("prod_price"));
            }

            resultSet.close();
            statement.close();
            connection.close();
            System.out.println("close db");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    private Connection getConnection() {
        try {
            //1 加载驱动类
            Class.forName("com.mysql.cj.jdbc.Driver");
            //2 获取数据库连接
            Connection connection = DriverManager.getConnection(URL, NAME, PASSWORD);
            return connection;
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    void createTable() {
        String dropSql = "drop table if exists student;";
        String createSql = ""
                + "CREATE TABLE Student"
                + "("
                + "  id  int  NOT NULL auto_increment primary key,"
                + "  update_date datetime default current_timestamp() ,"
                + "  name  char(10) NOT NULL ,"
                + "  age int default 18,"
                + "  score double"
                + ")";
        String showTableSql = "show tables";

        try {
            Connection connection = getConnection();

            Statement statement = connection.createStatement();
            statement.execute(dropSql);
            statement.execute(createSql);

            ResultSet resultSet = statement.executeQuery(showTableSql);
            while (resultSet.next()) {
                // mysql 查询结果集中的列下标，以 1 开始计数
                String tableName = resultSet.getString(1);
                if (tableName.equalsIgnoreCase("student")) {
                    System.out.println("create table:student success");
                    break;
                }
            }

            resultSet.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void inserStudent() {
        try {
            Connection connection = getConnection();

            //方法1
            String insertSql = "insert into student (name,age,score) values('a',17,19)";
            Statement statement = connection.createStatement();
            statement.execute(insertSql);

            //方法2
            String insertSql2 = "insert into student (name,age,score) values(?,?,?)"; //使用 ？ 作为占位符
            PreparedStatement preparedStatement = connection.prepareStatement(insertSql2);

            for (int i = 1; i <= 4; i++) {
                preparedStatement.setString(1, "zht" + i); // 待设置参数下标也是从 1 开始
                preparedStatement.setInt(2, 20 + i * 5);
                preparedStatement.setDouble(3, 60 + i * 10);
                preparedStatement.execute();

                Thread.sleep(1000);
            }

            statement.close();
            connection.close();
            System.out.println("insert ok");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void updateName(String newName) {
        try {
            Connection connection = getConnection();
            String updateSql = "update student set name = ? where score = ?";

            PreparedStatement preparedStatement = connection.prepareStatement(updateSql);
            preparedStatement.setString(1, newName);
            preparedStatement.setDouble(2, 100);
            preparedStatement.execute();

            preparedStatement.close();
            connection.close();
            System.out.println("update ok");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void deleteName(String name) {
        try {
            Connection connection = getConnection();
            String deleteSql = "delete from student where name = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(deleteSql);
            preparedStatement.setString(1, "lester");
            preparedStatement.execute();

            preparedStatement.close();
            connection.close();
            System.out.println("delete ok");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    //添加事务处理代码
    private void deleteName2(String name) {
        Connection connection = getConnection();
        try {

            connection.setAutoCommit(false);// 自动提交设置为false

            String deleteSql = "delete from student where name = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(deleteSql);
            preparedStatement.setString(1, "lester");
            preparedStatement.execute();

            connection.commit();//提交
            connection.setAutoCommit(true);

            preparedStatement.close();
            connection.close();
            System.out.println("delete ok");
        } catch (SQLException e) {
            e.printStackTrace();
            //如果异常则进行回滚
            try {
                connection.rollback();
            } catch (SQLException e1) {
                e1.printStackTrace();
            }
        }
    }

    private void seletAll() {
        try {
            Connection connection = getConnection();
            String selectSql = "select * from student";
            Statement statement = connection.createStatement();
            ResultSet set = statement.executeQuery(selectSql);

            System.out.println("select all:");
            while (set.next()) {
                StuBean bean = convertSetToStuBean(set);
                System.out.println(bean);
            }

            set.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void selectScoreBigThen(double bigThen) {
        try {
            Connection connection = getConnection();
            String selectSql = "select * from student where score > ?";

            PreparedStatement statement = connection.prepareStatement(selectSql);
            statement.setDouble(1, bigThen);

            ResultSet set = statement.executeQuery();

            System.out.println("select Score Big Then:");
            while (set.next()) {
                StuBean bean = convertSetToStuBean(set);
                System.out.println(bean);
            }

            set.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    private StuBean convertSetToStuBean(ResultSet set) {
        StuBean stuBean = null;
        try {
            if (set != null) {
                stuBean = new StuBean(set.getInt(1), set.getString(2),
                        set.getString(3), set.getInt(4),
                        set.getDouble(5));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return stuBean;
    }

    @AllArgsConstructor
    @Data
    public static class StuBean {

        int id;
        String update_date;
        String name;
        int age;
        double score;
    }
}
```

参考：

<https://www.cnblogs.com/Qian123/p/5339164.html>

##### 4 java JDBCTemplet

JDBC--->Java Data Base Connectivity,java数据库连接,简单点说就是可以**为多种关系数据库提供统一访问,由一组用java语言编写的类和接口组成。**

模板就是事先准备好的东西,你只需要去套用就可以,JDBCTemplate就是这样的模板,通过设置JDBCTemplate可以**减少对数据库的繁琐操作**,例如连接数据库,获得链接关闭,获得statement,resultset,preparedstatement这些等等。

传统的JDBC应用步骤:

- ​	1.指定数据库连接参数
- ​	2.打开数据库连接
- ​	3.声明SQL语句
- ​	4.预编译并执行SQL语句
- ​	5.遍历查询结果（如果需要的话）
- ​	6.处理每一次遍历操作
- ​	7.处理抛出的任何异常
- ​	8.处理事务
- ​	9.关闭数据库连接

JDBC的缺点就是太麻烦了,不易编码,容易出错,不利于开发者把精力投入到业务上去。简化JDBC就是新技术的目标。象Spring,hibernate等都通过对JDBC进行封装,以达到简化开发的目的。但是这些技术在自身侧重上略有不同。如Hibernate主要进行Object/Relational Mapping。

Spring的JDBC: 节省代码,不管连接(Connection),不管事务,不管异常,不管关闭(con.close() ps.close )

```java
import com.example.learndemo.database.jdbc.JDBCDemo.StuBean;
import java.util.List;
import java.util.Map;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.support.rowset.SqlRowSet;
import org.springframework.stereotype.Repository;

/**
 * 使用在 appplications.properties 的配置 配置数据源和数据库 类似于JPA
 或者通过代码配置：new JdbcTemplate(dataSource);
 */
@Repository
public class JDBCTempletDemo {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    // 其实JdbcTemplate就是将重复的connection/statement/ 等开启和关闭等重复操作进行了封装。

    public void insert() {
        String dropSql = "drop table if exists student;";
        String createSql = ""
                + "CREATE TABLE Student"
                + "("
                + "  id  int  NOT NULL auto_increment primary key,"
                + "  update_date datetime default current_timestamp() ,"
                + "  name  char(10) NOT NULL ,"
                + "  age int default 18,"
                + "  score double"
                + ")";

        jdbcTemplate.execute(dropSql);
        jdbcTemplate.execute(createSql);

        String insertSql = "insert into student (name,age,score) values(?,?,?)";

        for (int i = 0; i < 5; i++) {
            jdbcTemplate.update(insertSql, "hi" + i, 10 + i, 60 + i * 5);
        }
        //mysql 的insert/update/delete 都可以使用jdbcTemplate.update()
    }

    public void showAll() {
        String sql = "select * from student";
        List<Map<String, Object>> list = jdbcTemplate.queryForList(sql);
        System.out.println("list:" + list);

        SqlRowSet rowSet = jdbcTemplate.queryForRowSet(sql);

        while (rowSet.next()) {
            System.out.println(convertSetToStuBean(rowSet));
        }
    }

    public int add(String name, int age, double score) {
        String sql = "insert into student (name, age,score) values (?,?,?)";
        int res = jdbcTemplate.update(sql, name, age, score);
        return res;
    }

    private StuBean convertSetToStuBean(SqlRowSet set) {
        StuBean stuBean = null;
        try {
            if (set != null) {
                stuBean = new StuBean(set.getInt(1), set.getString(2),
                        set.getString(3), set.getInt(4),
                        set.getDouble(5));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return stuBean;
    }
}
```

数据源配置：<http://blog.didispace.com/springbootmultidatasource/>



##### 5 Hibernate

Hibernate是一种ORM框架，全称为 Object_Relative DateBase-Mapping，在**Java对象**与关系数据库的**数据表**之间建立某种**映射**，以实现直接存取Java对象。将在代码中对java对象的操作映射到对数据库的修改。

使用Hibernate要先引入依赖，数据库驱动，JDBC和hibernate就jar包，如果项目引入了springboot的jpa，那么也包含了这些依赖。因为jpa本身就是在hibernate之上又做了一次封装。

hibernate对数据库增删改查操作是通过Session类，Session类是由SessionFactory创建的，所有第一步就是要拿到SessionFactory。在创建SessionFactory的同时也加载对数据库的相关配置，类似于springboot的jpa。

代码如下：

```java
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
    private static final String DBURL = "jdbc:mysql://localhost:3306/";
    private static final String DBNAME = "testdb";
    private static final String DBUSERNAME = "root";
    private static final String DBPWD = "root";
    private static SessionFactory sessionFactory;

    public static SessionFactory getSessionFactory() {
        if (sessionFactory != null)
            return sessionFactory;

        Configuration configuration = new Configuration();
        configuration.setProperty("hibernate.connection.url", "jdbc:mysql://localhost:3306/testdb");
        configuration.setProperty("hibernate.connection.username", DBUSERNAME);
        configuration.setProperty("hibernate.connection.password", DBPWD);

        //不给参数就默认加载hibernate.cfg.xml文件
        configuration.configure("hibernate.cfg.xml");

//        ServiceRegistry serviceRegistry = new StandardServiceRegistryBuilder()
//                .configure("hibernate.cfg.xml")
//                .applySettings(configuration.getProperties()).build();
//        sessionFactory = configuration.buildSessionFactory(serviceRegistry);

        sessionFactory = configuration.buildSessionFactory();
        return sessionFactory;
    }
}
```

Configuration是一个管理配置类，通过这个类可加载hibernate的配置文件，设置数据库的一些属性值，configure()方法用于加载配置文件，如果指定参数则加载参数路径指定的配置文件，否则默认加载src/目录下的hibernate.cfg.xml文件。

buildSessionFactory()用于创建SessionFactory。

SessionFactory可以说是代表了hibernate.cfg.xml这个配置文件，因为这个配置文件就有一个节点叫做session-factory：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://hibernate.sourceforge.net/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <!-- 1. 数据库连接配置，也可以在代码中配置 -->
        <!--<property name="hibernate.connection.url">jdbc:mysql:///zhongfucheng</property>-->
        <!--<property name="hibernate.connection.username">root</property>-->
        <!--<property name="hibernate.connection.password">root</property>-->

        <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>

        <!--数据库方法配置， hibernate在运行的时候，会根据不同的方言生成符合当前数据库语法的sql-->
        <property name="hibernate.dialect">org.hibernate.dialect.MySQL57Dialect</property>
        <property name="show_sql">true</property>
        <property name="format_sql">true</property>
        
        <!-- 这里会自动创建数据表 -->
        <property name="hbm2ddl.auto">create</property>

        <!-- 映射数据表的 POJO类 -->
        <mapping class="com.example.sqldemo.model.User"></mapping>

    </session-factory>
</hibernate-configuration>
```

在配置文件里设置了和数据表映射的java类User, 配置这样映射关系可以通过xml文件或者代码注解，建议通过代码注解方式来配置。

```java
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
@Entity
@Table(name = "user")
public class User {
    protected User() {}

    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(name = "name", length = 32)
    private String name;

    @Column(name = "pwd", length = 32)
    private String passWord;

    @Column(name = "age")
    private int age;
}
```

Session的使用通过通过SessionFactory的openSession() 或者 getCurrentSession()方法。

Session维护了一个连接（Connection), 只要通过hibernate操作数据库，都必须通过Session。

Session也提供了一些对数据库的操作方法，如 save, update, query等，非springboot下使用hibernate的代码如下：

```java
import com.example.sqldemo.model.User;
import com.example.sqldemo.util.HibernateUtil;
import java.util.List;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;

public class Demo {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("start");
        SessionFactory sessionFactory = HibernateUtil.getSessionFactory();

        try (Session session = sessionFactory.openSession()){
            session.beginTransaction();
			
            for (int i = 1; i <=10; i++) {
                String name = "name_" + i;
                String pwd = "pwd_" + i;
                int age = 10 + i;
				//插入数据
                session.save(new User(null, name, pwd, age));
            }
            session.getTransaction().commit();//提交以后才能查询得到

            session.beginTransaction();
            //根据 ID 查询数据
            User user = session.get(User.class, 1L);
            System.out.println(user);

            //HQL 查询，hibernate query language 即hibernate提供的面向对象的查询语言
            Query<User> query1 = session.createQuery("FROM User", User.class);
            List<User> list = query1.list();
            System.out.println(list);

            Query<User> query2 = session.createQuery("FROM User where age > :age", User.class);
            query2.setParameter("age", 15);
            List<User> list2 = query2.list();
            System.err.println(list2.size() + "," + list2);

            //根据原生SQL语句创建查询，存在平台的不兼容问题
            String query = "select u.* from User u where age <:age";
            Query<User> query3 = session.createNativeQuery(query, User.class);
            query3.setParameter("age", 12);
            List<User> list3 = query3.list();
            System.err.println(list3);

            session.getTransaction().commit();
        }
    }
}
```

参考：<https://segmentfault.com/a/1190000013568216>



##### 6 FlyWay

Flyway是一个简单开源**数据库版本控制器**（约定大于配置），主要提供migrate、clean、info、validate、baseline、repair等命令。它支持SQL（PL/SQL、T-SQL）方式和Java方式，支持命令行客户端等，还提供一系列的插件支持（Maven、Gradle、SBT、ANT等）。它的原理非常简单，就是在数据库中创建一张自己用的表，例如schema_version，在里面存放数据库当前的状态，以此来管理数据库的版本。

1、使用它之前先要了解一些概念：

版本：对数据库的每一次变更可称为一个版本。

迁移：Flyway把数据库结构从一个版本更新到另一个版本叫做迁移。

可用的迁移：Flyway的文件系统识别出来的迁移版本。

已经应用的迁移：Flyway已经对数据库执行过的迁移。

2、flyway最基本的几个命令。

Migrate：应用所有的迁移到最新版本，它会在你的DB中新建个表schema_version来存放每次升级的版本信息。

Clean：clean all objects

Info：打印所有的迁移的信息以及状态。

Validate：迁移之前进行验证。

Baseline：初始化schema_version表，并插入一条原始verion=1。

Repair：它主要做了两件事，移除所有失败的迁移（升级），重置校验和。

3、 SQL脚本的命名规则，如 V1__init_table.sql

默认路径：

resource文件夹下：db.migration

prefix: default:V (大写) 

version: 版本号也可以使用大小版本组合的方式，小版本号用单 _区分  

separator: 分隔符，**双下划线** __  

description: 描述（必须要有意义）

flyway的这些参数是可以在spring中进行配置的。



新建一个测试Demo：

新建一个springboot工程，要先包含数据库相关的依赖包，添加flyway依赖：

```xml
<dependency>
      <groupId>org.flywaydb</groupId>
      <artifactId>flyway-core</artifactId>
</dependency>
```

在application.properties配置数据库连接

```xml
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/testdb
spring.datasource.username=root
spring.datasource.password=root
```

在resources的文件夹下，新建一个目录 db/migration。

添加一个文件V1__Base_version.sql

```sql
drop table if exists Person;
create table Person
(
	id int unsigned  auto_increment primary key, #主键
	FirstName  varchar(10) not null,
	Address varchar(50),
	City varchar(30),
	Age int unsigned
);
```

启动springboot工程，在这之前要保证testdb下是空的，执行成功后会在testdb下新创建2个表。

![1555669929295](D:\note\LearnNote\sql\assets\1555669929295.png)

同时控制台也打印出 migration 成功。

![1555670020692](D:\note\LearnNote\sql\assets\1555670020692.png)

再次新建一个文件：V2__insert_data.sql

```sql
insert into Person (FirstName, Address) values ("lester","PiDu");
insert into Person values (null, 'zht','jiaoda','chengdu', 22); 
```

运行工程，成功后控制台提示：

```
Database: jdbc:mysql://localhost:3306/testdb (MySQL 5.6)
Successfully validated 2 migrations (execution time 00:00.019s)
Current version of schema `testdb`: 1
Migrating schema `testdb` to version 2 - insert data
Successfully applied 1 migration to schema `testdb`
```

同时检索数据库的数据也发现，数据确实已经被插入了。

![1555670382630](D:\note\LearnNote\sql\assets\1555670382630.png)

