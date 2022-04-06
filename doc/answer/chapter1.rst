##############
第一章参考答案
##############

.. note::

  .. list-table:: 评分标准（总分 20）
    :header-rows: 1

    * - 评分
      - 所需分数
      - 对应分数
    * - :math:`\text{A}`
      - :math:`[15, 20]`
      - :math:`100`
    * - :math:`\text{B}`
      - :math:`[10, 15)`
      - :math:`85`
    * - :math:`\text{C}`
      - :math:`[5, 10)`
      - :math:`70`
    * - :math:`\text{D}`
      - :math:`[0, 5)`
      - :math:`0`

.. note::

  #. 装订前确认页面顺序
  #. 装订作业时避免盖住字迹

1.8
  .. image:: assets/1-8.jpg

  (a) :math:`\mathcal{Re}\{x_1(t)\}`
      :math:`= -2 = 2e^{0t}\cos(0t+\pi)`
  (b) :math:`\mathcal{Re}\{x_2(t)\}`
      :math:`= \sqrt{2}\cos{\frac{\pi}{4}}\cos(3t+2\pi)`
      :math:`= \cos(3t) = e^{0t}\cos(3t+0)`
  (c) :math:`\mathcal{Re}\{x_3(t)\}`
      :math:`= e^{-t}\sin(3t+\pi)`
      :math:`= e^{-t}\cos(3t+\frac{\pi}{2})`
  (d) :math:`\mathcal{Re}\{x_4(t)\}`
      :math:`= -e^{-2t}\sin(100t)`
      :math:`= e^{-2t}\sin(100t+\pi)`
      :math:`= e^{-2t}\cos(100t+\frac{\pi}{2})`

1.9
  .. image:: assets/1-9.jpg
  .. image:: assets/1-9a.jpg

1.14
  .. image:: assets/1-14.jpg
  .. image:: assets/1-14a.jpg

1.21 (d, e, f)
  .. image:: assets/1-21.jpg
  .. image:: assets/1-21-2.jpg
  .. image:: assets/1-21a.jpg

1.22 (g, h)
  .. image:: assets/1-22.jpg
  .. image:: assets/1-22a.jpg

1.23 (c)
  .. image:: assets/1-23.jpg
  .. image:: assets/1-23-2.jpg
  .. image:: assets/1-23a.jpg

1.24 (b)
  .. image:: assets/1-24.jpg
  .. image:: assets/1-24-2.jpg
  .. image:: assets/1-24a.jpg

1.25
  .. image:: assets/1-25.jpg
  .. image:: assets/1-25a.jpg
  .. warning:: （f）周期性判断

1.26
  .. image:: assets/1-26.jpg
  .. image:: assets/1-26a.jpg

1.36
  .. image:: assets/1-36.jpg
  .. image:: assets/1-36a.jpg

  .. warning:: （b，c）

1.38
  .. image:: assets/1-38.jpg
  .. image:: assets/1-38-2.jpg
  .. image:: assets/1-38-3.jpg
  .. image:: assets/1-38-4.jpg
  .. image:: assets/1-38a.jpg
  .. image:: assets/1-38a-2.jpg

  for (a), an alternative solution:

  .. math::

    \begin{align}
    \int_{-\infty}^{\infty}\delta(2t)\mathrm{d}t &= 1 \\
    \int_{-\infty}^{\infty}\frac{1}{2}\delta(2t)\mathrm{d}(2t) &= 1 \\
    \int_{-\infty}^{\infty}\frac{1}{2}\delta(t)\mathrm{d}t &= \int_{-\infty}^{\infty}\delta(2t)\mathrm{d}t \\
    \frac{1}{2}\delta(t) &= \delta(2t)
    \end{align}

  .. note:: 如可能，应在示意图中标明解析式。注意（b）中（f）图，:math:`t < 0` 时积分结果为 :math:`\frac{1}{2}e^{t/\Delta}`，而不是 :math:`\frac{1}{2}e^{\textcolor{red}{-}t/\Delta}`。

