<h1 align="center">
  <br>
  <br>
  <br>
  110-Borwein
  <br>
</h1>

&nbsp;

<h3 align="center">
    In 2001, the Borwein brothers studied the following integrals, which now bear their name:
</h3>

&nbsp;

$$ ∀n ∈ N, I_{n} = \int_{0}^{+∞} \prod_{k=0}^{n} {\frac {\sin( \frac {x} {2K+1} )} {\frac {x} {2K+1}}} dx $$

&nbsp;

<h3 align="center">
    These integrals are remarkable because the first ones are all equal to π/2.<br>
    An obvious conjecture would be that this is true for every value of n.<br>
    Some decades ago, an old-school mathemacian would have had to hand-calculate<br>
    the values of the first integrals (which would take several months, or even years),<br>
    the nassume all the integrals are equal to π, and finally try and demonstrate this conjecture.<br>
    <br>
    Today, we can use numerical calculus to evaluate as many of these integrals as possible before getting into a demonstration.<br>
    This is the goal of this project.<br>
    We'we had to compute Borwein integrals, using the midpoint rule, the trapezoidal rule and the Simpson’s rule,<br>
    and print both the value of In and the absolute difference between In and π.<br>
</h3>

&nbsp;

## 🏅 Results

| Cat | Percentages |
|:--:|:--:|
| Basic | 100% |
| cosine | 60% |
| sine | 60% |
| exponential | 60% |
| hyperbolic cosine | 60% |
| hyperbolic sine | 60% |
| Rigor | 100% |
| **Total** | **72.2%** |

&nbsp;

## ℹ️ Usage

```bash
./110borwein n
```

&nbsp;

## 📝 Description

```txt
n constant defining the integral to be computed
```
