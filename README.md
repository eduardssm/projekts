# Gala darbs-projekts studiju kursā DIP225
## Autors-Eduards Muciņš 231RDB206
## Projekta Uzdevums
Projekta mērķis ir izstrādāt programmu, kas automātiski iegūst informāciju par nākamās dienas RTU lekcijām un nodarbībām, pamatojoties uz manu studiju programmu, kursu un grupu. Piemēram, ja šodien ir trešdiena 13.03.2024, tad programma meklēs rītdienas datunmu HTML failā un no tās klases meklēs info pār tās dienas lekcijām.

## Izmantotās bibliotēkas
- **Selenium, Datetime un Time**
  - Rindiņas `import selenium` un `from selenium import webdriver` Python skriptā, tas norāda, ka skripts izmantos Selenium bibliotēku. Pirms izmantot Selenium, ir nepieciešams to instalēt. To var izdarīt, izmantojot pip install selenium'
    
  - Rindiņa from selenium.webdriver.chrome.service import Service ir daļa no Selenium bibliotēkas un tā tiek izmantota, lai norādītu, kāds serviss jāizmanto, ja vēlaties palaist Chrome pārlūkprogrammu, izmantojot Selenium. Lai precizētu, kad izmantojat Selenium, jums ir nepieciešama atbilstoša pārlūkprogrammas vadības (driver) programma, lai sasaistītu Selenium ar konkrētu pārlūkprogrammu. Šajā gadījumā Service klase tiek izmantota, lai konfigurētu un vadītu servisu, kas atbild par Chrome pārlūkprogrammas darbību.
    
  - from selenium.webdriver.common.by import By rindiņa ir daļa no Selenium bibliotēkas, kas tiek izmantota Python valodā, lai automatizētu web pārlūkprogrammu darbības. By klase piedāvā dažādas metodes vai stratēģijas, kas palīdz identificēt HTML elementus uz web lapas. Šīs stratēģijas var būt, piemēram, pēc ID, klases, nosaukuma, sākuma vai beigu teksta, linka teksta utt
    
  - Rindiņas import time Python skriptā norāda, ka skripts izmantos time bibliotēku. Šī bibliotēka nodrošina funkcijas, kas ļauj ar laiku aizkavēt programmas izpildi.
    
  - Rindiņas from datetime import datetime, timedelta Python skriptā norāda, ka skripts izmantos datetime un timedelta objektus no datetime bibliotēkas. Šī bibliotēka tiek izmantota, lai iegūtu pašreizējo datumu un timedelta, lai to parvēidotu, piemēram, pievieno papildus dienu

## Programmas struktūra
- Programma sastāv no aptuveni 50 rindām koda, kas ir pēc iespējas īsākais kods ko spēju izveidot.
- Lai sāktu šo programmu, bija jāātrod URL priekš RTU nodarbībām. Nākamais solis bija automatizēt no lapas atvēršanas izvēlnes(studiju programma, kurss, grupa), kas tika realizēts izmantojot selenium webdriver. Atrodot HTML kodā vajadzīgās vērtība, izmantojot ...click() funkciju var automātiski atvērt mājaslapu.

-Pēc šī soļa ir jāatrod HTML faila katras dienas dokumentāciju, lai varētu šodienas datumu pārvērst par rītdienas datumu un atrat HTML failā rītdienas lekcijas aprakstu. Šīs solis sagādāja lielākās grūtības projekta realizēšanā. 