1.42
  .. image:: assets/1-42.jpg
  .. image:: assets/1-42-2.jpg
  .. image:: assets/1-42a.jpg

  \(c\) Let us name the output of system 1 as :math:`w[n]` and the output of system 2 as :math:`z[n]`. Then,

  .. math::

    \begin{align}
    y[n] &= z[2n] = w[2n] + \frac{1}{2}w[2n-1] + \frac{1}{4}w[2n-2] \\
    &= x[n] + \frac{1}{4}x[n-1]
    \text{.}
    \end{align}

  The system is linear and time-invariant.

  or rewrite the relationship of system 1 as

  .. math::

    y[n] = \left[1+(-1)^n\right]\frac{x[\frac{n}{2}]}{2}
    \text{,}

  and continue connecting them in series.

  .. note:: （b）若 :math:`y_1(x)=x^2` 与 :math:`y_2(x)=\sqrt{x}` 级联，:math:`y(x)=|x|` 是非线性系统，不能作为反例。

  .. warning:: （c）

作图题
  #. 合理选择坐标范围：横坐标上，对周期信号，推荐显示至少两个周期，对衰减的信号，显示到其接近收敛；纵坐标上，图形主要部分不应被裁减
  #. 合理选择采样点数：就作图而言，为了得到平滑的图形，采样率等于或略大于两倍信号最高频率一般是不够的，推荐采样率在五倍信号最高频率以上

1.27 (b, c)
  .. image:: assets/1-27.jpg
  .. image:: assets/1-27-2.jpg
  .. image:: assets/1-27a.jpg

  .. note:: 无记忆系统的输出仅与当前输入有关；若输出依赖于未来的输入，系统亦是有记忆的。

1.28 (d, g)
  .. image:: assets/1-28.jpg
  .. image:: assets/1-28a.jpg
  .. image:: assets/1-28a-2.jpg

1.29 (a)
  .. image:: assets/1-29.jpg
  .. image:: assets/1-29a.jpg

  Let us now assume that the input-output relationship is changed to :math:`y[n] = \mathcal{Re}\{e^{j\pi n/4}x[n]\}`. Also, consider two inputs to the system such that

  .. math::

    x_1[n] \xrightarrow{S} y_1[n] = \mathcal{Re}\{e^{j\pi n/4}x_1[n]\}

  and

  .. math::

    x_2[n] \xrightarrow{S} y_2[n] = \mathcal{Re}\{e^{j\pi n/4}x_2[n]\}

  Now consider a third input :math:`x_3[n] = x_1[n] + x_2[n]`. The corresponding system output will be

  .. math::

    \begin{align}
      y_3[n] &= \mathcal{Re}\{e^{j\pi n/4}x_3[n]\} \\
      &= \cos(\pi n/4)\mathcal{Re}\{x_3[n]\} - \sin(\pi n/4)\mathcal{Im}\{x_3[n]\} \\
      &= \cos(\pi n/4)\mathcal{Re}\{x_1[n]\} + \cos(\pi n/4)\mathcal{Re}\{x_2[n]\} \\
      &\quad\; - \sin(\pi n/4)\mathcal{Im}\{x_1[n]\} - \sin(\pi n/4)\mathcal{Im}\{x_2[n]\} \\
      &= \mathcal{Re}\{e^{j\pi n/4}x_1[n]\} + \mathcal{Re}\{e^{j\pi n/4}x_2[n]\} \\
      &= y_1[n] + y_2[n]
    \end{align}

  Therefore, we may conclude that the system is additive.

1.31 (a)
  .. image:: assets/1-31.jpg
  .. image:: assets/1-31-2.jpg
  .. image:: assets/1-31-3.jpg
  .. image:: assets/1-31a.jpg

1.40
  .. image:: assets/1-40.jpg
  .. image:: assets/1-40a.jpg

1.44
  .. image:: assets/1-44.jpg
  .. image:: assets/1-44a.jpg
  .. image:: assets/1-44a-2.jpg

  .. note:: 证明两种表达方式等价，需要完成充要双向的推导。

1.45 (a, b)
  .. image:: assets/1-45.jpg
  .. image:: assets/1-45a.jpg
