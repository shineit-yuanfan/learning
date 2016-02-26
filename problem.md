linux下安装odoo
==========
什么是odoo？
odoo是用python语言编写的应用系统，运行在python的环境下的系统。因其开源性，强大的底层结构，可以根据自身要求，量身打造适合自己的ERP系统和电子商务系统。

为什么我们要用源代码安装odoo
------------

   源码安装实际上就是直接在源代码下运行odoo，而不是去安装他。他的好处在于他更新方便。模块开发人员可以很容易的使用。相比于其他方式可以更加灵活的启动和停止。它提供了更大的控制系统设置，允许多个odoo并行运行。

安装odoo库
----------------
从git的仓库克隆出odoo的库

	git clone https://github.com/odoo/odoo.git

（注意：克隆时间可能会比较长，因为需要克隆整个odoo项目的历史）

####安装相关文件

安装odoo库时，需要同时进行一些对配置文件的相关操作，作为支持odoo运行的一些辅助文件，或者是组成文件。

下载Python 2.7
----------
####为什么我们要下载python

因为odoo是运行在python下的系统，所以当我们安装odoo时应该先检测仪下我们的系统中是否

安装python。注意odoo只能运行在python版本2.7到3.0之间。3.0及以上odoo无法正常运行。

以下是源码安装python2.7的方法。
	
	sudo wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz

解压

	sudo tar zxvf Python-2.7.9

编译与安装

	sudo./configure --prefix=user/clcal/python2.7

通过添加--prefix用于指定python的安装路径于/usr/local/python2.7,配置完成后，我们就可以执行make操作了.

	make
	sudo make install
这样，我们就安装完python 2.7了。

PostgreSQL的安装
---------------
在odoo的使用中，我们需要用到一个本地的数据库PostgreSQL，通过以下命令安装

	sudo apt-get install postgresql postgresql-client


pip的安装
-----------
###pip介绍：

  pip是时python软件安装包管理系统，可以通过pip安装一些命令控制工具以及其他的东西。可以用来安装和管理软件包。可以用来很方便的安装或者删除python软件包。

  pip install some-package-name用来安装

  pip uninstall some-package-name用来删除

  pip使用方法
  使用pip安装文件  pip install SomePackage

  查看具体安装文件 pip show --files SomePackage

  卸载软件包       pip uninstall SomePackage
###为什么要使用pip
   odoo除了使用自己的数据库外，还要依赖一些外部的第三方库。而这些库则需要pip来下载。为了方便，我们将这些第三方库打包在了一个requirements.txt文件中。

安装pip：

 	sudo apt-get install python-pip

通过pip安装requirements.txt文件
---------------------
	
	pip install -r requirements.txt

requirements.txt中添加了odoo的所有依赖包及其精确版本号。

  由于在不同的虚拟机下，可能会出现不同的问题。requirements.txt文件下的库也不一定全部由python语言编写所以在安装过程中，可能会出现报错。如：



  可能遇到的问题1： 
	postgresql-server-X.Y没有安装

	Error: You need to install postgresql-server-dev-X.Y for building a

 	server-side extension or libpq-dev for building a client-side 			application.


>Cleaning up...
>  Removing temporary dir /tmp/pip_build_hsun...
>Command python setup.py egg_info failed with error code 1 in /tmp/pip_build_hsun/psycopg2
>Exception information:
>Traceback (most recent 允许多个ocall last):
>  File "/usr/lib/python2.7/dist-packages/pip/basecommand.py", line 122, in main
>    status = self.run(options, args)
>  File "/usr/lib/python2.7/dist-packages/pip/commands/install.py", line 278, in run
>    requirement_set.prepare_files(finder, force_root_egg_info=self.bundle, bundle=self.bundle)
>  File "/usr/lib/python2.7/dist-packages/pip/req.py", line 1230, in prepare_files
>    req_to_install.run_egg_info()
>  File "/usr/lib/python2.7/dist-packages/pip/req.py", line 326, in run_egg_info
>    command_desc='python setup.py egg_info')
>  File "/usr/lib/python2.7/dist-packages/pip/util.py", line 715, in call_subprocess
>    % (command_desc, proc.returncode, cwd))
>InstallationError: Command python setup.py egg_info failed with error code 1 in /tmp/pip_build_hsun/psycopg2

    通过报错信息可以看出是没有安装postgresql-server-dev-X.Y出现的问题。所以我们可
以安装postgresql-server-dev-9.3 （9.3是版本号）来解决问题。只要执行             sudo apt-get install postgresql-server-dev-9.3即可解决问题


  可能遇到的问题2：

安装lxml包 出错log
>Downloading/unpacking lxml==3.4.1 (from -r requirements.txt (line 17))
>  Downloading lxml-3.4.1.tar.gz (3.5MB): 3.5MB downloaded
>  Running setup.py (path:/tmp/pip_build_root/lxml/setup.py) egg_info for package lxml
>    /usr/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'bugtrack_url'
>      warnings.warn(msg)
>    Building lxml version 3.4.1.
>    Building without Cython.
>    ERROR: /bin/sh: 1: xslt-config: not found
    
	    make sure the development packages of libxml2 and libxslt are installed 
    
>    Using build configuration of libxslt
    
>    warning: no previously-included files found matching '*.py'

 这个报错信息中，可以通过make sure the development packages of libxml2 and libxslt are installed看出，我们是需要安装libxml2和libxsit。所以解决办法可以通过安装他们解决。执行sudo apt-get install libxml2-dev 和 sudo apt-get install libxslt1-dev 即可解决问题。
  可能遇到的问题3：
>In file included from Modules/LDAPObject.c:9:

>Modules/errors.h:8: fatal error: lber.h: No such file or directory
  
  python-ldap 是依赖于 OpenLDAP的，所以为了odoo正常安装应添加libsasl2-dev

解决方法

	sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev


NodeJS和NPM的安装

  在Linux中，用你的发行版的软件包管理器安装NodeJS和 NPM。
	
  Node.js是一个开放源代码、跨平台的、可用于服务器端和网络应用的运行环境。

	apt-get install -y npm

	sudo ln -s /usr/bin/nodejs /usr/bin/node

  一旦安装NPM，可以用它来装一些， less-plugin-clean-css:

	sudo npm install -g less less-plugin-clean-css

###警告：

  如果你是在Ubuntu13.10或者Debian wheezy 你需要手动安装之前的NodeJs

	wget -qO- https://deb.nodesource.com/setup | bash -

	apt-get install -y nodejs

运行Odoo
=======
通过执行

	python odoo.py

运行odoo，并在浏览器下打开localhost：8069既可以运行odoo了！






