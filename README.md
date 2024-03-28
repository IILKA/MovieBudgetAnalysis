$$
F(t) = \frac{\Sigma_{i = 1}^{t} A[i]}{\Sigma_{i = 1}^{n} A[i]},  \text{where} A[i] \text{is the }ith \ \text{data point in the dataset A pf size n}
$$

$$
\text{define a random variable Profitable representing the probability of a profitable trade and } \\ \bold{Profitable} ~ \sim ~ Bernoulli(p) \text{, where p = 0.7992 as estimated in section 3.2.3a}\\
\text{then define a random variable} \ \bold{B} \  \text{representing the amount of budget, with currently unknown distribution}
$$


Consider following probability relations: 
$$
\begin{aligned}
 &Pr(Profitable | B \leq t) \\
= &\frac{Pr(Profitable \land B \leq t)}{Pr(B \leq t)} \\
= &\frac{Pr(B \leq t | Profitable)\cdot Pr(Profitable)}{Pr(B \leq t)}\\
&\text{where } Pr(Profitable) = p = 0.7992, \text{and } Pr(B \leq t), Pr(B\leq t|Profitable)\text{ can be obtained} \\ &\text{by discrete cdf calculation described above}
\end{aligned}
$$

consider the differentiations of the $Pr(Profitable | B \leq t)$
$$
\begin{aligned}
&\frac{d}{dt}Pr(Profitable | B \leq t) \\
= &\frac{d}{dt}\frac{Pr(Profitable \land B \leq t)}{Pr(B \leq t)}\\
= &\ \frac{Pr(Profitable \land B=t)\cdot Pr(B\leq t)- Pr(Profitable \land B \leq t )\cdot \frac{d}{dt}Pr(B\leq t)}{Pr^2(B \leq t)}
\end{aligned}
$$
Thus we can conclude 
$$
\begin{aligned}
&Pr(Profitable \land B = t)  \\
= & \frac{d}{dt}Pr(Profitable | B \leq t) \cdot Pr^2(B\leq t)  + Pr(Profitable \land B \leq t) \cdot \frac{d}{dt}Pr(B\leq t)
\end{aligned}
$$

The continous form of $Pr(Profitable|B\leq t)$ and $Pr(B\leq t)$ can be obtained by logarithmic regression. 
The regression result is shown in the following table and visualized in fig. 



