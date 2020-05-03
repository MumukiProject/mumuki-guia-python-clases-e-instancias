def test_"bouba no sabe correr":
  expect(bouba.sabe_correr?).to be False


def test_"kiki no sabe correr":
  expect(kiki.sabe_correr?).to be False


def test_"bouba grita ¡agrrrg!":
  expect(bouba.gritar).to eq "¡agrrrg!"


def test_"kiki grita ¡agrrrg!":
  expect(kiki.gritar).to eq "¡agrrrg!"


def test_"bouba tiene 100 de salud inicialmente y está con vida":
  expect(bouba.salud).to eq 100
  expect(bouba.sin_vida?).to eq False


def test_"kiki tiene 100 de salud inicialmente y está con vida":
  expect(kiki.salud).to eq 100
  expect(kiki.sin_vida?).to eq False


def test_"Si bouba recibe 5 puntos de daño disminuye su salud en 10 puntos y está con vida":
  bouba.recibir_danio!(5)
  expect(bouba.salud).to eq 90
  expect(bouba.sin_vida?).to eq False


def test_"Si kiki recibe 5 puntos de daño disminuye su salud en 10 puntos y está con vida":
  kiki.recibir_danio!(5)
  expect(kiki.salud).to eq 90
  expect(kiki.sin_vida?).to eq False


def test_"Si bouba recibe mucho daño su salud es 0 y no está con vida":
  bouba.recibir_danio!(69)
  expect(bouba.salud).to eq 0
  expect(bouba.sin_vida?).to eq True


def test_"Si kiki recibe mucho daño su salud es 0 y no está con vida":
  kiki.recibir_danio!(69)
  expect(kiki.salud).to eq 0
  expect(kiki.sin_vida?).to eq True
