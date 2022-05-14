##############
第二章参考答案
##############

.. note::

  .. list-table:: 评分标准（总分 14）
    :header-rows: 1

    * - 评分
      - 所需分数
      - 对应分数
    * - :math:`\text{A}`
      - :math:`[12, 14]`
      - :math:`100`
    * - :math:`\text{B}`
      - :math:`[10, 12)`
      - :math:`85`
    * - :math:`\text{C}`
      - :math:`[8, 10)`
      - :math:`70`
    * - :math:`\text{D}`
      - :math:`[0, 8)`
      - :math:`0`

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

   .. note:: Do **NOT** forget to plot the output when you are expected to to exactly that.

   View the graph online: https://www.desmos.com/calculator/4sfkokoj2j

   .. figure:: assets/2-3a-2.jpg

      **Figure S2.3**: :math:`y[n]`

2.7
   .. image:: assets/2-7.jpg
   .. image:: assets/2-7-2.jpg
   .. image:: assets/2-7a.jpg
   .. image:: assets/2-7a-2.jpg

   Or :math:`y[n] = u[n] + u[n-2]`.

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

   .. warning::

      :math:`u_1(t)` is a unit doublet, not a unit step function:

      .. math::

         x(t) * u_1(t) = \frac{\mathrm{d}x(t)}{\mathrm{d}t}\text{.}

2.23
   .. image:: assets/2-23.jpg
   .. image:: assets/2-23-2.jpg
   .. image:: assets/2-23a.jpg
   .. image:: assets/2-23a-2.jpg

   .. note::

      Mark the axes smartly.

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

   .. warning::

      性质证明题

2.28（a，c）
   .. image:: assets/2-28.jpg
   .. image:: assets/2-28a.jpg

   .. warning::

         A system is stable if and only if every bounded input
         yields a bounded output.

      Remember the impulse response stability criteria correctly:

         If the system is LTI and can be described by an impulse
         response :math:`h[n]`, the above definition is equivalent to\ [1]_:

         .. math::

            \sum_{n=-\infty}^{\infty}|h[n]|<\infty\text{.}

         .. [1] https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1444705

   .. warning::

      Causal vs. noncausal vs. anticausal systems\ [2]_\ [3]_:

      - Causal or non-anticipative system: the output at any time depends only
        on the past and current inputs:

        .. math::

           \forall n < 0, h[n] = 0 \text{.}

      - Noncausal or acausal system: a system that has *some*
        dependence on input values from the future:

        .. math::

           \exists n_1 < 0, h[n_1] \neq 0 \text{.}

      - Anticausal system: a system that does not depend
        on past input values:

        .. math::

           \forall n > 0, h[n] = 0 \text{.}

      Obviously, anticausal systems are also noncausal.

      .. [2] The last paragraph of the textbook chapter 9.7.1
      .. [3] https://en.wikipedia.org/wiki/Causal_system

2.39（a）
   .. image:: assets/2-39.jpg
   .. image:: assets/2-39a.jpg
   .. image:: assets/2-39a-2.jpg

   An uglier illustration:

   .. raw:: html

      <div class="mermaid">
      flowchart LR
         X("x(t)")
         S("⊕")
         D("D")
         Y("y(t)")
         X -->|4| S --> Y
         Y --> D -->|-1/2| S
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
