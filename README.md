# RTR105
## Datormācības kursā elektroniskā klade


_Iepriekš paskaidrotās komandās ar laiku parādīsies papildinājumi un papildinājumi veikšanu datumu._



###Shell komandas



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


    history >yourhistorytext.txt
    ls
    Desktop    Downloads         Music                 Videos    Templates
    Documents  examples.desktop  yourhistorytext.txt   Pictures  Public


#### 3.nodarbības izmantoto komandu paskaidrojumi


**"mkdir"** - makes a directory, izveido jaunu mapi;


    mkdir ManaMape


**"rmdir"** - removes the specified directory, nodzēš norādīto mapi. Nedzēš, ja tajā ir kaut kas iekšā bez papildus argumenta;


**"rm"** -  removes the specified file or directory, nodzēš norādīto failu vai mapi un tās apakšmapes. 

  
  Pievienojot "_-r_", failus noņems bez ierunām ar visām apakšmapēm un apakšfailiem;


    rm -r ManaMape


**"more; nano; less; cat"** - displays the specified .txt file, depending on the command used, parāda norādīto .txt failu atkarībā no lietotās komandas.

  **"nano"** - Nano's ANOther editor, teksta rediģētājs termināli.
  

**"chmod"** - changes the _Read/Write/Execute_ permissions of the chosen file, nomaina noteiktā faila _Rakstīšanas/Lasīšānas/Palaišanas_ atļaujas. Skatīt _"ls"_ apakšpunktu _"-l"_.
  

#####chmod Atslēgas


   "chmod XXX" ievietojot "X" vietā noteiktu skaitli {0;1;2;3;4;5;6;7} jeb atslēgu, tiks mainīta attiecīgā lietotāja rwx vērtība, atkarībā no izvēlētā "X".
    
    0 - tiks noņemtas visas atļaujas;           ---
    1 - tiks iedota Execute atļauja;            --x
    2 - tiks iedota Write atļauja;              -w-
    3 - tiks iedotas Write un Execute atļaujas; -wx
    4 - tiks iedota Read atļauja;               r--
    5 - tiks iedotas Read un Execute atļaujas;  r-x
    6 - tiks iedotas Read un Write atļaujas;    rw-
    7 - tiks iedotas visas 3 atļaujas;          rwx
    
    
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


#### 4.nodarbības izmantoto komandu paskaidrojumi


Skriptu veidošana. Ar faila tipu _".sh"_ tiek norādīts shell skripts. Skriptu rakstīšanu var veikt NANO teksta rediģētājā.


    nano mans_skripts.sh


Noklusējumā skripts nav palaižams(trūkst executable atļauja). To pievieno, izmantojot _"chmod"_. Vajadzīgās atļaujas atslēgu skatīt sadaļā "chmod Atslēgas".


    chmod 764 mans_skripts.sh



### Python




Vērtību piešķiršana kādam mainīgajam notiek caur _"="_ jeb vienādības zīmi.


    >>> x = 10
    >>> print(x)
    10


Piešķirto vērtību var mainīt, piešķirot tam pašam mainīgajam citu vērtību.


    >>> x = 10
    >>> print(x)
    10
    >>> x = 20
    >>> print(x)
    20


Šos mainīgos var izmantot matemātiskās darbībās - saskaitīšanā(+), atņemšanā(-), reizināšānā(*), dalīšanā(/), kāpināšanā(**) un dalījuma atlikuma noteikšanā(%). Iekavās norādīts darbības simbols Python valodā.


    >>> x = 10; y = 20; z = y + 5; L = 3
    >>> print(x+y)
    30
    >>> print(y-x)
    10
    >>> print(x*y)
    200
    >>> print(x*2)
    20
    >>> print(x/y)
    0.5
    >>> print(x**2)
    100
    >>> print(z**(x/y))
    5.0
    >>> print(x % L)
    1


Mainīgā vērtību var mainīt, matemātiskajā darbībā izmantojot pašu mainīgo.


    >>> x = 2
    >>> x = x + 3
    >>> print(x)
    5



