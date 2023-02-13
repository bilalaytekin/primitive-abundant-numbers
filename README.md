# Primitive abundant numbers
 An abundant number (AN) is a positive integer $N$ such that $\tau(N) > 2 * N$ where $\tau$ is the Ramanujan tau function $tau(N) := \sum_{d \mid N} d$; whereas, a primitive abundant number (PAN) is an abundant number, the proper divisors of which are not abundant.
 
 In this repository, we search for and implement algorithms for finding PANs upto some number X.

 ## 1. Sifting abundant numbers
 **Fact:** All multiples of primitive abundant numbers are abundant.

 We keep two copies $P$ and $A$ of the set $\{0, 1, \dots, X\}$ and a $(X + 1) \times \log_2 X$ matrix $B$. We sift $P$ using the sieve of Eratosthenes. Then we sift the PANs upto $X$ as follows:
 1. Pick the next prime $p \in P$.
 2. For every $n \in A$ divisible by $p$, write $A[n] = A[n]/p$ and add $p$ to the row $B[n]$.
 3. If $A[n] = 1$ for some $n \in A$, then compute $\tau(n)$ using the formula
    \[ \tau(p_1^{e_1} \cdots p_k^{e_k}) = \frac{p_1^{e_1+1} - 1}{p_1 - 1} \cdots \frac{p_k^{e_k+1} - 1}{p_k - 1}, \]
 and decide whether $n$ is an abundant number.
 4. Sift out all multiples $d \cdot n \in A$.
   
Note that, if $n$ turns out to be an abundant number at Step 3, then it is actually a primitive abundant number because if there is any $n' \mid n,\, n' \neq n$, then $n$ would already be sifted out from $A$ at Step 4.


