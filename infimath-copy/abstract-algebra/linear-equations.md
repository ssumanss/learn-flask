# Gaussian Elimination

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLZt5lIVW7jQSmgk5b3FOOnT7kP4mDOs_N" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

The idea of Gaussian elimination is to convert a system of linear equation into an equivalent system using elementary operations, such that, new system is easy to solve.

In previous classes we have seen many method of solving system of linear equation. $i.e.,$

 1. Hit and Trial Method
 1. Substitution Method
 1. Elimination 
 1. Cramer's Rule

Gaussian elimination is a prominent method to solve any system of linear equation. 

##**Step 1:** Write out the **augmented matrix**

A system of linear equation is generally of the form

\begin{align}\newcommand{\x}{\bf{x}}\newcommand{\bb}{\bf{b}}
  A \x = \bb 
  \label{eq:linear}\quad\tag{1}
\end{align}

where $A \in M(n \times m)$ and $\newcommand{\R}{\mathbb{R}}\bb \in \R^n$ are given, and $\x=(x_1,\dots, x_m)^T$ is the vector of unknowns.  For example, the system

\begin{align*}
  x_2 + 2 \, x_3 - x_4 & = 1 \\
  x_1 + x_3 + x_4 & = 4 \\
  -x_1 + x_2 - x_4 & = 2 \\
  2 \, x_2 + 3 \, x_3 - x_4 & = 7
\end{align*}

can be written in the form \eqref{eq:linear} with

\begin{equation*}
  A = 
  \begin{pmatrix}
  0 & 1 & 2 & -1 \\
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 2 & 3 & -1
  \end{pmatrix} \,,
  \qquad \bb =
  \begin{pmatrix}
  1 \\ 4 \\ 2 \\ 7 
  \end{pmatrix} \,.
\end{equation*}

To simplify notation, we write $A$ and $\bb$ into a single
**augmented matrix**,

\begin{equation}
  \tilde{A} = \left(
  \begin{matrix}
  0 & 1 & 2 & -1 \\
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 2 & 3 & -1
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  1 \\ 4 \\ 2 \\ 7 
  \end{matrix}
  \right)\right. \,.
  \label{e.m}\tag{2}
\end{equation}

##**Step 2:** Bring $\tilde{A}$ into **reduced row echelon form**

The goal of this step is to bring the augmented matrix into
**reduced row echelon form**.  A matrix is in this form if

 * the first non-zero entry of each row is $1$, this element is
referred to as the \emph{pivot},
 * each pivot is the only non-zero entry in its column,
 * each row has at least as many leading zeros as the previous
r *
For example, the following matrix is in row echelon form, where $*$
could be any, possibly non-zero, number:

\begin{equation*}
  \begin{pmatrix}
  0 & 1 & * & 0 & * & * & 0 \\
  0 & 0 & 0 & 1 & * & * & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  \end{pmatrix}
\end{equation*}

Three types of **elementary row operations** are permitted in this
process, namely

 1. exchanging two rows of $\tilde{A}$,
 1. multiplying a row by a non-zero scalar,
 1. adding a multiple of one row to another row.

As an example, we row-reduce the augmented matrix \eqref{e.m}:

\begin{align*}
  & \left(
  \begin{matrix}
  0 & 1 & 2 & -1 \\
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 2 & 3 & -1
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  1 \\ 4 \\ 2 \\ 7 
  \end{matrix}
  \right)\right. 
  \xrightarrow{\text{reorder rows}}
  \left(
  \begin{matrix}
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 1 & 2 & -1 \\
  0 & 2 & 3 & -1
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  4 \\ 2 \\ 1 \\ 7 
  \end{matrix}
  \right)\right.
  \xrightarrow{\text{R1}+\text{R2}\to\text{R2}} \\
  & \left(
  \begin{matrix}
  1 & 0 & 1 & 1 \\
  0 & 1 & 1 & 0 \\
  0 & 1 & 2 & -1 \\
  0 & 2 & 3 & -1
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  4 \\ 6 \\ 1 \\ 7 
  \end{matrix}
  \right)\right.
  \xrightarrow{\substack{\text{R3}-\text{R2}\to\text{R3} \\
  \text{R4}-2\,\text{R2}\to\text{R4}}}
  \left(
  \begin{matrix}
  1 & 0 & 1 & 1 \\
  0 & 1 & 1 & 0 \\
  0 & 0 & 1 & -1 \\
  0 & 0 & 1 & -1
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  4 \\ 6 \\ -5 \\ -5
  \end{matrix}
  \right)\right.
  \xrightarrow{\text{R4}-\text{R3}\to\text{R4}} \\
  & \left(
  \begin{matrix}
  1 & 0 & 1 & 1 \\
  0 & 1 & 1 & 0 \\
  0 & 0 & 1 & -1 \\
  0 & 0 & 0 & 0
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  4 \\ 6 \\ -5 \\ 0
  \end{matrix}
  \right)\right.
  \xrightarrow{\substack{\text{R1}-\text{R3}\to\text{R1}\\
  \text{R2}-\text{R3}\to\text{R2}}}
  \left(
  \begin{matrix}
  1 & 0 & 0 & 2 \\
  0 & 1 & 0 & 1 \\
  0 & 0 & 1 & -1 \\
  0 & 0 & 0 & 0
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  9 \\ 11 \\ -5 \\ 0
  \end{matrix}
  \right)\right.
