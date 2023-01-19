# %%
from sympy import symbols, sin, cos, Symbol, solveset, diff, pprint, S
from sympy.plotting import plot
x = Symbol('x')
func = plot(sin(x)**2 - cos(x)*2, show = False)
func.show()

# %%
pprint(solveset(sin(x)**2 - cos(x)**2, x, domain=S.Reals), use_unicode = True)

# %%
pprint(solveset(sin(x)**2 - cos(x)**2 <0, x, domain= S.Reals), use_unicode=True)

# %%
pprint(solveset(sin(x)**2 - cos(x)**2 >0, x, domain= S.Reals), use_unicode=True)

# %%
eq_diff = diff(sin(x)**2 - cos(x)**2, x)
plot(eq_diff, show = False).show()
eq_diff

# %%
pprint(solveset(eq_diff, x, domain = S.Reals), use_unicode = True)

# %%
pprint(solveset(eq_diff>0, x, domain= S.Reals), use_unicode=True)

# %%
pprint(solveset(eq_diff < 0, x, domain= S.Reals), use_unicode=True)

