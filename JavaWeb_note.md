



#### 1.tomcat 安装（JDK）

https://blog.csdn.net/qq_32519693/article/details/71330930

访问静态页面 如:hi.html，需要在url后面加入 */hi.html，需要加入html后缀。

#### 2.Java Web基础教程（一）环境搭建

https://www.jianshu.com/p/a8b34d6368f1

get带参数请求格式：

`http://localhost:8080/HelloServlet?name=zht&age=20`

doGet方法：

```
// http://localhost:8080/HelloServlet?name=zht&age=20

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String name = request.getParameter("name");
        String age = request.getParameter("age");

        PrintWriter out = response.getWriter();

        //返回到请求者的页面
        out.println("hi,boy, it is first, name:" + name + ",age:" + age);

        //服务器控制台输出
        System.out.println("do get, name:" + name + ", age:" + age);
    }
```



[4 JavaWeb开发入门](https://www.cnblogs.com/xdp-gacl/p/3729033.html)

相关系列文章不错： https://www.cnblogs.com/xdp-gacl/p/3734395.html



#### 3 部署servlet到tomcat

https://juejin.im/entry/5b1a2b265188257d45297bda



servlet生命周期：

http://www.runoob.com/servlet/servlet-life-cycle.html

https://www.jianshu.com/p/1d5089a635af

https://blog.csdn.net/danielzhou888/article/details/70835418





#### 4 mysql 

安装 https://blog.csdn.net/zhouzezhou/article/details/52446608

https://www.cnblogs.com/mr-wid/archive/2013/05/09/3068229.html 21分钟 MySQL 入门教程



#### 5 Docker and K8S

阮一峰 http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html

使用 Docker 搭建 Java Web 运行环境 https://my.oschina.net/huangyong/blog/372491

Docker  从最简单的入手学习 Docker

https://mp.weixin.qq.com/s?__biz=MzIzNzEyNTc5Mg==&mid=100000030&idx=1&sn=3627f11ce45d62a35086c717dd43893e&chksm=68cc28d15fbba1c79340a159165eb8ca228d0b37561da33bfc9d505febc27b500d9853e55444#rd

Docker的八种用途  https://segmentfault.com/a/1190000005826167



#### 6 微服务

http://dockone.io/article/3687

https://www.roncoo.com/article/detail/130121

REST API概念：https://www.cnblogs.com/imyalost/p/7923230.html

API gateway :https://www.cnblogs.com/savorboard/p/api-gateway.html

路由（routing）是指分组从源到目的地时，**决定端到端路径的网络范围的进程** 。

在web开发中，“route”是指根据url分配到对应的处理程序。



**CI/CD**概念:https://blog.csdn.net/sinat_35930259/article/details/79429743

https://linux.cn/article-9926-1.html

持续集成，持续部署。

在CI环境中，开发人员将会频繁地向主干提交代码。这些新提交的代码在最终合并到主干前，需要经过编译和自动化测试流进行验证。

在CD环境中，通过自动化的构建、测试和部署循环来快速交付高质量的产品。某种程度上代表了一个开发团队工程化的程度，任何修改通过了所有已有的工作流就会直接和客户见面，只有当一个修改在工作流中构建失败才能阻止它部署到产品线。基本上，当开发人员在主分支中合并一个提交时，这个分支将被构建、测试，如果一切顺利，则部署到生产环境中。



**OSS**：Object Storage Service

阿里云对象存储服务  https://zhuanlan.zhihu.com/p/35788674

是一种面向**海量数据**规模的**分布式存储服务**，具有稳定、可靠、安全、低成本的特点，能够提供十一个九的数据可靠性。OSS提供与平台无关的**RESTful API接口**，您可以在互联网任何位置存储和访问。OSS的容量和处理能力**弹性扩展**，并提供多种存储类型供您选择，全面**优化**存储**成本**。

OSS是给你存文件的，相当于网盘，CDN是给你分发内容的，相当于缓存。



**SLF4J**: （Simple logging facade for Java）

SLF4J不同于其他日志类库，与其它有很大的不同。SLF4J(Simple logging Facade for Java)不是一个真正的日志实现，而是一个抽象层（ [abstraction layer](http://javarevisited.blogspot.com/2010/10/abstraction-in-java.html)），它允许你在后台使用任意一个日志类库。现在SLF4J正迅速成为Java世界的日志标准，slf4j-simple、logback都是slf4j的具体实现，log4j并不直接实现slf4j，但是有专门的一层桥接slf4j-log4j12来实现slf4j。

https://www.cnblogs.com/xrq730/p/8619156.html



**ECS**:*Elastic Compute Service*, 简称*ECS*) 是一种处理能力可弹性伸缩的计算服务器, Amazon *ECS* 是一个高度可扩展、高性能的容器编排服务，它支持Docker 容器，并允许您在AWS 上轻松运行和扩展容器化应用程序。

*ECS*是阿里云提供的一种基础云计算服务。使用云服务器*ECS*就像使用水、电、煤气等资源一样便捷、高效。



**RDS**： 云数据库（Relational Database Service，简称*RDS*）是一种稳定可靠、可弹性伸缩的在线数据库服务。

基于飞天分布式系统和全SSD盘高性能存储，支持MySQL、SQL Server、PostgreSQL和PPAS（高度兼容Oracle)引擎，默认部署主备架构且提供了容灾、备份、恢复、监控、迁移等方面的全套解决方案，彻底解决数据库运维的烦恼。

