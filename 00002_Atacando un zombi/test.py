def test_"La energía inicial de Juliana es 1000":
  expect(Juliana.energia).to eq 1000


def test_"Si Juliana ataca con 5 puntos de daño a Bouba su salud disminuye en 10 puntos":
  Juliana.atacar!(Bouba, 5)
  expect(Bouba.salud).to eq 90


def test_"Si Juliana ataca con 10 puntos de daño a Bouba su salud disminuye en 20 puntos":
  Juliana.atacar!(Bouba, 10)
  expect(Bouba.salud).to eq 70


def test_"Si Juliana ataca a Bouba con mucho daño su salud no puede ser menor a 0":
  Juliana.atacar!(Bouba, 69)
  expect(Bouba.salud).to eq 0
