# Python 數學運算說明（國中＋高中）

本文件以 Python 實作國中與高中的數學範例，涵蓋代數、幾何、三角函數、數列與機率統計等主題。使用 uv 虛擬環境執行，可直接複製程式碼到 Jupyter Notebook 或 Python 腳本中執行。

---

## 目錄

- [基本運算與常用函式](#一基本運算與常用函式)
- [國中數學範例](#二國中數學範例)
  - [1. 質數判斷與因數分解](#1-質數判斷與因數分解)
  - [2. 最大公因數（GCD）與最小公倍數（LCM）](#2-最大公因數gcd與最小公倍數lcm)
  - [3. 二元一次方程式](#3-二元一次方程式)
  - [4. 一元二次方程式](#4-一元二次方程式)
  - [5. 畢氏定理](#5-畢氏定理)
  - [6. 幾何面積與體積](#6-幾何面積與體積)
  - [7. 一次函數與直線斜率](#7-一次函數與直線斜率)
  - [8. 分數與百分比](#8-分數與百分比)
- [高中數學範例](#三高中數學範例)
  - [1. 三角函數](#1-三角函數)
  - [2. 指數與對數](#2-指數與對數)
  - [3. 數列與級數（等差、等比）](#3-數列與級數等差等比)
  - [4. 排列組合](#4-排列組合)
  - [5. 機率](#5-機率)
  - [6. 統計：平均數、標準差、迴歸](#6-統計平均數標準差迴歸)
  - [7. 微積分入門（極限與導數）](#7-微積分入門極限與導數)
  - [8. 矩陣與行列式](#8-矩陣與行列式)
- [附錄：常用套件](#附錄常用套件)

---

## 一、基本運算與常用函式

Python 內建 `math` 模組提供豐富的數學函式。

```python
import math

# 基本運算子
print(7 + 3)     # 加法 → 10
print(7 - 3)     # 減法 → 4
print(7 * 3)     # 乘法 → 21
print(7 / 3)     # 除法（浮點數）→ 2.333...
print(7 // 3)    # 整數除法（商）→ 2
print(7 % 3)     # 取餘數 → 1
print(7 ** 3)    # 次方 → 343

# math 常用函式
print(math.sqrt(16))    # 平方根 → 4.0
print(math.pow(2, 10))  # 2 的 10 次方 → 1024.0
print(math.pi)          # 圓周率
print(math.fabs(-5))    # 絕對值 → 5.0
print(math.floor(3.7))  # 無條件捨去 → 3
print(math.ceil(3.2))   # 無條件進位 → 4
print(round(3.14159, 2))  # 四捨五入到小數第 2 位 → 3.14
```

---

## 二、國中數學範例

### 1. 質數判斷與因數分解

```python
def is_prime(n):
    """判斷 n 是否為質數"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """質因數分解，回傳 {質因數: 次方}"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

print(is_prime(97))            # True
print(is_prime(100))           # False
print(prime_factors(360))      # {2: 3, 3: 2, 5: 1} → 2³×3²×5
```

### 2. 最大公因數（GCD）與最小公倍數（LCM）

```python
import math

a, b = 84, 36
gcd = math.gcd(a, b)          # 最大公因數 → 12
lcm = a * b // gcd            # 最小公倍數 → 252
print(gcd, lcm)

# 不使用內建函式的輾轉相除法
def gcd_manual(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd_manual(84, 36))     # 12
```

### 3. 二元一次方程式

解聯立方程式：
```
 2x + 3y = 13
 5x -  y =  7
```

```python
# 使用克拉瑪公式（Cramer's rule）
a1, b1, c1 = 2, 3, 13
a2, b2, c2 = 5, -1, 7

det = a1 * b2 - a2 * b1       # 主行列式
det_x = c1 * b2 - c2 * b1
det_y = a1 * c2 - a2 * c1

if det == 0:
    print("無唯一解")
else:
    x = det_x / det
    y = det_y / det
    print(f"x = {x}, y = {y}")   # x = 2.0, y = 3.0
```

### 4. 一元二次方程式

解 `ax² + bx + c = 0`，使用公式解。

```python
import math

def solve_quadratic(a, b, c):
    """回傳一元二次方程式的根"""
    D = b ** 2 - 4 * a * c      # 判別式
    if D < 0:
        return None             # 無實數解
    if D == 0:
        return (-b / (2 * a),)  # 重根
    sqrt_D = math.sqrt(D)
    return ((-b + sqrt_D) / (2 * a),
            (-b - sqrt_D) / (2 * a))

# x² - 5x + 6 = 0 → 根為 2, 3
print(solve_quadratic(1, -5, 6))    # (3.0, 2.0)
```

**驗證：** 兩根之和 `= -b/a = 5`，兩根之積 `= c/a = 6`。

### 5. 畢氏定理

直角三角形兩股為 a、b，斜邊為 c，則 `a² + b² = c²`。

```python
import math

a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)
print(f"斜邊 = {c}")    # 5.0

# 判斷是否為直角三角形
def is_right_triangle(sides):
    sides = sorted(sides)
    return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

print(is_right_triangle([6, 8, 10]))   # True
print(is_right_triangle([2, 3, 4]))    # False
```

### 6. 幾何面積與體積

```python
import math

# 圓
r = 5
circle_area = math.pi * r ** 2          # 圓面積
circle_circumference = 2 * math.pi * r  # 圓周長
print(circle_area, circle_circumference)

# 三角形（海龍公式）
def triangle_area(a, b, c):
    s = (a + b + c) / 2                 # 半周長
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(triangle_area(3, 4, 5))           # 6.0

# 圓柱體積
r, h = 3, 10
cylinder_volume = math.pi * r ** 2 * h
print(cylinder_volume)

# 球體積
sphere_volume = 4 / 3 * math.pi * r ** 3
print(sphere_volume)

# 扇形面積
def sector_area(r, degrees):
    return math.pi * r ** 2 * (degrees / 360)

print(sector_area(6, 90))               # 90° 扇形，半徑 6
```

### 7. 一次函數與直線斜率

直線 `y = mx + b`，斜率 `m = (y₂ − y₁) / (x₂ − x₁)`。

```python
def slope(p1, p2):
    """計算兩點連線的斜率"""
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return None                     # 鉛直線斜率不存在
    return (y2 - y1) / (x2 - x1)

print(slope((1, 2), (3, 6)))            # 2.0

# 由兩點求直線方程式
def line_from_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = slope(p1, p2)
    if m is None:
        return f"x = {x1}"
    b = y1 - m * x1
    return f"y = {m:.2f}x + {b:.2f}"

print(line_from_points((1, 2), (3, 6)))  # y = 2.00x + 0.00
```

### 8. 分數與百分比

```python
from fractions import Fraction
import math

# 分數運算
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f1 + f2)      # 1/2
print(f1 * f2)      # 1/18
print(f1 / f2)      # 2
print(f1 - f2)      # 1/6

# 百分比
score, total = 42, 60
percentage = score / total * 100
print(f"得分率 = {percentage:.1f}%")     # 70.0%

# 打折
price = 500
discounted = price * 0.8
print(f"打八折 = {discounted}")          # 400.0
```

---

## 三、高中數學範例

### 1. 三角函數

```python
import math

# 度與徑度轉換
deg = 60
rad = math.radians(deg)            # → 1.047
print(math.sin(rad))               # 0.8660
print(math.cos(rad))               # 0.5
print(math.tan(rad))               # 1.732

# 反三角函數
print(math.degrees(math.asin(0.5)))    # 30.0
print(math.degrees(math.acos(0.5)))    # 60.0

# 正弦定理：a/sinA = b/sinB = c/sinC
# 已知角 A=30°, 對邊 a=5，求對邊 b（角 B=60°）
A, B, a = math.radians(30), math.radians(60), 5
b = a * math.sin(B) / math.sin(A)
print(f"b = {b}")                        # 8.660...

# 和角公式驗證：sin(α+β)
alpha, beta = math.radians(30), math.radians(45)
lhs = math.sin(alpha + beta)
rhs = (math.sin(alpha) * math.cos(beta) +
       math.cos(alpha) * math.sin(beta))
print(math.isclose(lhs, rhs))            # True

# 三角恆等式：sin²θ + cos²θ = 1
theta = math.radians(37)
print(math.isclose(math.sin(theta) ** 2 + math.cos(theta) ** 2, 1))  # True
```

### 2. 指數與對數

```python
import math

# 指數律
a, b = 2, 3
print(2 ** 3)                 # 8
print(2 ** 3 * 2 ** 4)        # 128（相加：a^m × a^n = a^(m+n)）
print((2 ** 3) ** 2)          # 64（a^m)^n = a^(mn)

# 對數：log_b(x) = y  ⟺  b^y = x
print(math.log(8, 2))         # log₂8 = 3.0
print(math.log(1000, 10))     # log₁₀1000 = 3.0
print(math.log(math.e))       # ln(e) = 1.0（自然對數）

# 對數律驗證：log(xy) = log(x) + log(y)
x, y = 8, 4
lhs = math.log(x * y, 2)
rhs = math.log(x, 2) + math.log(y, 2)
print(math.isclose(lhs, rhs))    # True

# 應用：指數成長
# 細菌每小時翻倍，初始 100 隻，求 10 小時後數量
N0, t = 100, 10
print(N0 * (2 ** t))              # 102400

# 應用：半衰期
# 碳-14 半衰期 5730 年，求衰變公式 N(t) = N0 × (1/2)^(t/5730)
half_life = 5730
remaining = 0.5 ** (5730 / half_life)
print(remaining)                  # 0.5（正好一個半衰期）
```

### 3. 數列與級數（等差、等比）

```python
# 等差數列：aₙ = a₁ + (n-1)d
def arithmetic_nth(a1, d, n):
    return a1 + (n - 1) * d

def arithmetic_sum(a1, d, n):
    """等差級數前 n 項和：Sₙ = n/2 × (a₁ + aₙ)"""
    an = arithmetic_nth(a1, d, n)
    return n * (a1 + an) // 2

print(arithmetic_nth(3, 4, 10))     # 39
print(arithmetic_sum(3, 4, 10))     # 210

# 等比數列：aₙ = a₁ × r^(n-1)
def geometric_nth(a1, r, n):
    return a1 * (r ** (n - 1))

def geometric_sum(a1, r, n):
    """等比級數前 n 項和"""
    if r == 1:
        return a1 * n
    return a1 * (1 - r ** n) / (1 - r)

print(geometric_nth(2, 3, 5))       # 162
print(geometric_sum(2, 3, 5))       # 242.0

# 無窮等比級數（|r| < 1）：S = a₁ / (1 - r)
a1, r = 1, 1 / 2
print(a1 / (1 - r))                 # 2.0

# 費氏數列（遞迴）
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]
```

### 4. 排列組合

```python
import math
from itertools import permutations, combinations

# 階乘 n!
print(math.factorial(5))            # 120

# 排列 P(n, k) = n! / (n-k)!
def P(n, k):
    return math.factorial(n) // math.factorial(n - k)

# 組合 C(n, k) = n! / (k!(n-k)!)
def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(P(5, 2))                      # 20
print(C(5, 2))                      # 10

# 驗證：3 人排成一列的方法數
items = list(permutations([1, 2, 3]))
print(len(items))                   # 6 = 3!

# 驗證：從 5 人選 2 人委員會
combs = list(combinations([1, 2, 3, 4, 5], 2))
print(len(combs))                   # 10

# 實際應用：C(6, 2) 樂透選 6 中選 2
print(C(6, 2))                      # 15
```

### 5. 機率

```python
import random
from itertools import product

# 1. 古典機率：擲兩顆骰子，點數和為 7 的機率
outcomes = list(product(range(1, 7), repeat=2))
favorable = [o for o in outcomes if sum(o) == 7]
print(len(favorable), "/", len(outcomes))       # 6 / 36 = 1/6

# 2. 蒙地卡羅模擬驗證（隨機抽樣 100000 次）
random.seed(42)
N = 100_000
count = sum(1 for _ in range(N)
            if random.randint(1, 6) + random.randint(1, 6) == 7)
print(f"模擬機率 ≈ {count / N:.4f}")            # 約 0.1667

# 3. 條件機率：P(B|A) = P(A∩B) / P(A)
# 例：袋子有 3 紅球、2 藍球，先抽紅球(不放回)再抽紅球的機率
# P(兩球皆紅) = 3/5 × 2/4 = 3/10
p = (3 / 5) * (2 / 4)
print(f"兩球皆紅機率 = {p}")                     # 0.3

# 4. 期望值：擲骰子點數期望值 E = Σ x·P(x)
expectation = sum(x * (1 / 6) for x in range(1, 7))
print(f"骰子期望值 = {expectation}")             # 3.5
```

### 6. 統計：平均數、標準差、迴歸

```python
import statistics
import math

data = [78, 85, 92, 88, 90, 65, 72, 88, 95, 84]

mean = statistics.mean(data)                    # 平均數
median = statistics.median(data)                # 中位數
mode = statistics.mode(data)                    # 眾數
variance = statistics.variance(data)            # 母體變異數(樣本)
std = statistics.stdev(data)                    # 樣本標準差

print(mean, median, mode)                       # 83.7, 86.5, 88
print(f"標準差 = {std:.2f}")

# 標準化（z 分數）
z_scores = [(x - mean) / std for x in data]
print(z_scores[:3])

# 簡單線性迴歸（最小平方法）
# y = ax + b，其中 a = Sxy / Sxx
def linear_regression(xs, ys):
    n = len(xs)
    mx, my = statistics.mean(xs), statistics.mean(ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    a = sxy / sxx
    b = my - a * mx
    return a, b

# 已知 x 與 y 近乎線性關係
xs = [1, 2, 3, 4, 5]
ys = [2.1, 3.9, 6.1, 8.0, 9.9]
a, b = linear_regression(xs, ys)
print(f"迴歸線 y = {a:.2f}x + {b:.2f}")          # y ≈ 2.0x + 0.1

# 相關係數 r
def correlation(xs, ys):
    sx, sy = statistics.stdev(xs), statistics.stdev(ys)
    mx, my = statistics.mean(xs), statistics.mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / ((len(xs) - 1) * sx * sy)

print(f"相關係數 r = {correlation(xs, ys):.4f}")  # 非常接近 1，強正相關
```

### 7. 微積分入門（極限與導數）

```python
import math

# 導數的定義：f'(x) = lim(h→0) [f(x+h) - f(x)] / h
def derivative(f, x, h=1e-7):
    return (f(x + h) - f(x)) / h

# f(x) = x² → f'(x) = 2x
f = lambda x: x ** 2
print(derivative(f, 3))                 # ≈ 6.0

# f(x) = sin(x) → f'(x) = cos(x)
g = lambda x: math.sin(x)
print(derivative(g, math.pi / 4))       # ≈ cos(π/4) = 0.7071

# 多項式求導：xⁿ 的導數 = n·xⁿ⁻¹
def poly_derivative(coeffs):
    """coeffs 由高次到常數，例如 x³+2x²+3 → [1,2,0,3]"""
    return [coeffs[i] * (len(coeffs) - 1 - i)
            for i in range(len(coeffs) - 1)]

print(poly_derivative([1, 2, 0, 3]))    # [3, 4, 0] → 3x² + 4x

# 數值積分（梯形法則）近似 ∫₀¹ x² dx = 1/3
def trapezoid(f, a, b, n=1000):
    h = (b - a) / n
    return (h / 2) * (f(a) + f(b) +
            2 * sum(f(a + i * h) for i in range(1, n)))

print(trapezoid(lambda x: x ** 2, 0, 1))    # ≈ 0.333333
```

### 8. 矩陣與行列式

```python
# 使用內建 list 實作矩陣運算（不依賴 numpy）
def matrix_multiply(A, B):
    """矩陣乘法：A(m×n) × B(n×p) = C(m×p)"""
    m, n = len(A), len(A[0])
    p = len(B[0])
    if len(B) != n:
        raise ValueError("維度不符")
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(p)] for i in range(m)]

def determinant_2x2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]

def determinant_3x3(M):
    """行列式展開（薩呂法則）"""
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
          - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
          + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matrix_multiply(A, B))            # [[19, 22], [43, 50]]
print(determinant_2x2(A))               # 1×4 - 2×3 = -2

C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(determinant_3x3(C))               # 0（奇異矩陣）

# 用克拉瑪公式解 3 元一次聯立方程式
#   x + y + z = 6
#   x - y + z = 2
#   x + y - z = 0
import math  # 已於上方匯入

D = [[1, 1, 1], [1, -1, 1], [1, 1, -1]]
Dx = [[6, 1, 1], [2, -1, 1], [0, 1, -1]]
Dy = [[1, 6, 1], [1, 2, 1], [1, 0, -1]]
Dz = [[1, 1, 6], [1, -1, 2], [1, 1, 0]]

detD = determinant_3x3(D)
print(detD)                             # 4 ≠ 0，有唯一解
x = determinant_3x3(Dx) / detD
y = determinant_3x3(Dy) / detD
z = determinant_3x3(Dz) / detD
print(f"x = {x}, y = {y}, z = {z}")     # x=1, y=2, z=3
```

> 若需要更高效的矩陣運算，建議安裝 `numpy`：
> ```bash
> uv add numpy
> ```

---

## 附錄：常用套件

| 套件 | 用途 | 安裝指令 |
|------|------|----------|
| `math` | 內建數學函式（三角、對數、次方） | 內建，無需安裝 |
| `fractions` | 精確分數運算 | 內建，無需安裝 |
| `statistics` | 統計（平均數、標準差等） | 內建，無需安裝 |
| `random` | 隨機數與蒙地卡羅模擬 | 內建，無需安裝 |
| `sympy` | 符號運算（解方程式、微積分） | `uv add sympy` |
| `numpy` | 陣列與矩陣運算 | `uv add numpy` |
| `matplotlib` | 繪製函數圖形 | `uv add matplotlib` |

### SymPy 快速示範（符號運算）

```python
import sympy as sp

x, y = sp.symbols('x y')

# 解方程式
print(sp.solve(x ** 2 - 5 * x + 6, x))          # [2, 3]
print(sp.solve([x + y - 5, x - y - 1], [x, y])) # {x: 3, y: 2}

# 微分與積分
print(sp.diff(x ** 3 + 2 * x, x))               # 3x² + 2
print(sp.integrate(x ** 2, x))                  # x³/3

# 化簡
print(sp.simplify(sp.sin(x) ** 2 + sp.cos(x) ** 2))  # 1
```

---

## 執行方式

使用 uv 虛擬環境執行：

```bash
# 進入虛擬環境
source .venv/bin/activate

# 執行程式碼（複製上方程式碼存成 demo.py）
uv run python demo.py

# 或在 Jupyter Notebook 中逐格執行
uv run jupyter lab
```

祝你學習愉快！
