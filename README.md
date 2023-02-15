# Primitive abundant numbers
An abundant number (AN) is a positive integer $N$ such that $\tau(N) > 2N$ where $\tau$ is defined as $$\tau(N) := \sum_{d \mid N} d.$$ A deficient number is a positive integer $N$ such that $\tau(N) < 2N$. A primitive abundant number (PAN) is an AN, the proper divisors of which are deficient.
 
 In this repository, we search for and implement algorithms for finding PANs up to some number X.

 ## 1. Sifting abundant numbers
 **Fact:** All multiples of PANs are abundant.

 We keep two copies $P$ and $A$ of the set ${0, 1, \dots, X}$ and a $(X + 1) \times \log_2 X$ matrix $B$. We sift $P$ using the sieve of Eratosthenes. Then we sift the PANs up to $X$ as follows:
 1. Pick the next prime $p \in P$.
 2. For every $n \in A$ divisible by $p$, write $A[n] = A[n]/p^e$ where $p^e \mid\mid n$, and add $p$ to the row $B[n]$.
 3. If $A[n] = 1$ for some $n \in A$, then compute $\tau(n)$ using the formula $$\tau(p_1^{e_1} \cdots p_k^{e_k}) = \frac{p_1^{e_1+1} - 1}{p_1 - 1} \cdots \frac{p_k^{e_k+1} - 1}{p_k - 1},$$ and decide whether $n$ is an abundant number.
 4. Sift out all multiples $d \cdot n \in A$.
 4'. Sift out all multiples $d \cdot n \in A$ if $n$ is a perfect number.
   
 **Remark:** if $n$ turns out to be an abundant number at Step 3, then it is actually a primitive abundant number because if there is any proper divisor of $n$ that is an AN, then one of them is a PAN, so $n$ would already be sifted out from $A$ at a previous Step 4.


