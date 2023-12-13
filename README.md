# Adatbázis konverter program
A program egy konfigurációs fájlból kiolvasott adatok alapján megpróbál csatlakozni egy MySQL szerver megadott adatbázisára. Ezt követően kilistázza az adatbázisban elérhető összes adattáblát.
Lehetőség van a lista frissítésére arra az esetre, ha menet közben új tábla kerülne létrehozásra. A lista minden eleme mellett található egy jelölőnégyzet, amelyekkel tetszőlegesen kiválaszthatjuk az adattáblákat.
Lehetőség van a kiválasztott táblákat egy a felhasználó által kiválasztott mappába, CSV kiterjesztésben elmenteni.

## Telepítés
A kód fordításához ajánlott a legfrissebb, vagy legalább 3.6-os verziójú [Python telepítése](https://www.python.org/downloads/). Példa a program fordítására és futtatására PowerShellt használva:

```
git clone https://github.com/k-kristof/database_converter.git
cd .\database_converter\
python -m pip install virtualenv
python -m virtualenv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python .\src\main.py
```

Amennyiben csak a külső függőségeket kell telepíteni:

`pip install mysql_connector_python wxPython`

## Konfigurációs fájl
A konfigurációs fájlt egy párbeszédpanelen keresztül kell betallózni. A fájlnak tartalmaznia kell egy `mysql` nevű objektumot, amelynek a következő tulajdonságokkal kell rendelkeznie: `host`, `user`, `password`, `database`. A fájl kiterjesztése többféle lehet (például `.conf`, `.ini`, `.txt`, `.json`), de tartalmilag csak kétféle szabvány támogatott:

<table>
<tr>
<td>INI</td>
<td>JSON</td>
</tr>
<tr>
<td>
<pre>
[mysql]
host=
user=
password=
database=
</pre>
</td>
<td>
<pre>
{
    "mysql": {
        "host":"",
        "user":"",
        "password":"",
        "database":"",
    }
}
</pre>
</td>
</tr>
</table>

## A program működése
Induláskor felugrik egy ablak, ami négy elemet tartalmaz:
* egy 'Tallózás' feliratú aktív gomb
* egy 'Frissítés' feliratú inaktív gomb
* egy 'Mentés' feliratú inaktív gomb
* egy üres jelölőnégyzet lista
  
Ekkor csak a tallózó gombbal tudunk interakcióba lépni, amire rákattintva megnyílik egy fájltallózó párbeszédpanel. Itt kiválaszthatjuk a megfelelő konfigurációs fájlt, ami után a program betölti azt és a beolvasott adatok alapján csatlakozik a adatbázisszerverre. Ezt követően aktiválódik a frissítő és a mentő gomb, valamint a jobb oldalon található listában automatikusan megjelennek az adatbázisban található táblák nevei. A 'Frissítés' gombra kattintva újra lekérdezhetjük a táblákat arra az esetre, ha a program használata közben új tábla kerülne létrehozásra. Amennyiben nincs kijelölve egyetlen tábla sem a listából, a 'Mentés' gombra kattinva erről tájékoztató hibaüzenetet kapunk. Legalább egy, tetszőleges táblát kiválasztva már rákattinthatunk erre a gombra, ami egy fájlmentő párbeszédpanelt nyit meg. Itt ki kell választanunk egy célmappát, ahová aztán a kiválasztott listaelemek az eredeti nevükön, de `.csv` kiterjesztéssel elmentésre kerülnek. A folyamatot bármeddig ismételhetjük.

## Lehetséges fejlesztések
* a táblák megjelenítésekor további információk kerüljenek kiírásra - például méret, sorok száma, utolsó szerkesztési idő
* betekintés a táblákba - kiválasztáskor lekérdezzük az első n darab sort a táblából és megjelenítjük azt
* tetszőleges mentés - táblákat tetszőleges néven, tetszőleges szabvány fájlkiterjesztéssel (például: XML) lehessen elmenteni
