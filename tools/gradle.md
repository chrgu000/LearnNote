#### Gradle

https://blog.csdn.net/heqiangflytosky/article/details/50853268

https://www.zhihu.com/question/30432152



Gradle是一种构建工具，它抛弃了基于XML的构建脚本，取而代之的是采用一种基于Groovy的内部领域特定语言，建议可以先熟悉一下Groovy脚本。

gradle明明一般是./gradlew +参数， gradlew代表 gradle wrapper，意思是gradle的一层包装，大家可以理解为在这个项目本地就封装了gradle，即gradle wrapper， 在gradle/wrapper/gralde-wrapper.properties文件中声明了它指向的目录和版本。只要下载成功即可用grdlew wrapper的命令代替全局的gradle命令。

`./gradlew -v` 版本号
`./gradlew clean` 清除app目录下的build文件夹
`./gradlew build` 检查依赖并编译打包
`./gradlew tasks` 列出所有task
这里注意的是 ./gradlew build 命令把debug、release环境的包都打出来，如果正式发布只需要打Release的包，该怎么办呢，下面介绍一个很有用的命令 assemble， 如：

`./gradlew assembleDebug` 编译并打Debug包
`./gradlew assembleRelease` 编译并打Release的包
除此之外，assemble还可以和productFlavors结合使用：

`./gradlew installRelease` Release模式打包并安装



##### Gradle配置：

Gradle构建脚本 build.gradle 
Gradle属性文件 gradle.properties 
Gradle设置文件 settings.gradle，对于只有一个项目的构建而言是可选的，如果我们的构建中包含多于一个项目，那么它就是必须的，因为它描述了哪一个项目参与构建。每一个多项目的构建都必须在项目结构的根目录中加入一个设置文件。

在Gradle中，有两个基本概念：**项目**和**任务**。请看以下详解：

- **项目**是指我们的构建产物（比如Jar包）或实施产物（将应用程序部署到生产环境）。**一个项目包含一个或多个任务。**
- **任务**是指不可分的最小工作单元，执行构建工作（比如编译项目或执行测试）。

那么，这些概念和Gradle的构建又有什么联系呢？好，**每一次Gradle的构建都包含一个或多个项目**。



`Gradle home`指定了gradle文件目录 
`Service directory path`指定了gradle工作主目录

build.gradle
先看**整个项目的gradle配置**文件：

```
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:1.3.0'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        jcenter()
    }
}
```

内容主要包含了两个方面：一个是声明**仓库的源**，这里可以看到是指明的jcenter(), 之前版本则是mavenCentral(), jcenter可以理解成是一个新的中央远程仓库，兼容maven中心仓库，而且性能更优。 
另一个是声明了**android gradle plugin的版本**，android studio 1.0正式版必须要求支持gradle plugin 1.0的版本

某个Moudle的gradle配置文件：

```
buildscript {
    repositories {
        maven { url 'http://*********' }
    }

    dependencies {
        classpath 'com.android.tools.build:gradle:1.3.1'
    }
}
```



buildscript{}设置脚本的运行环境。
repositories{}支持java依赖库管理，用于项目依赖。





dependencies{}依赖包的定义。支持maven/ivy，远程，本地库，也支持单文件。如果前面定义了repositories{}maven 库，则使用maven的依赖库，使用时只需要按照用类似于com.android.tools.build:gradle:0.4，gradle 就会自动的往远程库下载相应的依赖。


--------------------- 