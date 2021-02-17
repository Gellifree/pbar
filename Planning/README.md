# Tervek

## Jelzés alapú elképzelés alapjainak megvalósítása.

```
Bar.size = N
Ciklus N-ig:
	DoSomething()
	Bar.Signal()
```
Minden iteráció esetén, jelzünk a BAR-nak hogy mozoghat. Ez esetben ujrarajzolódik.
Magának a BAR-nak nem kell megkapnia paraméterben hogy min iterál végig, csak a méretet.
így moduláris a működés.
