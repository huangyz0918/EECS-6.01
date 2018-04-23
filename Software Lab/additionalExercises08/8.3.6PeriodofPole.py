def periodOfPole(pole):
	pole = complexPolar(pole)
	if pole[1] == 0:
		return None
	else:
		return pole[1]

def complexPolar(p):
	if isinstance(p, complex):
		return (abs(p), math.atan2(p.imag, p.real))
	else:
		if p < 0:
			return (-p, math.pi)
		else:
			return (p, 0.0)

