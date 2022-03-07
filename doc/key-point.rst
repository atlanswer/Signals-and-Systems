######
知识点
######

#. 典型系统的特性判断

   .. csv-table:: 典型系统的特性判断
      :header: "", "平移", "尺度", "放大", "变量乘", "偏置", "变量加", "微分", "积分", "非线性映射"
      :align: center
      :stub-columns: 1

      "线性",     "Y", "Y", "Y", "INDET", "N", "INDET", "Y", "Y", "N"
      "时不变",   "Y", "N", "Y", "INDET", "Y", "INDET", "Y", "INDET", "Y"
      "因果",     "INDET", "N", "Y", "Y", "Y", "Y", "N", "INDET", "Y"
      "稳定",     "Y", "Y", "Y", "INDET", "Y", "INDET", "Y", "Y", "INDET"
