# RTR105
## Datormācības kursā elektroniskā klade


_Iepriekš paskaidrotās komandās ar laiku parādīsies papildinājumi un papildinājumi veikšanu datumu._


#### 2.nodarbības izmantoto komandu paskaidrojumi
**"cd"** - change directory, nomaina darbību atrašanās vietu;


Atgriezties home/user mapē.


    cd ~


**"man"** - manual, norāda norādītās komandas funkciju;


        man cd
  
  
**"uname"** - prints system information on screen, norāda sistēmas informāciju. 
Pievienojot _"-a"_, tiks norādīta OS versija, kernel nosaukums u.t.t.;


        uname
        Linux
        uname -a
        Linux User-VirtualBox 4.15.0-34-generic #37-Ubuntu SMP Mon Aug 27 15:21:48 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux



**"echo"** - "echoes" a line of text input by the user, uzraksta doto tekstu vai informāciju nākamajā līnijā. 


Izmanotojot kopā ar _"$0"_, tiks norādīts dotajā brīdī lietotais SHELL skripts;


        echo $0
        bash


Izmanotojot kopā ar _"-e"_, tiks pieļauti teksta papildinājumi, piemēram "\n";**(17.09.2018)**



**"sh"** - switch to sh script, pārslēdz no noklusējuma bash skripta uz sh. Lai tiktu atpakaļ, jāraksta terminālī _"bash"_;

**"whoami"** - displays current users name, norāda lietotāja nosaukumu jeb vārdu;


        whoami
        user


**"who"** - displays which users are online at the moment, norāda pieslēgtos lietotājus un ārējos pieslēgumus;

**"pwd"** - displays current directory, norāda pašreizējo funkciju izpildes vietu jeb atrašanos failu sistēmā;

**"ls"** - lists the contents of the current directory, norāda mapes sastāvu - kādas mapes ir pieejamas šajā mapē.


        ls
        Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos


  Pievienojot _"-l"_, tiks norādīts detalizēts saraksts. 
  
  Burtu virknes nozīme: 
  
   1. "d vai -" - ar "_d_" tiek apzīmētas mapes, ar _"-"_ tiek apzīmēts fails pašreizējā atrašanās vietā failu sistēmā;
   2. "r" - read jeb lasīšanas piekļuve;
   3. "w" - write jeb rakstīšanas piekļuve;
   4. "x" - execute jeb palaišanas/atvēršanas piekļuve.
    **(25.09.2018)**
    
    
      drwxrwxrwx
    
  
  Pievienojot _"-a"_, tiks norādīts arī lietotājam apslēpti faili un mapes, kuras nevajadzētu mainīt vai dzēst, vai nav svarīgas parastam lietotājam.
  
  
Mapes sastāva parādīšana, ja neatrodies vēlamajā mapē.
    
    ls ~/Music


**"history"** - prints a full history of used commands, including from previous sessions, norāda visas iepriekš lietotās komandas, tajā skaitā arī no iepriekšējām termināļa lietošanas reizēm;


  Lietojot ar _"> XXXXXXXX.txt"_, "X" vietā rakstot vēlamo teksta faila nosaukumu, tiks izveidots .txt fails ar visu vēsturi.



#### 3.nodarbības izmantoto komandu paskaidrojumi


**"mkdir"** - makes a directory, izveido jaunu mapi;


    mkdir ManaMape


**"rmdir"** - removes the specified directory, nodzēš norādīto mapi. Nedzēš, ja tajā ir kaut kas iekšā bez papildus argumenta;


**"rm"** -  removes the specified file or directory, nodzēš norādīto failu vai mapi un tās apakšmapes. 

  
  Pievienojot "_-r_", failus noņems bez ierunām ar visām apakšmapēm un apakšfailiem;


    rm -r ManaMape


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
