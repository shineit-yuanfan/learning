安装Odoo
----------

有很多方法可以安装Odoo，或者你可以不用安装，这取决于你要用它干什么。

这个文档介绍了大多数的安装选项。

:ref:`setup/install/demo`

最简单的安装只适合快速的Odoo尝试或者找一找感觉。

:ref:`setup/install/saas`

开始从全面迁移管理OdooS.A.，可以用两个方法测试Odoo，并用他服务与你的企业。但是限制了系统的灵活性（检查：没有自定义模块？还有呢？）

可以用来测试Odoo和长期“生产”使用。

:ref:`setup/install/packaged`

很容易去开始，带来更多灵活性的托管性与方便部署性，更好的控制数据储存。但是把维护的责任转移给了用户。

很容易的测试出Odoo的显影模块和可用于与其他部署和维护工作长期生产使用。

:ref:`setup/install/source`

比之前更难入手:ref:`setup/install/packaged`提供了更大的灵活性。但打包安装程序通常不允许多个odoo程序运行在同一个系统上,也不提供简单源用来访问Odoo本身。

良好的开发模块,可以用作生产部署的基础。

源代码可以通过下载压缩包或使用git获得。使用git更易于更新,有助于多个版本之间切换(包括当前开发版本)。

docjer image
--------

如果你常常用到docker进行开发和部署，官方docker基础图像可用。可以查看图像帮助手册获取更多的信息。

演示
-------

为了简单的得到的想法在Odoo中，演示实例是很有用的，他们共享实例，在这几个小时里，可以浏览和尝试没有递交的东西。

演示实例不需要本地安装,只需要一个web浏览器。

SaaS/租用模式
-------

Odoo提供了免费的私人实例。如果用来在非代码操作时检测和测试Odoo时不需安装。

像演示实例,SaaS实例不需要本地安装,一个web浏览器就足够了。

打开安装程序
--------

Odoo提供了基于Windows，deb-based分布（Debian，Ubuntu，....）和基于rpm的发行版（Fedora，CentOS，RHEL，....）的安装程序。


这些包可以用默认项。但很难判断是最新的。

官方包所有相关需求可在http//nightly.odoo.com上找到。

Windows
-----------

•下载地址https://nightly.odoo.com/9.0/nightly/exe/odoo_9.0.latest.exe

•运行下载文件

  警告

  在Windows 8,你可能会看到一个警告题为“Windows保护你的电脑。”点       击:guilabel:“更多信息”:guilabel:“运行”

•接受UAC提示

•通过各种安装步骤

Odoo结束时将自动开始安装。

组态
--------

设置配置文件  reference/cmdline/config 可以发现：文件 `{%PROGRAMFILES%}\\Odoo 9.0-{id}\\server\\openerp-server.conf`.

配置文件可以连接到一个远程编辑Postgresql,编辑文件位置或设定dbfilter。

重新加载配置文件,重启Odoo服务通过:menuselection:“服务- - > Odoo服务器”。

Deb

安装9.0 Odoo Debian-based分布,作为根用户执行以下命令:

	 # wget -O - https://nightly.odoo.com/odoo.key | apt-key add -
 	# echo "deb http://nightly.odoo.com/9.0/nightly/deb/ ./" >> /etc/apt/sources.list

 	# apt-get update && apt-get install odoo

这将自动安装所有默认项,安装Odoo本身作为一个守护进程,并自动启动它。

！危险！

打印的PDF报告,您必须安装wkhtmltopdf:wkhtmltopdf可用在debian存储库的版本不支持页眉和页脚,所以不能自动安装。推荐的版本是0.12.1 wkhtmltopdf在档案部分下载页面。作为Debian Jessis非官方发布,你可以在http://nightly.odoo.com/extra/上找到。

配置：

设置配置文件<reference/cmdline/config>`可以发现:文件/etc/odoo/openerp-server.conf`。

编辑配置文件时,Odoo必须重新启动才可以从新使用:

 	sudo service odoo restart

 	Restarting odoo: ok

 RPM