**"print()"** - izprintē doto informāciju. Tā var būt dotā mainīgā vērtība, dotais teksts(string vērtība), skaitliska konstante vai kāda šo elementu kombinācija.


    >>> x = 20
    >>> print(x)
    20
    >>> print(137)
    137
    >>> print("This is a test")
    This is a test
    >>>print("The value of x is", x)
    The value of x is 20


**"type()"** - norāda, kāds ir dotā elementa tips.


Skaitlis bez decimālā atdalītāja ir "integer" jeb "int" vērtība, ar atdalītāju - "floating point number" jeb "float" vērtība. Teksts - "string" jeb "str".


    >>> x = 20; y = 20.0; z = "Type 4"
    >>> type(x)
    <class'int'>
    >>> type(14)
    <class'int'>
    >>> type(y)
    <class'float'>
    >>> type(z)
    <class'str'>
    >>> type("Pass")
    <class'str'>
    >>> type("4")
    <class'str'>


Ar noteiktām komandām, šo elementu tipus var mainīt.


"string" tipa elementus var pārveidot uz "integer" vai "floating point number", ja tie atbilst noteiktām prasībām. Parasti, ja kāds skaitlis ir saglabāts kā "str" vērtība, tad to var pārveidot, bet, ja  tam klāt vēl ir burti, tad pārveidošanu nevar veikt(ja vien neatlasa noteiktu vietu mainīgajā, kuru vēlas pārveidot).


**"int()"** - nomaina mainīgā tipu uz "integer".


**"float()"** - nomaina mainīgā tipu uz "floating point number".


**"str()"** - nomaina mainīgā tipu uz "string".


    >>> x = 20; y = "4"
    >>> fx = float(x)
    >>> type(fx)
    <class'float'>
    >>> sx = str(x)
    >>> type(sx)
    <class'str'>
    >>> iy = int(y)
    >>> type(iy)
    <class'int'>


"String" tekstā var izvēlēties individuālus elementus vai elementu virkni, izmanot [] aiz mainīgā.


**"len()"** - nosaka elementu skaitu mainīgajā.


Katram elementam "string" tekstā tiek iedalīts savs kārtas skaitlis. Skaitīšana sākas no 0.
  

    c|h|a|r|a|c|t|e|r
    0|1|2|3|4|5|6|7|8


    >>> x = 'character'
    >>> print(x[3])
    r
    >>> len(x)
    9
    >>> print(x[1:3])
    har


"String" elementus var "saskaitīt".


    >>> x = 'character'
    >>> b = 'I' + '' + 'am' + '' + 'a' + x
    >>> print(b)
    I am a character


Bez '' starp vārdiem būtu izveidots viens vesels vārds.


**"vars()"** - vārdnīca, parāda pieejamos "modules" un atmiņā saglabātos mainīgos un to vērtības. Ar atribūtiem var parādīt papildu informāciju par mainīgo.

    Daži atribūti - __doc__ __dict__


**"locals()"** - vārdnīca, strādā kā "vars()", bet tas nestrādā ar mainīgajiem.



**"input()"** - pieprasa lietotāja ievadītu tekstu vai skaitli. Izmanto, ja grib dot mainīgajam citu vērtību katru reizi, kad palaiž programmu.


    x = input("Input hours worked:")


Pēc ievades, padotā vērtība tiek saglabāta kā mainīgā vērtība, bet šī vērtība ir saglabāta kā "string" vērtība. Šo tipu var mainīt ar atbilstošajām komandām ("int()","float()","str()")



Lai viegli noskaidrotu, ko funckija dara, var izmanot **"doc"**.


    >>> print(float.__doc__)
    float(x) -> floating point number
    
    Convert a string or number to a floating point number, if possible. 




Advancētākās programmās lieto **"if"** komandu, ka izpilda komandu(-as), ja tā nosacījums izpildās.


    x = 1
    if x == 1:
        print("Variable is exactly 1")


Ja neizpildās noteiktais "if", var izmantot **"elif"**, kas strādās tikai tad, ja neizpildīsies "if" vai iepriekšējais(-ie) "elif".


    x = 1
    if x > 2:
        print("More than 2")
    elif x < 2:
        print("Less than 2")


