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

   .. figure:: assets/2-3a-2.jpg

      **Figure S2.3**: :math:`y[n]`

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
      \label{eq.2}\tag{eq.2}\text{.}

   Using commutativity:

   .. math:: g^{(1)}(t) = f^{(1)}(t)*h(t)\tag{eq.3}

   Property 7 (integral property):

   .. math::

      g^{(-1)}(t) = f(t)*h^{(-1)}(t)
      \label{eq.4}\tag{eq.4}\text{.}

   Obviously:

   .. math::

      g^{(-1)}(t) = f^{(-1)}(t)*h(t)
      \label{eq.5}\tag{eq.5}\text{.}

   Consider this:

   .. math::

      \begin{align}
      g(t) &= \left[\int_{-\infty}^{t}f^{(1)}(\tau)\mathrm{d}\tau
      +f(-\infty)\right]*h(t) \\
      &= \left[f^{(1)}(t)\right]^{(-1)}*h(t)\text{,}
      \end{align}

   since :math:`f_1(-\infty)=f_2(-\infty)=0`. Using :math:`(\ref{eq.4})` and :math:`(\ref{eq.5})`, we get:

   .. math::

      g(t) = f^{(1)}(t)*h^{(-1)}(t)\label{eq.6}\tag{eq.6}

   Of course:

   .. math::

      g(t) = f^{(-1)}(t)*h^{(1)}(t)\label{eq.7}\tag{eq.7}

   First, we repeatedly use :math:`(\ref{eq.2})` or :math:`(\ref{eq.4})` to get
   :math:`f^{(i)}(t)=f_1(t)*f_2^{(i)}(t)`, and then we can prove :math:`f^{(i)}(t)=f_1^{(j)}(t)*f_2^{(i-j)}(t)` with :math:`(\ref{eq.6})` and :math:`(\ref{eq.7})`.

2.28（a，c）
   .. image:: assets/2-28.jpg
   .. image:: assets/2-28a.jpg

2.39（a）
   .. image:: assets/2-39.jpg
   .. image:: assets/2-39a.jpg
   .. image:: assets/2-39a-2.jpg

   .. .. mermaid::

   ..    graph LR
   ..       A --- B

.. raw:: html

   <div class="mermaid">
      graph LR
         A --- B
         B-->C[fa:fa-ban forbidden]
         B-->D(fa:fa-spinner)
   </div>

2.40
   .. image:: assets/2-40.jpg
   .. image:: assets/2-40a.jpg
   .. image:: assets/2-40a-2.jpg
   .. image:: assets/2-40a-3.jpg

2.53（c-i）
   .. image:: assets/2-53.jpg
   .. image:: assets/2-53a.jpg

2.54（c-i）
   .. image:: assets/2-54.jpg
   .. image:: assets/2-54a.jpg
