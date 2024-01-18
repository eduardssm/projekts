# Gala darbs-projekts studiju kursā DIP225
## Autors-Eduards Muciņš 231RDB206
## Projekta Uzdevums
Projekta mērķis ir izstrādāt programmu, kas automātiski iegūst informāciju par nākamājam RTU lekcijām un nodarbībām, pamatojoties uz manu studiju programmu, kursu un grupu. 

## Izmantotās bibliotēkas
- **Selenium un Time**
  - source.py izmanto selenium un time bibliotēkas,
      - selenium izmanto, lai iegūtu informāciju no RTU nodarbību mājaslapas izmantojot HTML "web       scraping"
      - time bibliotēku izmanto, lai varētu iegūt šodienas datumu, kuru pēc tam pārvērš uz nākāmas dienas datumu, lai varētu ar selenium palīdzību iegūt datus par nākamās dienas nodarbībām

## Programmas struktūra
- Programma sastāv no aptuveni 50 rindām koda, kas ir pēc iespējas īsākais kods ko spēju izveidot.
- Lai sāktu šo programmu, bija jāātrod URL priekš RTU nodarbībām. Nākamais solis bija automatizēt no lapas atvēršanas izvēlnes(studiju programma, kurss, grupa), kas tika realizēts izmantojot selenium webdriver. Atrodot HTML kodā vajadzīgās vērtība, izmantojot ...click() funkciju var automātiski atvērt mājaslapu.

-Pēc šī soļa ir jāatrod HTML faila katras dienas dokumentāciju, lai varētu šodienas datumu pārvērst par rītdienas datumu un atrat HTML failā rītdienas lekcijas aprakstu. Šīs solis sagādāja lielākās grūtības projekta realizēšanā. 
