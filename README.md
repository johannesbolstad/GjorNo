# GjørNo


GjørNo' er en nettside utviklet av NTNU studenter i faget Programvareutvikling. Formålet med nettsiden er å inspirere mennesker til å komme i aktivitet, særlig i en tid der mange føler på ensomhet og det er lite som skjer. På siden kan privatpersoner og orginasjoner lage en bruker og legge ut aktiviteter. Akrivitetene kan filtreres basert på gitte kriterier, og på denne måten kan GjørNo' komme med forslag til aktiviteter til brukerene.

Privatpersoner kan legge ut aktiviteter med en beskrivelse og informajson om den er ute eller inne. Orginasjoner kan legge ut mer opplysniger på sine aktiviteter, da man kan legge til dato, tidspunkt og gratis/betaling.   

## Rammeverk og programmeringspråk

Nettsiden er bygget med rammeverket django. Django benytes både til frontend og backend, og nettsiden er dermed en fullstack djanog applikasjon. Backend er skrevet med Python. Frontend er skrvert med programmerinspråkene HTML,CSS og JavaScript samt benyttet seg av det åpne kildekode-CSS-rammerverket Bootstrap. 


## Nødvendigheter for å starte nettsiden

For å starte opp nettsiden må man ha installert python. Hvis du ikke har dette installert kan du inspirerte dette [her](https://www.python.org/downloads/). Videre må man også ha installert pip, som man kan gjøre med kommandoen `pip install pip` i terminalen. Etter dette kan man installere django,  django-crispy-forms , som man gjør med terminal-kommandoenene `python -m pip install Django` , `pip install django-crispy-forms`. Asgiref, sqlparse og pytz må også lasted ned. Dette gjøres med kommandoenene `pip install asgiref`, `pip install sqlparse` og `pip install pytz`. 






## Slik kjører du nettsiden

For å kjøre nettsiden må man klone repoet lokalt på egen datamaskin. Dette kan man gjøre med denne linken `https://gitlab.stud.idi.ntnu.no/tdt4140/landsby-1/gruppe-16/gjorno.git`. Videre må man sørge for at alle nødvendigheter er installert. Deretter kan man kjøre kommandoen: `python manage.py runserver` på stedet  **gjorno/do_something** i mappehierarkiet. 


## Brukerhistorier

Nettsiden er utviklet utifra dialog med brodukteier samt disse brukerhistorierene:

*	Som en bruker ønsker jeg å kunne legge ut aktiviteter offentlig slik at andre kan bli inspirerte til å gjøre det samme
*	Som en bruker, ønsker jeg å kunne se aktiviteter, slik at jeg kan gjennomføre disse
*	Som en bruker/organisasjon ønsker jeg å kunne logge inn i egen profil, slik at jeg lett kan få oversikt over aktiviteter jeg har lagt ut
*	Som en bruker/organisasjon, ønsker jeg å kunne markere aktiviteter slik at de blir en del av en aktivitetslogg
*	Som en organisasjon ønsker jeg å kunne opprette organiserte aktiviteter slik at andre brukere kan melde seg på
*	Som en bruker ønsker jeg å kunne melde meg på aktiviteter i regi av organisasjoner slik at jeg kan se og delta på aktuelle turer
*	Som en bruker, ønsker jeg å kunne filtrere/sortere aktiviteter, slik at jeg kan finne de turene jeg har interesse for
*	Som en bruker ønsker jeg å kunne skille mellom aktiviteter lagt ut av organisasjoner og andre brukere
*	Som en admin, ønsker jeg å kunne slette, opprette og moderere aktiviteter slik at aktivitetene er kvalitetssikret
*	Som en admin ønsker jeg en statistikkside slik at jeg kan ha oversikt over hvilke aktiviteter som er mest populære



