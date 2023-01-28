# Matrix of Linear Transformation

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLZt5lIVW7jQSQ4bY1loXYbdiHsx5eulgI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As we have seen that any finite-dimensional vector space $V$ with an ordered basis is isomorphic to $\newcommand{R}{\mathbb{R}}\R^n$. Now suppose we have two vector spaces $V$ and $W$ over the same field $\R$, and a linear transformation $T$ between them. If we fix a basis $\alpha$ for $V$ and $\beta$ for $W$, then we have following situation

<figure markdown>
<script type="text/tikz">
    \begin{tikzpicture}[node distance=4cm, auto]
        \node (V) {$(V, \alpha)$};
        \node (W) [right of=V] {$(W, \beta)$};
        \node (R) [below of=V] {$R^m$};
        \node (M) [below of=W] {$R^n$};
        \draw[-stealth] (V) to node {$T$} (W);
        \draw[-stealth] (V)-- node [left] {\small $\rho_\alpha$} (R);
        \draw[-stealth] (W)-- node [right] {\small $\rho_\beta$} (M);
        \draw[-stealth] (R)-- node [below] {\small $f$} (M);
    \end{tikzpicture}
</script>
</figure>

where the function $f$ is given by the compositions of these functions as follows 
\begin{align*}
    f=\rho_\beta\circ T\circ \rho_{\alpha}^{-1}
\end{align*}
So, for any linear transformation $T: V\to W$, we can find a unique linear transformation $f:\R^n\to \R^n$. 

One important property of the vector spaces like $\R^n$ is that any linear transformation between such space is given by a matrix as the following theorem

**Theorem:** For any field $F$, any linear transformation $T:F^n \to F^m$ is given by a matrix, $A$, of size $m\times n$, such that, $T(\mathbf{x}) = A\mathbf{x}$. 

##**Matrix of a Linear Transformation**

**Definition:** Let $V$ and $W$ be two vector spaces over a field $F$ with ordered basis $\alpha$ and $\beta$ respectively. Suppose $T: V\to W$ is a linear transformation, then the matrix associated with the linear transformation $f$ is called **the matrix of $T$ with respect to $\alpha$ and $\beta$**, and it is denoted by $\left[\, T \,\right ]_{\alpha}^{\beta}$.

The following theorem provides a method to calculate the matrix of a linear transformation with given bases.

**Theorem:** Let $T: V\to W$ be a linear transformation from a vector space $v$ to $w$ over field $F.$ Let $\alpha=(v_1, \dots, v_n)$ and $\beta=(w_1,\dots,w_n)$ be the ordered basis of $V$ and $W$ respectively. Then the matrix=
of linear transformation $T$ w.r.to $\alpha$ and $\beta$ is given by.

$$[\,T\,]^{\beta}_{\alpha}=\begin{bmatrix}
    \vdots     &\vdots& &\vdots   \\
    [\,T(v_1)\,]_{\beta} & [\,T(v_2)\,]_{\beta} & \cdots & [\,T(v_n)\,]_{\beta} \\
    \vdots     &\vdots& &\vdots 
    \end{bmatrix}_{m \times n}$$

**Proof** For any $v\in V$, we have  

\begin{align*}
    v&=x_1v_1+\dots+x_nv_n, \quad x_{i}\in F\\
\end{align*}

Now applying $T$ on both sides, we get

\begin{align*}
    T(v)&=T(x_{1}v_{1}+\dots+x_nv_n)\\
    T(v)&=x_1T(v_1)+\dots+x_{n}T(v_n)\\
\end{align*}

Since, $T(v_i)\in W$, we can find scalar $a_{ij}$, such that,

\begin{align*}
    T(v_1)&=a_{11}w_1+a_{22}w_2+\dots+a_{m1}w_n\\
    &\vdots \\
    T(v_n)&=a_{1n}w_1+a_{2n}w_n+\dots+a_{mn} w_{m}
\end{align*}

Now assume, 

\begin{align*}
    (a_{11},\dots, a_{m1})&=[T(v_1)]_{\beta}\\
    (a_{22},\dots, a_{m2})&=[T(v_2)]_{\beta}\\
    &\vdots \\
    (a_{m1},\dots, a_{mn})&=[T(v_n)]_{\beta}
\end{align*}

\begin{align*}
    T(v)&=\sum_{i=1}^{n} X_{i}T(v_{i})\\
    T(v_i)&=\sum_{v=1}^{n}a_{ji}w_{i}
\end{align*}

\begin{align*}
    T(V)=\sum_{i=1}^{n}X_{i}T(V_{i})&=\sum_{i=1}^{n}x_i\left(\sum_{j=1}^{n}a_{ji}w_{j}\right)\\
    &=\sum_{i=1}^{n}\sum_{j=1}^{m} x_i a_{ji}w_{j}\\
    &=\sum_{j=1}^{m}\left(\sum_{i=1}^{n}x_{i}a_{ji}\right)w_{j}\\
     &=\sum_{j=1}^{m}\left(\sum_{i=1}^{n}a_{ji}x_{i}\right)w_{j}
\end{align*}

\begin{align*}
\left[T(v)\right]_{\beta}&=\left(\sum_{i=1}^{n}a_{1i} X_{i}, \sum_{i=1}^{n}a_{2j}X_i, \dots, \sum_{i=1}^{n}a_{mi}X_{i}\right)\\
\left[T(v)\right]_{\beta}&=\left[\begin{array}{ccccc}
 \sum_{i=1}^{n}a_{1i} X_{i}    &=a_{11}X_1&+a_{12}X_2&+\dots&+a_{1n}X_{n}  \\
    \sum_{i=1}^{n}a_{2i} X_{i}    &=a_{21}X_1&+a_{22}X_2&+\dots&+a_{2n}X_{n}  \\
    \vdots & \vdots &\vdots & \vdots\\
    \sum_{i=1}^{n}a_{1i} X_{i}    &=a_{11}X_1&+a_{12}X_2&+\dots&+a_{1n}X_{n}  \\
\end{array}\right]\\
&=\left[\begin{array}{cccc}
     a_11&\dots&a_{1n}  \\
     a_21& \dots& a_{2n}\\ 
     \vdots &\ddots & \vdots \\
     a_{m1}&\dots & a_{mn}
\end{array}\right]\left[\begin{array}{c}
     X_1 \\
     X_2\\
     \vdots\\
     X_{n}
\end{array}\right]\\
&=\big [\left[T(v_1)_{\beta}\right] \dots \left[T(v_{n})_{\beta}\right] \big ]\left[V\right]_{\alpha}
\end{align*}

After watching this you can try question 1 from [assignment 1](PDFs/201820A1.pdf).