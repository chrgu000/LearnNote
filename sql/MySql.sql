
# sql语句对大小写不敏感

-- show databases;

/*
DROP database IF EXISTS zhtdb;
create database zhtdb;
use zhtdb;
create table Person 
(
	id int unsigned  auto_increment primary key, #主键
	FirstName  varchar(10) not null,
	Address varchar(50),
	City varchar(30),
	Age int unsigned
);

insert into Person (FirstName, Address) values ("lester","PiDu");
insert into Person values (null, 'zht','jiaoda','chengdu', 22); 
# 对text，使用单引号，部分数据库也识别双引号, 对应数字，不需要引号

insert into Person values (null, 'zht','jiaoda2','chengdu2',23);
#insert into Person values (null, 'bzht','jiaoda3','chengdu',24);



select * from Person;
select FirstName,Address,City from Person;
select FirstName,Address from Person;

# 关键词 DISTINCT 用于返回唯一不同的值。 
select distinct firstname from person;

select * from person where city='chengdu';

*/

use zhtdb;
select * 
from Products;

-- 这个注释符合和注释之间必须有空格间隔，否则会报错

-- 返回单列不同的值，如果返回2列，则会返回所有值
select distinct vend_id 
from products;

-- 返回输出集中的前3个
select vend_id 
from products limit 3;

-- 数据库的行数是从0开始
select vend_id 
from products limit 3 offset 1; -- 从第1行开始，返回后面3行，可等效 limit 3, 1

-- 排序， order by 应该位于句子最后位置
select prod_name
from products;

select prod_name
from products 
order by prod_name;

-- 只有在prod_price相同时候，才会按照prod_name排序
select prod_id, prod_price, prod_name
from products 
order by prod_price, prod_name;

-- SQL排序默认是按照升序进行（ASC）, 如果降序需要使用 DESC，放在每个列名后面
-- 只有在prod_price相同时候，才会按照prod_name排序
-- 对prod_price按照降序， 相同的prod_price，按照prod_name降序升序排列
select prod_id, prod_price, prod_name
from products 
order by prod_price desc, prod_name; -- 等效于： order by 2 desc, 3;

select prod_name, prod_price
from products
where prod_price < 10;

select vend_id, prod_name
from products
where vend_id != 'DLL01';

select prod_name, prod_price
from products
where prod_price between 5 and 10;

select *
from customers
where cust_email is null;

select * 
from products
where vend_id = 'DLL01' and prod_price <= 4;

select * 
from products
where vend_id = 'DLL01' or vend_id = 'BRS01';

select * 
from products
where vend_id = 'DLL01' or vend_id = 'BRS01'
and prod_price > 10;

select * 
from products
where (vend_id = 'DLL01' or vend_id = 'BRS01')
and prod_price > 10;

select prod_name , prod_price, vend_id
from products
where vend_id in ('DLL01','BRS01')
order by prod_price;

select prod_name , prod_price, vend_id
from products
where not vend_id  = 'DLL01'
order by prod_price;

select *
from products
where prod_name like 'Fish%'; -- 等同于 'fish%'


select *
from products
where prod_name like '%bean bag%';

select prod_name
from products
where prod_name like '__ inch%'; --  _ 匹配单个任意字符

select prod_name
from products
where prod_name like '[FB]%'; -- 匹配F或者B开头的,,mysql不支持？？？

select vend_name,'(', vend_country, ')' -- 没有连接效果，需要使用 concat 
from vendors
order by vend_name;


select concat(vend_name,'(', vend_country, ')')
from vendors
order by vend_name;

select concat(vend_name,'(', vend_country, ')')
as vend_title -- 定义一个别名
from vendors
order by vend_name;

select prod_id, quantity, item_price,
quantity * item_price as expanded_price
from orderItems
where order_num = 20008;


-- select是简单的访问和处理表达式
select 3 * 7;

select trim('    abc   ');

select now();

select vend_name , upper(vend_name) as vend_upper
from vendors
order by vend_name;

select *
from orders 
where year(order_date) = 2012; -- 提取年份

select avg(prod_price) as avg_price
from products;


select avg(prod_price) as avg_price
from products
where vend_id = 'DLL01';

select count(*) as count_cust -- 使用 * 包含列中的null
from customers;

select count(cust_email) as count_email -- 使用 非* 不包含列中的null
from customers;

select max(prod_price) 
from products;

select min(prod_price) as min_price 
from products;

select sum(quantity) 
from orderItems
where order_num = 20005;

select sum(quantity * item_price) 
from orderItems
where order_num = 20005;

select avg(distinct prod_price) as avg_price_distinct
from products
where vend_id='DLL01';


select count(*) as num_items,
	min(prod_price) as price_min,
	max(prod_price) as price_max,
	avg(prod_price) as price_avg
	from products;
	
	
select vend_id, count(*) as num_prods
from products
group by vend_id; 

	
select vend_id, count(*) as num_prods
from products
group by vend_id;

select cust_id, count(*)
from orders
group by cust_id;

select *, count(*) -- 分组之后，对某个分组，如果其他列大于1行，则只显示第一行。
from orders
group by cust_id
having count(*) >= 2; -- having 对group by 的条件限制