Amazon Relational Database Service (Amazon RDS) 让您能够在云中轻松设置、运行和扩展**关系数据库**。它在自动执行耗时的管理任务（如硬件预置、数据库设置、修补和备份）的同时，可提**供经济实用的可调容量**。这使您能够腾出时间专注于应用程序，为它们提供所需的快速性能、高可用性、安全性和兼容性。

Amazon RDS 在多种类型的数据库实例（**针对内存、性能或 I/O 进行了优化**的实例）上均可用，并提供**六种常用的数据库引擎**供您选择，包括 Amazon Aurora、PostgreSQL、MySQL、MariaDB、Oracle 和 Microsoft SQL Server。您可以使用 AWS Database Migration Service 轻松将您现有的数据库迁移或复制到 Amazon RDS。



**DynamoDB**: 非关系数据库，适用于在任何规模都需要高性能的应用程序

Amazon DynamoDB 是一种非关系数据库，可在任何规模提供可靠的性能。它是一种完全托管的多区域、多主表数据库，可实现不到 10 毫秒的一致延迟，并提供内置的安全性、备份和还原以及内存中的缓存。

超过 100000 位 AWS 客户选择了 DynamoDB，用于移动、Web、游戏、广告技术、IoT 以及许多其他需要低延迟数据访问的应用程序。为您的应用程序创建一个新表，其他的交给 DynamoDB。Amazon DynamoDB 是一种完全托管的 NoSQL 数据库服务，提供快速且可预测的性能，同时还能够实现无缝扩展。使用 DynamoDB，您可以免除操作和扩展分布式数据库的管理工作负担，因而无需担心硬件预置、设置和配置、复制、软件修补或集群扩展等问题。此外，DynamoDB 提供了加密静态，这可以消除在保护敏感数据时涉及的操作负担和复杂性。



**SQL 和 NoSQL 的区别**：https://www.jianshu.com/p/b32fe4fe45a3

SQL (Structured Query Language) 数据库，指关系型数据库 - 主要代表：SQL Server，Oracle，MySQL(开源)，PostgreSQL(开源)。

NoSQL（Not Only SQL）泛指非关系型数据库 - 主要代表：MongoDB，Redis，CouchDB。

NoSQL相对SQL来讲,关联性相对更自由.限制也较少. 可以更自由的使用。

1.实质。    非关系型数据库的实质：非关系型数据库产品是传统关系型数据库的功能阉割版本，通过减少用不到或很少用的功能，来大幅度提高产品性能。

2.价格。目前基本上大部分主流的非关系型数据库都是免费的。而比较有名气的关系型数据库，比如Oracle、DB2、MSSQL是收费的。虽然Mysql免费，但它需要做很多工作才能正式用于生产。

3.功能。    实际开发中，有很多业务需求，其实并不需要完整的关系型数据库功能，非关系型数据库的功能就足够使用了。这种情况下，使用性能更高、成本更低的非关系型数据库当然是更明智的选择。



