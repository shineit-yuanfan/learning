 数据库从新开启命令：
 
 pg_ctl -D /usr/local/var/postgres start
 
@api.depends前面要不要加taken_seats 


重启是涉及到py文件

升级是涉及到数据文件

要同时进行重启和升级需要改动python文件的定义类改变。

###开发遇到的问题
####日历视图  
   无法import
   
    from datetime import time
    
    
@http.route装饰器可以根据具体的函数返回信息进行路径分发和控制访问权限。

有关ir.action.act_window的介绍在https://www.odoo.com/documentation/9.0/reference/actions.html#window-actions-ir-actions-act-window

####定义日期

	default=fields.Date.context_today
给一个时间是今天的默认值

####constraints的作用

  自动验证，当发生异常时，报错。
  
####方法

#####create创建
#####write修改
#####copy拷贝
#####unlink删除
#####search查找
###xpath

除了通过字段名定为，我们可以通过xpth定位任何一个节点。


###transientModel
用来临时存放数据

###wizard用法

在action行动中添加数据
src_model里面填写依赖的表
res_model里面为wizard的表
key2里面可以控制出现的位置。



    
    
    
    
  