select vend_id , count(*)
from products
where prod_price >= 4
group by vend_id
having count(*) >= 2;

select *
from orderItems;

select order_num, count(*) as items
from orderItems
group by order_num
having items >= 3;

select order_num, count(*) as items
from orderItems
group by order_num
having items >= 3
order by items,  order_num; -- 对分组进行排序

-- 子查询, 查询订购物品 RGAN01 的顾客信息，根据物品查询订单号，根据订单号查询顾客id,根据顾客id查出顾客信息
select order_num
from orderItems
where prod_id = 'RGAN01';

select cust_id
from orders
where order_num in (select order_num
from orderItems
where prod_id = 'RGAN01');

select *
from customers
where cust_id in (select cust_id
from orders
where order_num in (select order_num
from orderItems
where prod_id = 'RGAN01'));


-- 显示顾客表中每个顾客的订单总数, 子查询作为字段
select 
	cust_name,
	cust_state,
	(select count(*) from orders where orders.cust_id = customers.cust_id) as cust_orders
from customers
order by cust_name;


select vend_name, prod_name, prod_price
from vendors, products; -- 输出笛卡尔积，vend_name的所有行（n）分别和prod_name, prod_price每一行(m)配对,结果是:n*m


select vend_name, prod_name, prod_price -- vend_name, vendors.vend_id, prod_name, prod_price
from vendors, products
where vendors.vend_id = products.vend_id; --  对之前的笛卡尔输出集进行过滤

-- 查看表结构
select 'orderitems';
select * from orderitems limit 1;
select 'products';
select * from products limit 1;
select 'vendors';
select * from vendors limit 1;
select 'customers';
select * from customers limit 1;
select 'orders';
select * from orders limit 1;


-- 输出订单号为 20007 的产品名，供应商名字，产品价格，订单数量
select order_num,prod_name, vend_name,  prod_price, quantity
from vendors, products, orderItems -- 表的顺序可以是任意
where order_num = 20007
and vendors.vend_id = products.vend_id
and orderItems.prod_id = products.prod_id;




-- 返回订购产品 prod_id：RGAN01 的顾客信息，cust_name顾客名字、联系信息  prod_id:RGAN01 
-- orderitems.order_num / prod_id
-- orders.cust_id / order_num--> customers.cust_id/name
select cust_name, cust_contact
from customers,orders,orderItems
where orderitems.prod_id = 'RGAN01'
	and orderItems.order_num = orders.order_num
	and orders.cust_id = customers.cust_id;
	
select *
from orderItems
order by order_num,order_item;


-- 外联结，包含没有关联行的行,null
-- 检索所有的顾客，及其订单号
select C.*, O.order_num
from customers as C, Orders as O
where c.cust_id = o.cust_id;

select customers.cust_id, Orders.order_num
from customers left outer join Orders -- 外联结，包括没有订单号的顾客
on customers.cust_id = Orders.cust_id;

select customers.cust_id, Orders.order_num
from customers right outer join Orders -- 外联结，包括没有订单号的顾客
on customers.cust_id = Orders.cust_id;

select customers.cust_id, Orders.order_num
from Orders  right outer join customers -- right 外联结，通过调整表的顺序可以做到等效 left
on customers.cust_id = Orders.cust_id;

-- 检索所有的顾客，以及每个顾客的订单数
select customers.cust_id,customers.cust_name, count(orders.order_num)
from customers inner join orders
on orders.cust_id = customers.cust_id
group by orders.cust_id;

select customers.cust_id,customers.cust_name, count(orders.order_num)
from customers left outer join orders
on orders.cust_id = customers.cust_id
group by orders.cust_id;

-- 等效上面的语句
select customers.cust_id,customers.cust_name,
	(select count(order_num) from orders where customers.cust_id = orders.cust_id)
from customers;


select cust_name, cust_contact, cust_email, cust_state
from customers
where cust_state in ('IL', 'IN', 'MI')
union 
select cust_name, cust_contact, cust_email, cust_state -- 第二个选择参数要和第一个保持一致，否则输出数据异常
from customers
where cust_name = 'Fun4All';


select cust_name, cust_contact, cust_email, cust_state
from customers
where cust_state in ('IL', 'IN', 'MI')
union all
select cust_name, cust_contact, cust_email,cust_state
from customers
where cust_name = 'Fun4All';

/*
drop table if exists student;
CREATE TABLE Student
(
  id  int  NOT NULL auto_increment primary key,
  update_date datetime default current_timestamp() ,
  name  char(10) NOT NULL ,
  age int default 18,
  score double
);

insert into student (name,age,score) values('a',17,39);
insert into student (name,score) values('b',39);
select * from student;

*/



DROP TABLE IF EXISTS tb_article;
 
CREATE TABLE tb_article (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL DEFAULT '',
  summary varchar(1024) NOT NULL DEFAULT '',
  status int(11) NOT NULL DEFAULT '0',
  type int(11) NOT NULL,
  user_id bigint(20) NOT NULL DEFAULT '0',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  public_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

show tables;
select * 
from tb_article;
