<h1 align="center">
  <br>
  <br>
  <br>
  108-Trigo
  <br>
</h1>

&nbsp;

<h3 align="center">
    As you may know (or not), the exponential function can be written as the sum of a power series:
</h3>

&nbsp;

$$ e^x = \sum_{ n=0 }^∞ { x^n \over n! } = 1 + x + { x^2 \over 2! } + { x^3 \over 3! } + ... $$

&nbsp;

<h3 align="center">
    So does many other functions, such as trigonometric and hyperbolic functions.<br>
    These power series are extremely handy when it comes to fast approximations of all those functions.<br>
    But they can also be used to exponentiate (for instance) mathematical objects (as long as they can be elevated to integer powers).<br>
    One could for example compute the cosine of a function, the exponentiation of a graph,<br>
    the hyperbolic tangent of a rotation or the sine of a square matrix (which is what we've done here) ...<br>
    Given a matrix and the name of a function, your program must apply the latter to the former, and print the result.<br>
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
./108trigo fun a0 a1 a2 ...
```

&nbsp;

## 📝 Description

```txt
fun function to be applied, among at least “EXP”, “COS”, “SIN”, “COSH” and “SINH”
ai coeficients of the matrix
```
