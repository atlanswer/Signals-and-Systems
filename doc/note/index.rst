#####
笔记
#####

#. 老师推荐的教程

   #. `学习 Python 的第一步 <https://zhuanlan.zhihu.com/p/252679715>`_
   #. `Jupyter Notebook + Wolfram Engine 配置指南 <https://zhuanlan.zhihu.com/p/168098091>`_

#. 老师推荐的文章

   #. `汉语拼音的四个声调，在波形上反应出来是什么量？ <https://www.zhihu.com/question/38441819>`_

      .. image:: ../doc/WeChat\ Image_20220307222914.png
         :width: 50%

   #. `傅里叶变换与不确定性 <https://www.cnblogs.com/hwBeta/p/6542320.html>`_
   #. `傅里叶变换中的不确定性原理（一） <https://zhuanlan.zhihu.com/p/60638534>`_
   #. `傅里叶变换中的不确定性原理（二） <https://zhuanlan.zhihu.com/p/60835095>`_
   #. `关于不确定性原理的一些看法 <https://zhuanlan.zhihu.com/p/441554945>`_

#. 阶跃函数缩放

   .. image:: ../doc/WeChat\ Image_20220307220903.png
      :width: 50%
   .. image:: ../doc/WeChat\ Image_20220307221140.png
      :width: 50%
   .. image:: ../doc/WeChat\ Image_20220307221208.png
      :width: 50%

#. 思考题

   下面是一位同学提供的求解多谐振复合函数基础周期的新解法，大家可以看看，这个思路是否总是可以快速的给出基础周期

   .. image:: ../doc/WeChat\ Image_20220307221345.png

#. 卷积图解

   .. image:: ../doc/WeChat\ Image_20220307223419.png

#. 典型系统的特性判断

   .. csv-table:: 典型系统的特性判断
      :header: "", "平移", "尺度", "放大", "变量乘", "偏置", "变量加", "微分", "积分", "非线性映射"
      :align: center
      :stub-columns: 1

      "线性",     "Y", "Y", "Y", "INDET", "N", "INDET", "Y", "Y", "N"
      "时不变",   "Y", "N", "Y", "INDET", "Y", "INDET", "Y", "INDET", "Y"
      "因果",     "INDET", "N", "Y", "Y", "Y", "Y", "N", "INDET", "Y"
      "稳定",     "Y", "Y", "Y", "INDET", "Y", "INDET", "Y", "Y", "INDET"
