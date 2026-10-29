"""Modular certificates excluding Q divisible by (t^2-1)^2.

Requires SymPy. A unit Groebner basis at a prime greater than L+1
proves characteristic-zero exclusion, using finiteness of the canonical
polynomial-Wronskian family proved in the accompanying note.
An inconclusive calculation is not evidence of a complex solution.
"""

import argparse
import time

import sympy as sp


def equations(length, roots, prime, pairs=2):
    if pairs < 1 or roots < 2 * pairs or length < 2 * roots:
        raise ValueError("Require pairs>=1, n>=2*pairs, and L>=2n.")
    if not sp.isprime(prime) or prime <= length + 1:
        raise ValueError("The modulus must be a prime greater than L+1.")
    t = sp.Symbol("t")
    degree = roots - 2 * pairs
    variables = sp.symbols("h0:" + str(degree))
    # At L=2n the coefficient of t^(2n-1) in the Wronskian forces
    # the coefficient of t^(n-1) in Q to vanish.
    if length == 2 * roots and degree:
        variables = variables[:-1]
    ring = sp.GF(prime).poly_ring(*variables) if variables else sp.GF(prime)
    h = t**degree + sum(variable * t**i for i, variable in enumerate(variables))
    q = sp.Poly(sp.expand((t*t - 1)**pairs * h), t, domain=ring)
    qplus = sp.Poly(q.as_expr().subs(t, t + 1), t, domain=ring)
    qminus = sp.Poly(q.as_expr().subs(t, t - 1), t, domain=ring)
    residual = sp.Poly(t**length, t, domain=ring)
    companion_degree = length - roots + 1

    for m in range(companion_degree, -1, -1):
        if m == roots:
            continue  # Fix the gauge coefficient [t^n]P=0.
        column = (sp.Poly((t+1)**m, t, domain=ring) * qminus
                  - sp.Poly((t-1)**m, t, domain=ring) * qplus)
        factor = ring.convert(residual.nth(m + roots - 1))
        factor *= ring.convert(pow(2 * (m - roots), -1, prime))
        residual -= column.mul_ground(factor)

    return variables, [value for value in residual.all_coeffs() if value != 0]


def check(length, roots, prime):
    variables, system = equations(length, roots, prime)
    print("L=", length, "n=", roots, "prime=", prime,
          "variables=", len(variables), "equations=", len(system), flush=True)
    if not variables:
        excluded = bool(system)
    else:
        basis = sp.groebner(system, *variables, modulus=prime,
                            order="grevlex", method="f5b")
        excluded = len(basis.polys) == 1 and basis.polys[0].total_degree() == 0
        print("Groebner basis size:", len(basis.polys), flush=True)
    print("RESULT:", "EXCLUDED" if excluded else "INCONCLUSIVE", flush=True)
    return excluded


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("L", type=int)
    parser.add_argument("n", type=int)
    parser.add_argument("--prime", type=int, default=101)
    args = parser.parse_args()
    started = time.monotonic()
    check(args.L, args.n, args.prime)
    print("Elapsed seconds:", round(time.monotonic() - started, 2), flush=True)
