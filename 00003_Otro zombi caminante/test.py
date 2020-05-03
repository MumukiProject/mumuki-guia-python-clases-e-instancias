def test_"Bouba no sabe correr":
  expect(Bouba.sabe_correr?).to be False


def test_"Kiki no sabe correr":
  expect(Kiki.sabe_correr?).to be False


def test_"Bouba grita ¡agrrrg!":
  expect(Bouba.gritar).to eq "¡agrrrg!"


def test_"Kiki grita ¡agrrrg!":
  expect(Kiki.gritar).to eq "¡agrrrg!"


def test_"Bouba tiene 100 de salud inicialmente":
  expect(Bouba.salud).to eq 100


def test_"Kiki tiene 100 de salud inicialmente":
  expect(Kiki.salud).to eq 100


def test_"Si Bouba recibe 5 puntos de daño disminuye su salud en 10 puntos":
  Bouba.recibir_danio!(5)
  expect(Bouba.salud).to eq 90


def test_"Si Kiki recibe 5 puntos de daño disminuye su salud en 10 puntos":
  Kiki.recibir_danio!(5)
  expect(Kiki.salud).to eq 90


def test_"Si Bouba recibe mucho daño su salud no puede ser menor a 0":
  Bouba.recibir_danio!(69)
  expect(Bouba.salud).to eq 0


def test_"Si Kiki recibe mucho daño su salud no puede ser menor a 0":
  Kiki.recibir_danio!(69)
  expect(Kiki.salud).to eq 0
