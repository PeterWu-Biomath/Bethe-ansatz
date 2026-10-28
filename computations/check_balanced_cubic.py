"""Exact finite-parameter checks for three additional Bethe roots.

For specified a,L, exclude H|S_a together with Xi=K=0 by polynomial
gcds over cyclotomic number fields. This is not a proof for all a,L.
Run with a SymPy installation: python check_balanced_cubic.py 2 14.
"""

import argparse
import time

import sympy as sp


def check_fiber(a, length, h_expr, parameter, domain, substitutions, name):
    t = sp.Symbol("t")
    print(name, ": constructing the degree-two obstruction", flush=True)

    def polynomial(expr):
        if not substitutions:
            return sp.Poly(expr, parameter, domain=domain)
        variable, root = next(iter(substitutions.items()))
        raw = sp.Poly(expr, parameter, domain=sp.QQ.frac_field(variable))
        if domain == sp.QQ:
            return sp.Poly.from_dict(
                {power: domain.convert(value.subs(variable, root))
                 for power, value in raw.terms()}, parameter, domain=domain)
        generator = domain.convert(domain.ext)

        def evaluate(value):
            numerator, denominator = sp.fraction(sp.cancel(value))

            def horner(expression):
                result = domain.zero
                for scalar in sp.Poly(expression, variable, domain=sp.QQ).all_coeffs():
                    result = result * generator + domain.convert(scalar)
                return result

            return horner(numerator) / horner(denominator)

        return sp.Poly.from_dict({power: evaluate(value) for power, value in raw.terms()},
                                 parameter, domain=domain)

    logarithmic = sp.diff(h_expr, t) / h_expr
    obstruction = sp.cancel(
        sp.Rational(2 * length - 5 * a, 2)
        - logarithmic.subs(t, 3)
        - logarithmic.subs(t, 1)
        + logarithmic.subs(t, -1)
        + logarithmic.subs(t, -3)
    )
    numerator = sp.fraction(obstruction)[0]
    modulus = polynomial(numerator).monic()
    if modulus.degree() == 0:
        print(name, ": K is a unit; excluded", flush=True)
        return True

    def coefficient(expr):
        return polynomial(expr).rem(modulus)

    zero, one = coefficient(0), coefficient(1)
    h = sp.Poly(h_expr, t)
    hc = [coefficient(h.nth(i)) for i in range(3)]

    def add(left, right):
        return [x + y for x, y in zip(left, right)]

    def multiply(left, right):
        result = [zero] * 5
        for i in range(3):
            for j in range(3):
                result[i + j] += (left[i] * right[j]).rem(modulus)
        for i in (4, 3):
            lead = result[i].rem(modulus)
            for j in range(3):
                result[i - 3 + j] -= (lead * hc[j]).rem(modulus)
        return [value.rem(modulus) for value in result[:3]]

    def power(base, exponent):
        value = [one, zero, zero]
        while exponent:
            if exponent & 1:
                value = multiply(value, base)
            base = multiply(base, base)
            exponent //= 2
        return value

    def shifted_h(shift):
        # H(t+shift), reduced modulo H(t), whose leading coefficient is 1.
        expanded = sp.Poly(sp.expand(h_expr.subs(t, t + shift) - h_expr), t)
        return [coefficient(expanded.nth(i)) for i in range(3)]

    plus = multiply(power([one, one, zero], length - a),
                    power([coefficient(-3), one, zero], a))
    minus = multiply(power([coefficient(-1), one, zero], length - a),
                     power([coefficient(3), one, zero], a))
    remainder = add(multiply(plus, shifted_h(-2)),
                    multiply(minus, shifted_h(2)))
    common = modulus
    for value in remainder:
        common = sp.gcd(common, value)

    # Clearing denominators must not leave configurations excluded in the note.
    bad = sp.prod(h_expr.subs(t, value) for value in (-3, -1, 1, 3))
    bad *= sp.discriminant(h_expr, t)
    bad = polynomial(sp.cancel(bad))
    while common.degree() > 0:
        removed = sp.gcd(common, bad)
        if removed.degree() == 0:
            break
        common = common.exquo(removed)
    print(name, ": common gcd degree", common.degree(), flush=True)
    return common.degree() == 0


def check(a, length):
    if a < 2 or length < 4 * a + 6:
        raise ValueError("Require a>=2 and L>=4a+6.")
    t, p, v, s = sp.symbols("t p v s")
    same_parity = (length - a) % 2 == 0
    if same_parity:
        total = -(3 * (p + 9) + v**2 * (p + 1)) / (8 * v)
    else:
        total = -v * (p + 7) / 2
    constant = v * (p + 1) - total
    h = t**3 - total * t**2 + p * t - constant
    momentum = sp.Poly(
        (-(1 + v))**length - (-1)**(a * length) * (1 - v)**length, v
    )
    passed = True
    for factor, _multiplicity in sp.factor_list(momentum)[1]:
        factor = sp.Poly(factor, v)
        if same_parity and factor.eval(0) == 0:
            continue  # The v=0 endpoint is checked separately below.
        if factor.degree() == 1:
            root = -factor.nth(0) / factor.nth(1)
            domain = sp.QQ
        else:
            domain = sp.QQ.alg_field_from_poly(factor, alias="vroot")
            root = domain.ext
        passed &= check_fiber(
            a, length, h, p, domain, {v: root}, "momentum " + str(factor.as_expr())
        )

    if same_parity:
        # Pi=1 implies p=-1 and q=-9s. Pi=-1 implies p=-9 and q=-s.
        passed &= check_fiber(a, length, t**3 - s*t*t - t + 9*s,
                              s, sp.QQ, {}, "Pi=1")
        if length % 2 == a * length % 2:
            passed &= check_fiber(a, length, t**3 - s*t*t - 9*t + s,
                                  s, sp.QQ, {}, "Pi=-1")
    print("RESULT:", "EXCLUDED" if passed else "UNRESOLVED", flush=True)
    return passed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int)
    parser.add_argument("L", type=int)
    args = parser.parse_args()
    started = time.monotonic()
    check(args.a, args.L)
    print("Elapsed seconds:", round(time.monotonic() - started, 2), flush=True)
