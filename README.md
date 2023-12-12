# Adatbázis konverter program
A program egy konfigurációs fájlból kiolvasott adatok alapján megpróbál csatlakozni egy MySQL szerver megadott adatbázisára. Ezt követően kilistázza az adatbázisban elérhető összes adattáblát.
Lehetőség van a lista frissítésére arra az esetre, ha menet közben új tábla kerülne létrehozásra. A lista minden eleme mellett található egy jelölőnégyzet, amelyekkel tetszőlegesen kiválaszthatjuk az adattáblákat.
Lehetőség van a kiválasztott táblákat egy a felhasználó által kiválasztott mappába, CSV kiterjesztésben elmenteni.

## Konfigurációs fájl

A konfigurációs fájlt egy párbeszédpanelen keresztül kell betallózni. A fájlnak tartalmaznia kell egy `mysql` nevű objektumot, amelynek a következő tulajdonságokkal kell rendelkeznie: `host`, `user`, `password`, `database`. A fájl kiterjesztése többféle lehet (például `.conf`, `.ini`, `.txt`, `.json`), de tartalmilag csak kétféle szabvány támogatott:

INI:
```
[mysql]
host=
user=
password=
database=
```

JSON:
```
{
    "mysql": {
      "host":"",
      "user":"",
      "password":"",
      "database":"",
    }
}
```