**K8S**:kubernetes，首先，他是一个全新的基于容器技术的分布式架构领先方案。Kubernetes(k8s)是Google开源的**容器集群管理系统**（谷歌内部:Borg）。**在Docker技术的基础上，为容器化的应用提供部署运行、资源调度、服务发现和动态伸缩等一系列完整功能，提高了大规模容器集群管理的便捷性。**

https://linux.cn/article-8858-1.html

https://blog.csdn.net/skh2015java/article/details/80300562

     这样说，当你有多个物理服务器，并且需要多个服务共同相互协同，但你总怕某一天，哪台物理服务器宕机了，全部服务就此傻掉了，你要马上发现并，开始在新的服务器上再部署一边。当然这样不是不可以，但，你发现问题需要时间，再弄一台服务器需要 时间，重新部署一份服务，需要更多时间，怎么办！！！这时候，为了避免上面宕机带来的一系列问题，推荐你使用k8s ，它有自检机制当多个物理服务器集群环境里，当有一台服务宕机，或某此情况 不能提供服务时，k8s 用调度集群里的其它Node 来运行这些服务，并且你不用担心因物理机的变动 带来的一系列IP 的变动， 因为K8S 有自己的对服务IP 的定义 ，不会因为项目在一个集群里的迁移而带来IP 等麻烦。
    
    情况二，假设你还没用k8s，但你想到了，负载均衡，你可能用的nginx 或 haproxy 来代理后端的服务，但在你更新项目时，你需要做的是一个项目的多个冗余，你需要 一个一个的操作更新，这其中你还不能出错，并且不能按时保证。
    
    这个时候 ，你应该想k8s ，它是以配置文件维护的。你只需要一个命令，或更新一下配置文件的镜像版本 ，重新提交，k8s会自动的一个一个把旧的版本替换掉，当你的冗余是一个的时候 ，它会直接生成一个新的版本，当新版本生成完成，才会把 旧的替换到，它总能保持正常业务的运行


**SpringBoot新建项目: **https://blog.csdn.net/gnail_oug/article/details/80094047



**gitlab：**

https://mritd.me/2017/11/28/ci-cd-gitlab-ci/



#### 7 注解学习

**@Autowired**：@Autowired注解是按类型装配依赖对象，默认情况下它要求依赖对象必须存在，如果允许null值，可以设置它required属性为false。在Spring框架进行bean对象依赖注入时，@Autowired利用可以对成员变量、方法和构造函数进行标注，来完成自动装配的工作。

https://muyinchen.github.io/2017/08/23/Spring5%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90-@Autowired/



`@Component`, `@Service`, `@Controller`, `@Repository`是spring注解，注解后可以被spring框架所扫描并注入到spring容器来进行管理 。
`@Component`是**通用注解**，其他三个注解是这个注解的拓展，并且具有了特定的功能 
`@Repository`注解在**持久层**中，具有将数据库操作抛出的原生异常翻译转化为spring的持久层异常的功能。 
`@Controller`层是spring-mvc的注解，具有**将请求进行转发，重定向**的功能。 
`@Service`层是业务逻辑层注解，这个注解只是标注该类处于**业务逻辑层**。 
用这些注解对应用进行分层之后，就能将请求处理，义务逻辑处理，数据库操作处理分离出来，为代码解耦，也方便了以后项目的维护和开发。