Ja neizpildās neviena no "elif" vai "if" komandām, var izmantot komandu **"else"**, kurai nav jāpievieno neviens papildu nosacījums - tā strādās, ja viss cits nepiepildās.


    x = 2
    if x > 2:
        print("More than 2")
    elif x < 2:
        print("Less than 2")
    else:
        print("Exactly 2")


Parasti "if" un "elif" izmanto salīdzinājumus, lai noteiktu, vai komandu izpildīt.

Salīdzināšanas simboli. Šie simboli tikai aplūko vērtības un tās neizmaina, pat ja salīdzinājumā ir iekļauta matemātiska darbība.

    1 <  - mazāk kā
    2 <= - mazāks vai vienāds kā
    3 == - vienāds ar(vienu = izmanto piešķiršanai)
    4 >  - vairāk kā
    5 >= - lielāks vai vienāds kā
    6 != - nav vienāds


Python valodā, pildot komandas, ir svarīgi, vai tām ir atkāpe no malas. "if" un tā paveidu apakškomandas ir vienu "tab" tālāk par pašu "if".



Lai ietaupītu vietu kodā un lai atvieglotu kļūdu meklēšanu, Python ļauj izveidot savas funkcijas.


**"def name()"** - tiek definēta funkcija, kas izpilda noteiktās funckijas, kad tā tiek izsaukta.


    def multiply():
        x = float(input("Ievadi pirmo skaitli:"))
        y = float(input("Ievadi otro skaitli:"))
        z = x * y
        return print("Reizinajuma rezultats ir :",z)

    multiply()


Lai noslēgtu uzrakstīto funkciju, kura izdod kādu mainīgā vērtību, ir jāpiesauc "return" un vēlamais funkcijas rezultāts. Lai funckija izpildītos, tā ir jāizsauc. Tā netiek pildīta pie definēšanas.


Funkcijā arī var izmantot jau ārpus tās veidotas vērtības, definējot iekavās ievietojot vienu vai vairākus mainīgos. Kad funkciju izsauc, iekavās jāievieto vēlaimais mainīgais, pēc kura veikt aprēķinus funkcijā.


Funckijā esošie mainīgie, pat ja tiem sakrīt nosaukums, paliek tikai funkcijas ietvaros. Pēc piemēra, "multiply()" x mainīgais paliek funckijā. To izsaucot, piemēram, lietojot "print(x)", tiks norādīta ķļūda, jo šāda vērtība nav definēta.


Ērta funckija Python ir "try" un "except". Ja zem "try" esošās funckijas izdod kļūdu, neizpildās pienācīgi, tad tiek pildītas zem "except" esošās darbības.


    try:
        x = float(input("Ievadi skaitli:"))
        print(x)
    except:
        print("Netika ievadiits skaitlis")


Ja tiks padots skaitlis, skaitlis tiks izprintēts. Ja tiks padots burts jebkas cits, tiks izprintēts "Netika ievadiits skaitlis".


Ļoti liela daļa programmu lieto ciklus, kas pilda funkciju, kamēr nosacījums izpildas vai arī mūžīgi(līdz piepildās atmiņa).


**"while 'nosacījums'"** - pilda apakškomandas, kamēr izpildās nosacījums. Parasti  pirms cikla tiek definēts skaitlis un cikla ietvaros šis skaitlis tiek samazināts.


    n = 3
    while n > 0:
        print(n)
        n = n - 1
    print(n)
    print("Done")


Šādas programmas izeja būtu:


    3
    2
    1
    0
    Done


Bez rindas "n = n - 1", cikls strādātu bezgalīgi, izejā printējot "3". Ja vēlas, lai cikls izbeigtos bez šādas rindas, izmanto "break" komandu.


    while True:
        line = input("-")
        if line == 'done':
            break
        print(line)
    print("Done")


Šāds cikls izprintēs visu, ko lietotājs pados, līdz kamēr tiks padots teksts "done".


Ja vēlas, lai cikls neveic savu funkciju kāda noteiktā vietā, izmanto "continue" komandu.


    while True:
        line = input("-")
        if line[0] == '#'
            continue
        if line == 'done': 
            break
        print(line)
    print("Done")


