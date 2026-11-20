"""Independent exact local identity for eq:low-square-identity.

The floor summand is divided by w_i.  Consecutive reference ratios
are expressed through L_i, and all three rho values remain free.
"""
import sympy as s

lam, L, i, R, k, alpha_p, alpha_bar = s.symbols(
    "lambda L_i i R k alpha_p alpha_bar"
)
rho_prev, rho, rho_next = s.symbols("rho_prev rho rho_next")
c = lam - 1
r_prev = 1 / lam - L
r = 1 / (lam * (1 + L))
L_next = 1 / lam - r
weight_ratio = lam * r**2
Delta = rho - rho_next
Delta_prev = rho_prev - rho
C_alpha = alpha_p + lam * R
tau = 1 - C_alpha * r + (lam + 1) * R - R / r_prev

W0 = c * i / lam - 1 + 2 * i * L
Wp = c * W0 + 4 * i * L - 2 * r * (i * L + (i + 1) * lam * L_next)
W = W0 + R * Wp
B = (2 * i * (alpha_p + c * R) / lam
     + 2 * i * R * r * L + 2 * (i + 1) * R * lam * r**2 * L
     + k * (2 * i - 1) * tau)

# These are t_{i-1}/beta_i, J_{i-1}/(c beta_i), and gamma-bar/beta_i.
t = -R * rho_prev / r_prev + (1 + (lam + 1) * R) * rho - (alpha_bar + lam * R) * r * rho_next
J = (-2 * R * rho_prev / r_prev
     + (1 + 2 * alpha_bar + (3 * lam + 1) * R) * rho
     - (lam + 2 * alpha_bar + lam * (lam + 1) * R) * r * rho_next)
gamma = rho * (r - r_prev) - r * Delta + k * (1 - 1 / (2 * i)) * Delta
floor = i * ((rho - lam * r * rho_next) * J / lam + 2 * gamma * t)

# Local RHS before the diagonal terms are replaced by the V_i tails.
rhs = (W * rho**2 + Delta * rho * B
       + (alpha_bar - alpha_p) * Delta * (2 * i * rho / lam - k * (2 * i - 1) * r * rho_next)
       + k * (2 * i - 1) * (C_alpha * r * Delta**2 - R * Delta * Delta_prev / r_prev))

telescoping = (-(i - 1) * (1 + c * R) * rho**2
               + i * (1 + c * R) * weight_ratio * rho_next**2
               - 2 * i * R * L / r_prev * rho_prev * rho
               + 2 * (i + 1) * R * weight_ratio * L * rho * rho_next)

assert s.cancel(floor - rhs - telescoping) == 0
assert s.cancel(L_next / r - L) == 0
assert s.cancel(weight_ratio - 1 / (lam * (1 + L)**2)) == 0
print("Exact local floor residual and both telescope relations verified.")
