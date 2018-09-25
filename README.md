# RTR105
## Datormācības kursā elektroniskā klade


_Iepriekš paskaidrotās komandās ar laiku parādīsies papildinājumi un papildinājumi veikšanu datumu._


#### 2.nodarbības izmantoto komandu paskaidrojumi
**"cd"** - change directory, nomaina darbību atrašanās vietu;

**"man"** - manual, norāda norādītās komandas funkciju;

  i.e. _"man cd"_
  
  
**"uname"** - prints system information on screen, norāda sistēmas informāciju. 
Pievienojot _"-a"_, tiks norādīta OS versija, kernel nosaukums u.t.t.;


**"echo"** - "echoes" a line of text input by the user, uzraksta doto tekstu vai informāciju nākamajā līnijā. 


Izmanotojot kopā ar _"$0"_, tiks norādīts dotajā brīdī lietotais SHELL skripts;

Izmanotojot kopā ar _"-e"_, tiks pieļauti teksta papildinājumi, piemēram "\n";**(17.09.2018)**



**"sh"** - switch to sh script, pārslēdz no noklusējuma bash skripta uz sh. Lai tiktu atpakaļ, jāraksta terminālī _"bash"_;

**"whoami"** - displays current users name, norāda lietotāja nosaukumu jeb vārdu;

**"who"** - displays which users are online at the moment, norāda pieslēgtos lietotājus un ārējos pieslēgumus;

**"pwd"** - displays current directory, norāda pašreizējo funkciju izpildes vietu jeb atrašanos failu sistēmā;

**"ls"** - lists the contents of the current directory, norāda mapes sastāvu - kādas mapes ir pieejamas šajā mapē.

  Pievienojot _"-l"_, tiks norādīts detalizēts saraksts. 
  
  Burtu virknes nozīme: 
  
   1. "d vai -" - ar "_d_" tiek apzīmētas mapes, ar _"-"_ tiek apzīmēts fails pašreizējā atrašanās vietā failu sistēmā;
   2. "r" - read jeb lasīšanas piekļuve;
   3. "w" - write jeb rakstīšanas piekļuve;
   4. "x" - execute jeb palaišanas/atvēršanas piekļuve.
    **(25.09.2018)**
  
  Pievienojot _"-a"_, tiks norādīts arī lietotājam apslēpti faili un mapes, kuras nevajadzētu mainīt vai dzēst.


**"history"** - prints a full history of used commands, including from previous sessions, norāda visas iepriekš lietotās komandas, tajā skaitā arī no iepriekšējām termināļa lietošanas reizēm;


  Lietojot ar _"> XXXXXXXX.txt"_, X vietā rakstot vēlamo teksta faila nosaukumu, tiks izveidots .txt fails ar visu vēsturi.



#### 3.nodarbības izmantoto komandu paskaidrojumi


**"mkdir"** - makes a directory, izveido jaunu mapi;


  i.e. "_mkdir ManaMape_"


**"rmdir"** - removes the specified directory, nodzēš norādīto mapi. Nedzēš, ja tajā ir kaut kas iekšā bez papildus argumenta;


**"rm"** -  removes the specified file or directory, nodzēš norādīto failu vai mapi un tās apakšmapes. 

  
  Pievienojot "_-r_", failus noņems bez ierunām;


**"more; nano; less"** - displays the specified .txt file, depending on the command used, parāda norādīto .txt failu atkarībā no lietotās komandas.

  **"nano"** - Nano's ANOther editor, teksta rediģētājs termināli.
  

**"chmod"** - changes the _Read/Write/Execute_ permissions of the chosen file, nomaina noteiktā faila _Rakstīšanas/Lasīšānas/Palaišanas_ atļaujas. Skatīt _"ls"_ apakšpunktu _"-l"_.
  
   "chmod XXX" ievietojot "X" vietā noteiktu skaitli {0;1;2;3;4;5;6;7}, tiks mainīta attiecīgā lietotāja rwx vērtība, atkarībā no izvēlētā "X".
    
    0 - tiks noņemtas visas atļaujas;
    1 - tiks iedota Execute atļauja;
    2 - tiks iedota Write atļauja;
    3 - tiks iedotas Write un Execute atļaujas;
    4 - tiks iedota Read atļauja;
    5 - tiks iedotas Read un Execute atļaujas;
    6 - tiks iedotas Read un Write atļaujas;
    7 - tiks iedotas visas 3 atļaujas.
    
    
**"mv"** - moves or renames files, depending on the chosen name and location in the command line, pārvieto vai pārsauc failu, atkarībā no izvēlētā nosaukuma un izvēlētās saglabāšanas vietas.


Faila pārsaukšana.

    mv fails1.txt fails101.txt
    
    
Faila pārvietošana.

    mv fails1.txt Mape
    mv fails1.txt ../


**"cp"** - copies files to the designated location with the chosen name(if chosen), kopē failus uz noteikto vietu failu sistēmā ar noteikto nosaukumu(ja izvēlēts jauns).


Faila kopēšana

    cp fails1.txt ./fails101.txt
    cp fails1.txt Music
