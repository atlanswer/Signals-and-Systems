##############
第二章参考答案
##############

.. note::
   第二章答案施工中...

2.1（b）
   .. image:: assets/2-1.jpg
   .. image:: assets/2-1a.jpg

   .. math::

      \begin{align}
      y_2[n] &= x[n+2] * h[n] \\
      &= \sum_{k=-\infty}^{\infty}h[k]x[n+2-k] \\
      &= 2x[n+1]+2x[n+3] \\
      &= 2\delta[n+3]+4\delta[n+2]+2\delta[n+1]+2\delta[n]-2\delta[n-2]
      \end{align}

2.3
   .. image:: assets/2-3.jpg
   .. image:: assets/2-3a.jpg

   View the graph online: https://www.desmos.com/calculator/4sfkokoj2j

   .. image:: assets/2-3a-2.jpg

2.7
   .. image:: assets/2-7.jpg
   .. image:: assets/2-7-2.jpg
   .. image:: assets/2-7a.jpg
   .. image:: assets/2-7a-2.jpg

离散卷积计算
   请作图展示结果

2.10
   .. image:: assets/2-10.jpg
   .. image:: assets/2-10a.jpg

2.11
   .. image:: assets/2-11.jpg
   .. image:: assets/2-11a.jpg
   .. image:: assets/2-11a-2.jpg

2.20
   .. image:: assets/2-20.jpg
   .. image:: assets/2-20a.jpg
   .. image:: assets/2-20a-2.jpg

2.23
   .. image:: assets/2-23.jpg
   .. image:: assets/2-23-2.jpg
   .. image:: assets/2-23a.jpg
   .. image:: assets/2-23a-2.jpg

证明卷积性质
   To prove property 8, we need property 6 & 7.

   Assume that

   .. math:: g(t) = f(t)*h(t)\text{.}\tag{eq.1}

   Property 6 (differential property):

   .. math::

      g^{(1)}(t) = f(t)*h^{(1)}(t)
      \tag{eq.2}\text{.}

   Using commutativity:

   .. math:: g^{(1)}(t) = f^{(1)}(t)*h(t)\tag{eq.3}

   Property 7 (integral property):

   .. math::

      g^{(-1)}(t) = f(t)*h^{(-1)}(t)
      \tag{eq.4}\text{.}

   Obviously:

   .. math::

      g^{(-1)}(t) = f^{(-1)}(t)*h(t)
      \tag{eq.5}\text{.}

   
   
   .. math::

      \begin{align}
      g^{(1)}(t) &= \frac{\mathrm{d}}{\mathrm{d}t}
      \int_{-\infty}^{\infty}f(\tau)h(t-\tau)\mathrm{d}\tau \\
      &= \int_{-\infty}^{\infty}f(\tau)\left[\frac{\mathrm{d}}{\mathrm{d}t}
      h(t-\tau)\right]\mathrm{d}\tau \\
      &= f(t)*h^{(1)}(t)
      \tag{eq.2}\text{.}
      \end{align}



2.28（a，c）
   .. image:: assets/2-28.jpg
   .. image:: assets/2-28a.jpg

2.39（a）
   .. image:: assets/2-39.jpg
   .. image:: assets/2-39a.jpg
   .. image:: assets/2-39a-2.jpg

2.40
   .. image:: assets/2-40.jpg
   .. image:: assets/2-40a.jpg
   .. image:: assets/2-40a-2.jpg

2.53（c-i）
   .. image:: assets/2-53.jpg
   .. image:: assets/2-53a.jpg

2.54（c-i）
   .. image:: assets/2-54.jpg
   .. image:: assets/2-54a.jpg