[**@Slf4j注解实现日志输出**](https://blog.csdn.net/qq_26525215/article/details/79182628)

```
@Slf4j
public class ValidatorAction {
    public void printValidatorResult(Set<ConstraintViolation<ValidatorBean>> set1){
        for(ConstraintViolation<ValidatorBean> constraintViolation:set1){
            log.info("错误: "+constraintViolation.getMessage());
            log.info("字段: "+constraintViolation.getPropertyPath().toString());
        }
     }
}
```

https://blog.csdn.net/HeatDeath/article/details/79833880



@Bean ：Spring的@Bean注解用于告诉方法，产生一个Bean对象，然后这个Bean对象交给Spring管理。产生这个Bean对象的方法Spring只会调用一次，随后这个Spring将会将这个Bean对象放在自己的IOC容器中。

https://www.jianshu.com/p/93727fa9bf23

https://www.jianshu.com/p/2f904bebb9d0

https://www.cnblogs.com/soundcode/p/6477974.html



@Value: 通过@Value将外部配置文件的值动态注入到Bean中。

https://www.cnblogs.com/wangbin2188/p/9014837.html



@RestController:注解是它继承自@Controller注解。4.0之前的版本，spring MVC的组件都使用@Controller来标识当前类是一个控制器servlet。 返回的数据不是html标签的页面，而是其他某种格式的数据时（如json、xml等）使用RestController；

https://blog.csdn.net/u010412719/article/details/69710480



@RequestMapping : 是Spring Web 应用程序中最常被用到的注解之一。这个注解会将 HTTP 请求映射到 MVC 和 REST 控制器的处理方法上。 

https://www.iteye.com/news/32657/



**@RequestParam**：在SpringMVC后台控制层获取参数的方式主要有两种，一种是request.getParameter("name")，另外一种是用注解@RequestParam直接获取。这里

https://www.cnblogs.com/caoyc/p/5635427.html

https://www.cnblogs.com/jpfss/p/7910026.html

```
1 @RequestMapping("user/add")
2 public String add(@RequestParam("name") String name,
3             @RequestParam("age") int age){
4         System.out.println(name+","+age);
5     return "hello";
6 }
当我们请求路径为：http://localhost:8080/springmvc-1/user/add?name=caoyc&age=18
输出结果：caoyc,18
```



**@PreAuthorize**：@PreAuthorize 注解适合进入方法前的权限验证， @PreAuthorize可以将登录用户的roles/permissions参数传到方法中。 @PreAuthorize可以兼顾，角色/登录用户权限，参数传递给方法等等。



**@ApiOperation**:不是spring自带的注解，是swagger里的 
com.wordnik.swagger.annotations.ApiOperation;

@ApiOperation和@ApiParam为API生成做的注解，个参数说明如下： 
@ApiOperation(value = “接口说明”, httpMethod = “接口请求方式”, response = “接口返回参数类型”, notes = “接口发布说明”；其他参数可参考源码； 
@ApiParam(required = “是否必须参数”, name = “参数名称”, value = “参数具体描述”



@ApiResponse

用在@ApiResponses中，一般用于表达一个错误的响应信息
code：数字，例如400
message：信息，例如”请求参数没填好”
response：抛出异常的类

实际项目中非常需要写文档，提高Java服务端和Web前端以及移动端的对接效率。

Swagger是当前最好用的**Restful API文档生成的开源项目**，通过swagger-spring项目

实现了与SpingMVC框架的无缝集成功能，方便生成spring restful风格的接口文档，

同时swagger-ui还可以测试spring restful风格的接口功能。



**@Getter和@Setter** :出现的目的是
public int getFoo() {return foo;} 不需要在写get 和 set 方法。

您可以使用@Getter或@Setter来注释任何字段，以使lombok自动生成默认的getter / setter。

https://www.jianshu.com/p/93353398e964

https://blog.csdn.net/qq_37192800/article/details/79785906



Java的常见术语（PO/POJO/VO/BO/DAO/DTO）

https://www.cnblogs.com/wjn563/p/3967235.html

https://blog.csdn.net/wyx0224/article/details/81190792



JPA之@Entity、@Table、@Column、@Id:Java Persistence API定义了一种定义，可以将常规的普通Java对象（有时被称作POJO）映射到数据库。
这些普通Java对象被称作Entity Bean。
除了是用Java Persistence元数据将其映射到数据库外，Entity Bean与其他Java类没有任何区别。
事实上，创建一个Entity Bean对象相当于新建一条记录，删除一个Entity Bean会同时从数据库中删除对应记录，修改一个Entity Bean时，容器会自动将Entity Bean的状态和数据库同步。

https://www.cnblogs.com/xuwenjin/p/8830850.html



**@Scheduled**: @Scheduled注解为定时任务，cron表达式里写执行的时机

https://blog.csdn.net/qq_33556185/article/details/51852537



**@Mapper**：添加了@Mapper注解之后这个接口在编译时会生成相应的实现类，这个接口中不可以定义同名的方法，因为会生成相同的id，也就是说这个接口是不支持重载的

https://blog.csdn.net/phenomenonsTell/article/details/79033144





**Lombok**: https://zhuanlan.zhihu.com/p/32779910

主要减少一些 get/set/toString 方法的编写



**mock**：https://juejin.im/post/59c3a3ba6fb9a00a496e6397

https://blog.csdn.net/sdyy321/article/details/38757135



Java8 的map 新增方法：

https://irusist.github.io/2016/01/04/Java-8%E4%B9%8BMap%E6%96%B0%E5%A2%9E%E6%96%B9%E6%B3%95/



#### 8 json

https://www.json.org/json-zh.html

https://blog.csdn.net/xiazdong/article/details/7059573



#### 9 http and websocket

http://www.ruanyifeng.com/blog/2016/08/http.html

http://www.ruanyifeng.com/blog/2017/05/websocket.html



#### 10 enum枚举深入理解 

https://blog.csdn.net/javazejian/article/details/71333103

```
public final class ActionEnumImpl extends Enum {
	//私有构造函数 只能由编译器调用
    private ActionEnumImpl(String s, int i) {
        super(s, i);
    }
    private final String name; //枚举字符串名称
    private final int ordinal;//枚举顺序值

..........

    public static final ActionEnumImpl STOP;
    public static final ActionEnumImpl RIGHT;
    public static final ActionEnumImpl LEFT;

    static  {
        STOP = new ActionEnumImpl("STOP", 0);
        RIGHT = new ActionEnumImpl("RIGHT", 1);
        LEFT = new ActionEnumImpl("LEFT", 2);
    }
}
枚举其实是一种特殊的java类，每一个枚举的成员变量相当于类的实例。
构造函数中的s对应name，i对应ordinal，是枚举中的基本要素。

```



#### 11 JPA ORM

JPA、Hibernate、Spring data jpa之间的关系

https://my.oschina.net/u/3080373/blog/1828589?p=2



Hibernate

https://segmentfault.com/a/1190000013568216



spring JPA

https://juejin.im/post/5aa733af518825558a0646fb

https://segmentfault.com/a/1190000015047290

复合主键： https://segmentfault.com/a/1190000014865889



Mybatis



#### 12 log4j

https://www.tianmaying.com/tutorial/log4j

https://blog.csdn.net/tterminator/article/details/53559936  配置多个logger



#### 13 spring



#### 14 springMVC



#### 15  ? extends T 与 ? super T 解惑

https://segmentfault.com/a/1190000008423240

父类引用可以指向其子类，子类引用却不能指向父类。

List<? extends Integer>  list-- ？表示Integer类型或者其子类，list不能写入，因为不确定其存储类型，存入的类型不一定能转成实际的？类。只能保证读出的类型可转换成Integer类型。

List<? super Integer>  list-- ？表示Integer类型或者其父类，list不能读取，因为不确定读出来的类型，只能读Object类型。可以写入，Integer类型或者Integer的子类，因为写入的类型可以转换成？类型。

PECS原则，Producter使用Extends, 用来读取，程序是生产者，对外生产数据，外部程序读取生产者的内容。

消费者模式使用super,用来写入，程序是消费者，读取外部程序的内容。



#### 16 .gitlab-ci.yml介绍

JB的git之旅-gitlab ci介绍：https://juejin.im/post/5afd42be6fb9a07aaa11793f

 [JB的git之旅--.gitlab-ci.yml介绍- 掘金](https://juejin.im/post/5b1a4438e51d4506d1680ee9)

[YAML 语言教程- 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2016/07/yaml.html)

语法介绍：https://www.jianshu.com/p/e091df2ff1c4

gradle ： http://www.open-open.com/lib/view/open1447139848053.html



```
public T get() --- 返回当前线程可用的实际value值
	获取当前线程，拿到当前线程的filed:ThreadLocalMap, map的key是threadLocal变量，
	value是实际的值
	如果map为空
		调用ThreadLocal的初始化函数初始化value值
		new一个ThreadLocalMap，并存入一个键值对，key是this，即当前ThreadLocal本身引用
		value是刚才初始化的value值
			注意map的实现方式，内部是一个Entry数组，数组的元素不是链表，
			当key求得的下标冲突时候，使用线性探测发，将下标加一后再判断
			且Entry继承了WeakReference<ThreadLocal<?>>
			包含1个field：value，就是存入的value值.
			key被用在初始化父类构造函数了,
			super(key)，在后面从map读取数据的时候拿来和传入的key比较
  
	如果map不为空
		根据key,拿到entry的值
		返回entry的value值。


```