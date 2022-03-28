##############
第一章参考答案
##############

.. note:: 施工中...

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

1.26
  .. image:: assets/1-26.jpg
  .. image:: assets/1-26a.jpg

1.36
  .. image:: assets/1-36.jpg
  .. image:: assets/1-36a.jpg

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

1.27 (b, c)
  .. image:: assets/1-27.jpg
  .. image:: assets/1-27-2.jpg
  .. image:: assets/1-27a.jpg

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

  .. note:: 证明两种表达方式等价，需要完成双向的推导。

1.45 (a, b)
  .. image:: assets/1-45.jpg
  .. image:: assets/1-45a.jpg