\end{align*}


##**Step 3:** Zero, one, or many solutions?

There are two fundamentally different situations:

 1. The matrix $A$ is **regular**.  In this case, the left-hand
block of $\tilde{A}$ has been reduced to the identity matrix.  There is
exactly one solution, independent of which vector $\bb$ you started out
with. 

 2. The matrix $A$ is **degenerate**.  In this case, the left-hand
block of the row-reduced augmented matrix has more columns than
non-zero rows.  Then, dependent on which vector $\bb$ you started out
with, there is either no solution at all (the system is
**inconsistent**), or an infinite number of solutions (the system
is **underdetermined**).

If the rightmost column of the row-reduced augmented matrix has a
nonzero entry in a row that is otherwise zero, the system is
inconsistent.

Otherwise, the general solution has the following structure.  It is
the sum of a **particular solution** of the **inhomogeneous
equation** $A\x=\bb$ and the **general solution** of the
**homogeneous equation** $A\x=0$.

##**Step 4:** Write out the solution


 - If the left-hand block of the row-reduced matrix is not square,
make it square by adding or removing rows of zeros.  This has to
be done in such a way that the leading $1$ in each row (the
\emph{pivot}) lies on the diagonal!
 - The rightmost column of the row-reduced augmented matrix is a
particular solution.
 -  To find a basis for the general solution of the homogeneous
system, proceed as follows:  Take every column of the row-reduced
augmented matrix that has a zero on the diagonal.  Replace that zero
by $-1$.  The set of these column vectors is the basis you need.

In the example above, a particular solution is $(9, 11, -5, 0)^T$ and
the general solution of the homogeneous equation is a one-dimensional
subspace with basis vector $(2,1,-1,-1)^T$.  Therefore, the general
solution to the inhomogeneous equation $A\x=\bb$ is the line

\begin{equation*}
  \x = 
  \begin{pmatrix}
    9 \\ 11 \\ -5 \\ 0
  \end{pmatrix}
  + \lambda
  \begin{pmatrix}
  2 \\ 1 \\ -1 \\ -1
  \end{pmatrix} \,.
\end{equation*}

Another example:  Assume that the row-reduced matrix is

\begin{equation*}
  \left(
  \begin{matrix}
  0 & 0 & 1 & -3 & 0 & 4\\
  0 & 0 & 0 & 0 & 1 & 6 
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  -3 \\ 7
  \end{matrix}
  \right)\right.\,.
\end{equation*}

Padding the matrix with the required rows of zeros gives

\begin{equation*}
  \left(
  \begin{matrix}
  0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & -3 & 0 & 4\\
  0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 1 & 6 \\
  0 & 0 & 0 & 0 & 0 & 0   
  \end{matrix}
  \right.\left|\left.
  \begin{matrix}
  0 \\ 0 \\ -3 \\ 0 \\ 7 \\ 0
  \end{matrix}
  \right)\right.\,,
\end{equation*}

and the general solution is

\begin{equation*}
  \x =
  \begin{pmatrix}
  0 \\ 0 \\ -3 \\ 0 \\ 7 \\ 0
  \end{pmatrix}
  + \lambda_1
  \begin{pmatrix}
  -1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0
  \end{pmatrix}
  + \lambda_2
  \begin{pmatrix}
  0 \\ -1 \\ 0 \\ 0 \\ 0 \\ 0 
  \end{pmatrix}
  + \lambda_3
  \begin{pmatrix}
  0 \\ 0 \\ -3 \\ -1 \\ 0 \\ 0 
  \end{pmatrix}
  + \lambda_4
  \begin{pmatrix}
  0 \\ 0 \\ 4 \\ 0 \\ 6 \\ -1
  \end{pmatrix}  \,.
\end{equation*}

##**Step 5:** Check your solution

By multiplying $A$ with the vectors representing the solution, you can
easily verify that the computation is correct.  In our example,

\begin{align*}
  A \begin{pmatrix}
    9 \\ 11 \\ -5 \\ 0
  \end{pmatrix}
  &=
  \begin{pmatrix}
  0 & 1 & 2 & -1 \\
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 2 & 3 & -1
  \end{pmatrix}
  \begin{pmatrix}
    9 \\ 11 \\ -5 \\ 0
  \end{pmatrix}
  = \begin{pmatrix}
  1 \\ 4 \\ 2 \\ 7 
  \end{pmatrix} =\bb \,, \\
  A \begin{pmatrix}
  2 \\ 1 \\ -1 \\ -1
  \end{pmatrix}
  &=
  \begin{pmatrix}
  0 & 1 & 2 & -1 \\
  1 & 0 & 1 & 1 \\
  -1 & 1 & 0 & -1 \\
  0 & 2 & 3 & -1
  \end{pmatrix}
  \begin{pmatrix}
  2 \\ 1 \\ -1 \\ -1
  \end{pmatrix}
  =
  \begin{pmatrix}
  0\\0\\0\\0
  \end{pmatrix} \,.  
\end{align*}



After watching this you can try question 1 from [assignment 1](PDFs/201820A1.pdf).
