# Autonomiczny saper. Projekt SI część pierwsza etap wspólny

<b>Grupa projektowa: Zofia Bączyk Marek Gulawski Witold Borowiak</b>

<p>W tej części prjektu wykonano:
  <ol>
    <li>Reprezentację obiektów i ich stanów na kracie</li>
    <li>Agenta, Sapera, będącego głównym obiektem projektu</li>
    <li>Graficzną reprezentację kraty oraz jej elementów</li>
  </ol>
 </p>
## Technolohie użyte do wykonania
<p>Całe środowisko zostało napisane w Python 3.8 w oparciu o bibliotekę Pygame 1.9.6. 
Następne etapy projektu również będą opartę o ten język programowania. 
Brak zmiany technologi zapewni większą spójność projektu.</p>

## Krata
<a id="krata"> Zdjęcie </a>
[krata]: https://drive.google.com/open?id=1qQnFF0h3g1D9mHqkVNUOfLFdXn_Xmhkc
<p>Obszarem możliwych ruchów jest krata. Krata jest przedstawiona jako objekty: Saper, ściana, bomba, puste pole.
Mapy są tłumaczone z dwuwymiarowej tablicy gdzie: '1'- reprezentuje ścianę, '2'- reprezentuje sapera, '3'- reprezentuje bombę a '0'- puste pola po których może poruszać się Saper.
Zasoby graficzne znajdują się w folderze images.</p>

## Obiekty
<p>Obiekty reprezentowane na kracie znajdują się w folderze objects.
Znajdują się tam obiekty: Saper, Bomba, Ściana.</p>

## Mapy
<p>Mapy zapisane w postaci tablic dwuwymiarowych zapisane są w folderze maps. 
Przy uruchamianiu programu są one przez niego tłumaczone na obiekty oraz kratę po której może poruszać się Saper.</p>