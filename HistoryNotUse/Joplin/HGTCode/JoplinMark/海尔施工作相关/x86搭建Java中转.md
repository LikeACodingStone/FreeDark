
 -  登录X86  在D盘创建文件夹 Share，设置共享为EveryOne读写权限。
 - 进入控制面版-网络和Internet-网络和共享中心-更改高级共享设置（密码保护的共享-关闭密码保护的共享）。
 - 远程将Java代码和Jdk1.7 放入共享目录Share，安装JDK，一直下一步，然后配置环境变量，
	- JAVA_HOME
	- C:\Program Files\Java\jdk1.7.0_40

	- CLASSPATH
	- .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;

- 在Path最后面加入
	- %JAVA_HOME%\bin
	- %JAVA_HOME%\jre\bin

使用cmd窗口 java 和 javac  命令测试，一定要两个命令都可以使用

 - 启用一下 Application/java/RunPCR.bat 看一下是否正常运行，如果正常运行 将该文件放入
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 路径下，然后再点击一遍（一定要点击）运行启动程序，
最后关闭程序，重启板子就可以了。
- 远程登录账号密码
- Administrator
- 123456
