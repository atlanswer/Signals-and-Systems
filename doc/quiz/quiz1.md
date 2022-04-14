# 前四章小测

```{note}
总分 100 分
```

## 第一章

```{note}
25 分，三选二
```

1. 判断并简要解释下面的系统是否为线性系统：$y[n] = \mathcal{Re}\{x[n]\}$
   > 参考例题 1.19，练习 1.29
   >
   > In checking the linearity of a system, it is
   > important to remember that the system must
   > satisfy both the additivity and homogeneity
   > properties and that the signals, as well as
   > any scaling constants, are allowed to be complex.
   >
   > Consider two inputs to the system such that
   >
   > $$
   > x_1[n]\xrightarrow{S}y_1[n]=\mathrel{Re}\{x_1[n]\}
   > \quad\text{and}\quad x_2[n]\xrightarrow{S}y_2[n]
   > =\mathrel{Re}\{x_2[n]\}
   > \text{.}
   > $$
   >
   > Additivity:
   >
   > Now consider a third input $x_3[n]=x_1[n]+x_2[n]$.
   > The corresponding system output will be
   >
   > $$
   > \begin{aligned}
   > y_3[n] &= \mathrel{Re}\{x_3[n]\} \\
   > &= \mathrel{Re}\{x_1[n]+x_2[n]\} \\
   > &= \mathrel{Re}\{x_1[n]\}+\mathrel{Re}\{x_2[n]\} \\
   > &= y_1[n]+y_2[n]
   > \text{.}
   > \end{aligned}
   > $$
   >
   > Therefore, we may conclude that the system is additive.
   >
   > Homogeneity:
   >
   > Let
   >
   > $$
   > x_1[n] = r[n] + js[n]
   > $$
   >
   > be an arbitrary complex input with real and imaginary
   > parts $r[n]$ and $s[n]$, respectively, so that the
   > corresponding output is
   >
   > $$
   > y_1[n] = r[n]
   > \text{.}
   > $$
   >
   > Now, consider scaling $x_1[n]$ by a complex number,
   > for example, $a = j$; i.e., consider the input
   >
   > $$
   > \begin{aligned}
   > x_2[n] &= jx_1[n] = j(r[n] + js[n]) \\
   > &= -s[n] + jr[n]
   > \text{.}
   > \end{aligned} 
   > $$
   >
   > The output corresponding to $x_2[n]$ is
   >
   > $$
   > y_2[n] = \mathrel{Re}\{x_2[n]\} = -s[n]
   > \text{,}
   > $$
   >
   > which is not equal to the scaled version of
   > $y_1[n]$,
   >
   > $$
   > ay_1[n] = jr[n]
   > \text{.}
   > $$
   >
   > We conclude that the system violates the
   > homogeneity property and hence is not linear.
1. 将下面的式子写成实虚部之和的形式：$i^i$
1. 判断下面的系统是否是周期系统，如果是，写出基础周期：$e^{jM(2\pi/N)n}$

## 第二章

```{note}
25 分，三选二
```

1. 计算输入信号和系统冲激响应的卷积并画出结果图形：

$$
   x(t) = e^{2t}u(-t)\text{, }
   h(t) = u(t - 3)
$$

2. 在 initial rest 的前提下，求下面微分方程的解：

$$
   \frac{\mathrm{d}y(t)}{\mathrm{d}t} + 2y(t)
   = e^{3t}u(t)
$$

## 第三章

```{note}
25 分，二选一
```

1. 计算傅里叶级数：
   1. $x[n]$ 周期为 $N$，$
         x[n] = \begin{cases}
            1 &|n|\leq N_1 \\
            0 &|n| > N_1    
         \end{cases}
    $
1. 写出一个同时满足如下条件的一个信号 $x(t)$ 表达式：
   1. $x(t)$ 为实函数，奇对称
   1. $x(t)$ 是周期信号，周期为 $2$，傅里叶级数系数为 $a_k$
   1. $a_k = 0\text{, for }|k|>1$
   1. $\frac{1}{2}\int_{0}^{2}|x(t)|^2\mathrm{d}t = 1$

## 第四章

```{note}
25 分
```

考虑信号：$
x =
\begin{cases}
   0 &|t| > 1 \\
   (t + 1) / 2 &|t|\leq 1
\end{cases}
$

1. 求该信号的傅里叶变换 $\mathop{X}(j\omega)$
1. 取前一步 $\mathop{X}(j\omega)$ 的实部，证明它就是 $x(t)$ 偶部的傅里叶变换
1. 求 $x(t)$ 奇部的傅里叶变换
1. 求 $\mathrm{d}x(t)/\mathrm{d}t$ 的傅里叶变换
1. 求 $x(\omega)$ 的傅里叶变换