-------

 Warning

与RHEL-based分布(RHEL,CenOS,Scientific Linux),EPEL必须用Odoo添加到发行版的存储库可所有的依赖关系上。CenOS:

	sudo yum install -y epel-release

对于其他的RHEL-based内容，查看EPEL文档

	$ sudo yum install -y epel-release

	$ sudo postgresql-setup initdb

	$ sudo systemctl enable postgresql

	$ sudo systemctl start postgresql

	$ sudo yum-config-manager --add-repo=https://nightly.odoo.com/9.0/nightly/rpm/odoo.repo

	$ sudo yum install -y odoo

	$ sudo systemctl enable odoo

	$ sudo systemctl start odoo

！危险！

打印的PDF报告,您必须安装wkhtmltopdf:wkhtmltopdf可用在debian存储库的版本不支持页眉和页脚,所以不能自动安装。使用wkhtmltopdf下载页面上可用的版本。

配置：
---------

设置配置文件`<reference/cmdline/config>`可以发现：文件:`/ etc / odoo / openerp-server.conf`编辑配置文件时,通过SystemD Odoo必须重启:

	$ sudo systemctl restart odoo

源安装
-----------

“安装”的真正来源是不安装Odoo,而直接从源代码运行代替它。

这可以更方便模块开发人员作为Odoo源比使用打包安装更容易(或构建这个文档和信息可用离线)。

这也使得启动和停止Odoo比包装设备设立的服务更灵活和明确，并允许使用压倒一切的设置：参考：`命令行参数<reference/cmdline>`无需编辑配置文件。

最后，它提供了更大的控制系统的设置，并允许更容易地保持（和运行）多个版本odoo并排运行。

有两种方式来获得odoo源的zip和git。

•Odoo链接可以从https://nightly.odoo.com/9.0/nightly/src/odoo_9.0.latest.zip下载的zip文件则需要解压缩使用其内容

•git允许Odoo简单的更新和容易的版本之间切换。它还在简化了维护非模块补丁上做出贡献。 GIT中的主要缺点是，它比一个压缩档明显更大，因为它包含了Odoo项目的整个历史。

Git仓库，https://github.com/odoo/odoo.git。

下载它需要的git客户端（可以通过在Linux发行版可​​用），并且可以使用下面的命令来执行：

$ git clone https://github.com/odoo/odoo.git

安装依赖性
---------

源安装需要手动安装的依赖关系：

•Python 2.7版。

   ◦在Linux和OS X中，包括默认。


   ◦在Windows中，使用官方Python 2.7.9安装程序。

   警告

   安装过程中选择“添加到python.exe路径”，然后重新启动后，确保：envvar：`PATH`更新

   注意

   如果已经安装了Python，请确保它是2.7.9，以前的版本都不太方便和3.x版本不兼容


•PostgreSQL的，使用本地数据库

安装后，您将需要创建一个postgres用户：默认情况下只有用户的Postgres，和Odoo不允许对连接成postgres。

◦在Linux中，使用发行版的包，然后创建一个名为像你登录一个Postgres用户：

$ sudo su - postgres -c "createuser -s $USER"

由于角色的登录是一样的Unix登录Unix套接字可以是不带密码的使用。

◦在OS X上，postgres.app是开始最简单的方法，然后创建一个Postgres用户在Linux上


◦在Windows上，使用PostgreSQL为Windows，然后

      ◾添加PostgreSQL的bin目录（默认为C:\Program Files\PostgreSQL\9.4\bin）添加到您的：envvar：`PATH`

      ◾create与使用PG管理GUI密码的postgres用户：开放pgAdminIII，双击该服务器上创建一个连接，请选择：menuselection：`Edit --> New Object --> New Login Role`，在进入USENAME中：guilabel：`Role Name`（如odoo），然后打开：guilabel：`Definition`选项卡，并输入密码（如odoo），然后单击：guilabel：`OK`。

该用户名和密码必须通过使用任一来Odoo：选项：`-w <odoo.py -w>`和：选项：`-r <odoo.py -r>`选项或：参考：`配置文件<参考/ CMDLINE /配置>`