Ja ievadītā teksta pirmais elements būs "#", tad cikls sāksies no jauna un netiks izprintēts rakstītais pēc šī simbola.


**"for 'mainīgais' in 'masīvs'"** - tiek izpildīta darbība pie katra dotā masīva elementa(cik elementu, tik reizes tiks pildītas darbības ciklā).


    for i in [10, 8, 6, 4, 2]:
        print(i/2)
    print("Done")


Funkcijas rezultāts:


    5
    4
    3
    2
    1
    Done


Masīvu var definēt arī pirms šīs funckijas.


    x = [10,8,6,4,2]
    for i in x:
        ...


Masīviem var pievienot vērtības, izmantojot ".append". Piemērā tiks izprintēts masīvas ar jaunajām vērtībām. [5, 4, 3, 2, 1]


    x = []
    n = 5
    while n > 0:
        x.append(n)
        n = n -1
    print(x)



Skaitļu masīviem var mainīt individuālas vērtības. Tiem arī var izvēlēties noteiktu virkni ar elementiem, kurus izprintēt vai izmantot, izmatojot [n:m], gluži kā tika lietots "string" elementiem. Masīvu elementus skaita tāpat kā "string" elementus


    >>> x = [1, 2, 5 , 12, 209]
    >>> x[2] = 137
    >>> print(x)
    [1, 2, 137, 12, 209]
    >>> print(x[1:3])
    [2, 137, 12]


**"dict()"** - tiek izveidota vārdnīca. Tā apkopo padotos datus un ļauj ātri tiem piekļūt ar indeksiem.


    >>> soma = dict()
    >>> soma['graamata'] = 1
    >>> soma['ziimulis'] = 48
    >>> soma['klade'] = 15
    >>> print(soma)
    {'graamata': 1, 'ziimulis': 48, 'klade': 15}
    >>> print(soma['klade'])
    15
    >>> soma['klade'] = soma['klade'] + 3
    >>> print(soma)
    {'graamata': 1, 'ziimulis': 48, 'klade': 18}


Indekss ir dotais vārds un cipari ir dati.


**"list()"** -  strādā kā vārdnīca, bet neizmanto vārdus indeksācijai, bet gan ciparus. Strādā kā masīvs.


    >>> nums.append(42)
    >>> nums append(137)
    >>> nums.append(137)
    >>> print(nums)
    [42, 137]
    >>> nums[0] = 212
    >>> print(nums)
    [212, 137]


**"open()"** -  atver pieprasīto failu, lai to lietotu programmā. Izveido "atslēgu", ar kuru piekļūst šim failam.


Piemēra programma saskaita līniju skaitu tekstā un izprintē rindas, kas sākas ar "pi".


    key = open("teksts.txt")
    n = 0
    for line in key:
        n = n + 1
        if line.startswith("pi"):
            print(line)
    print(n)


Programmas rezultāts:


    piens
    
    piens
    
    11
    >>> 


Lai izvairītos no atstarpēm, izmanto ".rstrip" vai ".lstrip".


    ...
    for line in key:
        line = line.rstrip()
        if ...
    ...



Python nav pilnīgi visa vajadzīga. Ja vēlas lietot funkcijas, kuras atbalsta Python, bet nav pieejams noklusējuma bibliotēkā, izmanto **"import"** funkciju.


Ar "import" tiek importētas dažādas bibliotēkas. Šī funkcija ļauj importēt visu bibliotēku vai arī noteiktu komandu vai komandas. Šīs komandas nosaukumu var saglabāt, kāds ir, vai nodēvēt pēc savas izvēles.


    from matplotlib import pyplot as plt


Ar šo darbību tiek importēta grafika zīmēšanas komanda "pyplot" un tiek nodēvēta par "plt" atmiņas taupīšanas un programmētāja laika taupīšanas nolūkos.


Ir daudz un dažādu bibliotēku.


Daži piemēri - time, math, numpy, sys, matplotlib.


Math un numpy bibliotēkā ir atrodoamas komandas, kas aprēķina dažādas matemātiskās darbības. Bieži lieto trigonometrisko funckiju aprēķinu veikšanai (piemēram, cos(x) vai sinh(x) ) 



