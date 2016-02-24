linux下安装odoo
==========
为什么我们要用源代码安装odoo
------------

   源码安装实际上就是直接在源代码下运行odoo，而不是去安装他。他更新方便。模块开发人员可以更加容易的使用。相比其他方式可以更加灵活的启动或者停止。它可以提供更大的控制系统设置，可以同时允许多个odoo并行运行。

安装odoo库
----------------
*从git的仓库克隆出odoo的库

	git clone https://github.com/odoo/odoo.git

（注意：克隆时间可能会比较长，因为需要克隆整个odoo项目的历史）

###安装依赖

安装odoo库需要同时配置一些相关操作作为依赖

下载Python 2.7
----------
	
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

创建数据库用户 root，并指定其为超级用户：

	sudo -u postgres createuser --superuser root

登录数据库控制台，设置 root 用户的密码，退出控制台：

	sudo -u postgres psql

pip的安装
-----------
pip介绍：

  pip是时python软件安装包管理系统，可以通过pip安装一些命令控制工具以及其他的东西。可以用来安装和管理软件包。可以用来很方便的安装或者删除python软件包。

  pip install some-package-name用来安装

  pip uninstall some-package-name用来删除

  pip使用方法
  使用pip安装文件  pip install SomePackage

  查看具体安装文件 pip show --files SomePackage

  卸载软件包       pip uninstall SomePackage

安装pip：

 	sudo apt-get install python-pip

通过pip安装requirements.txt文件
---------------------
	
	pip install -r requirements.txt

  在安装过程中，可能会出现报错。如：

 问题1：

>安装psycopg2 出错log ：Error:pg_config executable not found的解决
 


 解决方案

  ** make sure the development packages of libxml2 and libxslt are installed **

Assuming you are running a debian-based distribution

	sudo apt-get install libxml2-dev
	sudo apt-get install libxslt1-dev 

或者安装python开发包

	sudo apt-get install python-dev

as suggested by commenters

  问题2： 
	postgresql-server-X.Y没有安装

>Error: You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.


>Cleaning up...
>  Removing temporary dir /tmp/pip_build_hsun...
>Command python setup.py egg_info failed with error code 1 in /tmp/pip_build_hsun/psycopg2
>Exception information:
>Traceback (most recent call last):
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


解决方法：
	
	sudo apt-get install postgresql-server-dev-9.3


  问题3：

>安装lxml包 出错log
>Downloading/unpacking lxml==3.4.1 (from -r requirements.txt (line 17))
>  Downloading lxml-3.4.1.tar.gz (3.5MB): 3.5MB downloaded
>  Running setup.py (path:/tmp/pip_build_root/lxml/setup.py) egg_info for package lxml
>    /usr/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'bugtrack_url'
>      warnings.warn(msg)
>    Building lxml version 3.4.1.
>    Building without Cython.
>    ERROR: /bin/sh: 1: xslt-config: not found
    
>    ** make sure the development packages of libxml2 and libxslt are installed **
    
>    Using build configuration of libxslt
    
>    warning: no previously-included files found matching '*.py'


解决方法
    ** make sure the development packages of libxml2 and libxslt are installed **

Assuming you are running a debian-based distribution

	sudo apt-get install libxml2-dev
	sudo apt-get install libxslt1-dev 

或者安装python开发包

	sudo apt-get install python-dev

as suggested by commenters


  问题4：
> Downloading requests-2.6.0-py2.py3-none-any.whl (469kB): 372kB downloaded
>Exception:
>Traceback (most recent call last):
>  File "/usr/lib/python2.7/dist-packages/pip/basecommand.py", line 122, in main
>    status = self.run(options, args)
>  File "/usr/lib/python2.7/dist-packages/pip/commands/install.py", line 278, in run
>    requirement_set.prepare_files(finder, force_root_egg_info=self.bundle, bundle=self.bundle)
>  File "/usr/lib/python2.7/dist-packages/pip/req.py", line 1198, in prepare_files
>    do_download,
>  File "/usr/lib/python2.7/dist-packages/pip/req.py", line 1376, in unpack_url
>    self.session,
>  File "/usr/lib/python2.7/dist-packages/pip/download.py", line 572, in unpack_http_url
>    download_hash = _download_url(resp, link, temp_location)
>  File "/usr/lib/python2.7/dist-packages/pip/download.py", line 433, in _download_url
>    for chunk in resp_read(4096):
>  File "/usr/lib/python2.7/dist-packages/pip/download.py", line 421, in resp_read
>    chunk_size, decode_content=False):
>  File "/usr/share/python-wheels/urllib3-1.7.1-py2.py3-none-any.whl/urllib3/response.py", line 225, in stream
>    data = self.read(amt=amt, decode_content=decode_content)
>  File "/usr/share/python-wheels/urllib3-1.7.1-py2.py3-none-any.whl/urllib3/response.py", line 174, in read
>    data = self._fp.read(amt)
>  File "/usr/lib/python2.7/httplib.py", line 573, in read
>    s = self.fp.read(amt)
>  File "/usr/lib/python2.7/socket.py", line 380, in read
>    data = self._sock.recv(left)
>  File "/usr/lib/python2.7/ssl.py", line 341, in recv
>    return self.read(buflen)
>  File "/usr/lib/python2.7/ssl.py", line 260, in read
>    return self._sslobj.read(len)
>SSLError: The read operation timed out


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




	