•在上市Python的相关性：文件：`requirements.txt`文件。

◦在Linux中，python依赖可能是安装与系统管理或使用PIP。

 对于使用本机代码（Pillow，lxml，greenlet，gevent，psycopg2的，ldap）库，可能需要安装开发工具和原生的依赖之前pip是能够安装依赖自己。这些都是在-dev或-devel包的Python，Postgres的，libxml2的，libxslt上，libevent的，libsasl2的libldap2可用的。然后Python可以通过自己自行安装：

	$ pip install -r requirements.txt

◦在 OS X，则需要安装命令行工具（Xcode的选--install），然后下载并安装你的选择（homebrew，MacPorts）安装非Python的依赖关系的软件包管理器。那么pip可以用来安装Python依存关系在Linux上：

	$ pip install -r requirements.txt

◦在Windows，你需要手动安装一些相关性，调整的requirements.txt文件，然后运行pip来安装其剩余的。

安装使用psycopg这里安装http://www.stickpeople.com/projects/python/win-psycopg/

然后编辑requirements.txt文件：
◾removepsycopg2的，你已经拥有了它。
◾remove可选的python-LDAP，GEVENT和psutil因为它们需要编译。
◾addpypiwin32因为它是Windows下的需要。

然后使用PIP安装使用以下命令从CMD.EXE提示的依赖关系（由您下载Odoo的实际路径替换\ YourOdooPath）：

	C:\> cd \YourOdooPath
	C:\YourOdooPath> C:\Python27\Scripts\pip.exe install -r requirements.txt

•较少的NodeJS CSS

◦在Linux中，用你的发行版的软件包管理器安装NodeJS和 NPM。

 警告

 在Debian wheezy和Ubuntu 13.10，你需要手动安装之前的NodeJS：

	$ wget -qO- https://deb.nodesource.com/setup | bash -

	$ apt-get install -y nodejs

 在后来的Debian（>jessie）和Ubuntu（> 14.04），你可能需要添加一个符号作为NPM包调用节点，但debian的调用二进制的NodeJS

	$ apt-get install -y npm

	$ sudo ln -s /usr/bin/nodejs /usr/bin/node

 一旦安装NPM，可以用它来装一些， less-plugin-clean-css:

	$ sudo npm install -g less less-plugin-clean-css

◦在OS X上，通过您首选的软件包管理器（homebrew，MacPorts），然后安装越来越少，less-plugin-clean-css:：

	$ sudo npm install -g less less-plugin-clean-css

◦在Windows下安装的install NodeJS，重启（更新：ENVVAR：`PATH`），并安装一些 less-plugin-clean-css

	C:\> npm install -g less less-plugin-clean-css

运行Odoo
--------

一旦所有的依赖关系成立，Odoo可以通过运行odoo.py推出。

:ref:`Configuration <reference/cmdline>` can be provided either through :ref:`command-line arguments <reference/cmdline>` or through a :ref:`configuration file <reference/cmdline/config>`.

常见的必要的配置是：

•PostgreSQL的主机，端口，用户名和密码。

Odoo已经超越psycopg2的的默认没有违约：在连接端口5432建立一个UNIX SOCKET与当前用户，没有密码。默认情况下这应该在Linux和OS X上运行，但它不会在Windows上工作，因为它不支持Unix套接字。


•在默认设置自定义插件路径来加载自己的模块


在Windows下执行odoo将是一个典型的方式：

C:\YourOdooPath> python odoo.py -w odoo -r odoo --addons-path=addons,../mymodules --db-filter=mydb$

这里的odoo，odoo是PostgreSQL的登录名和密码，../mymodules是额外的插件目录和MYDB默认的数据库服务在localhost：8069

在Unix下执行odoo将是一个典型的方式：
$ ./odoo.py --addons-path=addons,../mymodules --db-filter=mydb$

这里的../mymodules是额外的插件目录和MYDB默认的数据库服务在localhost：8069

