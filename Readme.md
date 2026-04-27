<!-- HEADER_START: {"lang": "de"} -->


Dokumentation  

# Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen

<br> 
<br> 
<br> 

[**Stefan Meisegeier**](https://orcid.org/0000-0003-2347-1836)&sup1;, [**Maren Imhoff**](https://orcid.org/0009-0001-0030-566X)&sup1;, **Karsten Berg**&sup1;, & [**Klaus Kraywinkel**](https://orcid.org/0000-0002-9250-6003)&sup1;

<br> 



&emsp;&emsp;&sup1; [Robert Koch-Institut](https://www.rki.de/) | [ZfKD - Zentrum für Krebsregisterdaten](https://www.krebsdaten.de/)

<br> 

**Zitieren**  
<!-- CITATION_START: {"citation_style": "apa"} -->  
Meisegeier, S., Imhoff, M., Berg, K., & Kraywinkel, K. (2024). Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.10022040](https://doi.org/10.5281/zenodo.10022040)
<!-- CITATION_END -->

<br>

---

E-Mail-Adresse für Rückmeldungen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)  

---


<br>

**Zusammenfassung**    
In diesem Strukturdatensatz werden begleitende Informationen zu Struktur und Klassifikationen des bundesweiten Datensatzes des Zentrums für Krebsregisterdaten (ZfKD) am Robert Koch-Institut sowie Beispieldaten bereitgestellt. Dieser klinische Krebsregisterdatensatz ist nicht öffentlich zugänglich, kann jedoch auf Antrag für wissenschaftliche Forschung bereitgestellt werden. Er enthält Daten zu neu auftretenden Krebsfällen, die von medizinischen Einrichtungen an die Krebsregister der Bundesländer gemeldet und von dort an das ZfKD übermittelt werden. Die Datenerfassung basiert auf dem Bundeskrebsregisterdatengesetz sowie den entsprechenden Landesgesetze.

<br>

**Inhaltsverzeichnis**  

<!-- TOC_START: {"heading_depth": 2} -->
  - [Einleitung](#einleitung)  
  - [Informationen zum Entstehungskontext des ZfKD-Datensatzes](#informationen-zum-entstehungskontext-des-zfkd-datensatzes)  
  - [Struktur des bundesweiten klinischen Krebsregisterdatensatzes](#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes)  
  - [Hinweise zur Nachnutzung der Daten](#hinweise-zur-nachnutzung-der-daten)  
<!-- TOC_END -->

<br>

<!-- HEADER_END -->

## Einleitung

Die Krebsregistrierung in Deutschland erfolgt auf der Basis von Landesgesetzen. Diese verpflichten medizinische Einrichtungen (v. a. niedergelassene Ärztinnen und Ärzte, pathologische Institute, Kliniken, Screening-Einheiten), neu auftretende Krebsfälle und definierte Ereignisse im Krankheits- bzw. Behandlungsverlauf an das zuständige Krebsregister zu melden.

Die Krebsregister der Bundesländer wiederum übermitteln nach Vorgabe des [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) einmal jährlich Angaben zu neu erfassten Erkrankungsfällen an das Zentrum für Krebsregisterdaten (ZfKD) am Robert Koch-Institut. Das ZfKD prüft die Qualität der Daten, führt sie zu einem bundesweiten Datensatz zusammen und stellt sie [auf Antrag für wissenschaftliche Forschungsprojekte](https://www.krebsdaten.de/info_antrag) zur Verfügung.

In diesem Repository werden begleitende Informationen zur [**Struktur**](#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes) des bundesweiten ZfKD-Datensatzes bereitgestellt. Ein weiteres wesentliches Element der Krebsregisterdaten stellen [**Klassifikationen**](#klassifikationen) dar - Referenztabellen für Variablen des Datensatzes und ihre definierten Ausprägungen. Diese Tabellen werden durch beteiligte Akteure kontinuierlich harmonisiert. 

> [!NOTE]
> Der ZfKD-Datensatz ist nicht öffentlich zugänglich, kann aber auf Antrag für wissenschaftliche Forschungszwecke genutzt werden. Bitte verwenden Sie für Fragen zur Antragstellung die  E-Mail-Adresse des ZfKD: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)  oder das auf der Internetseite des ZfKD bereitgestellte [Kontaktformular](https://www.krebsdaten.de/SharedDocs/Kontaktformulare/A/Antrag-krebsdaten/Integrator_SCU.html). Informationen zum gesetzlichen Auftrag, zu Methoden und Veröffentlichungen des ZfKD erhalten Sie ebenfalls auf den [Internetseiten des ZfKD](https://www.krebsdaten.de/). Bitte beachten Sie, dass das ZfKD an den Daten, die von den Krebsregistern übermittelt wurden, keine Änderungen vornimmt.

## Informationen zum Entstehungskontext des ZfKD-Datensatzes

Für die Erhebung klinischer Krebsregisterdaten wurde mit dem [Krebsfrüherkennungs- und -registergesetz (KFRG)](https://www.bgbl.de/xaver/bgbl/start.xav?start=//*%5B@attr_id=%27bgbl113s0617.pdf%27%5D#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl113s0617.pdf%27%5D__1697181091765) im [§ 65c Fünftes Buch Sozialgesetzbuch (SGB V)](https://www.gesetze-im-internet.de/sgb_5/__65c.html) ein bundesrechtlicher Rahmen geschaffen. Die von den klinischen Krebsregistern zu erfassenden Angaben werden in dem von der Arbeitsgemeinschaft Deutscher Tumorzentren (ADT) und der Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID, jetzt DKR e.V.) erarbeiteten [onkologischen Basisdatensatz (oBDS)](https://basisdatensatz.de/) spezifiziert und regelmäßig überarbeitet. Die letzte Anpassung des oBDS wurde am 12. Juli 2021 [im Bundesanzeiger publiziert](https://www.bundesanzeiger.de/pub/publication/bRrUsRox5lQ14casCXs/content/bRrUsRox5lQ14casCXs/BAnz%20AT%2012.07.2021%20B4.pdf). Einmal jährlich übermitteln die Krebsregister Daten nach Maßgabe des [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) an das ZfKD.

Seit der Novellierung des BKRG durch das [Gesetz zur Zusammenführung von Krebsregisterdaten](https://www.bgbl.de/xaver/bgbl/start.xav#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl121s3890.pdf%27%5D__1697190045694) enthalten die ans ZfKD übermittelten Daten auch klinische Angaben, u. a. zum Krankheitsverlauf und zur Behandlung (ab Diagnosejahr 2020).

Die Inhalte und die Struktur der ans ZfKD zu übermittelnden Daten wurden in einer AG mit Vertretern des ZfKD und der Krebsregister abgestimmt, dabei diente der oBDS und das novellierte Bundeskrebsregisterdatengesetz (§ 5) als Arbeitsgrundlage.

Das Arbeitsergebnis ist das hier beschriebene, für die Datenübermittlung ans ZfKD zu verwendende XML-Schema (alternativ als oBDS-RKI oder ZfKD-Lieferdatensatz bezeichnet, siehe dazu [Struktur des bundesweiten klinischen Krebsregisterdatensatzes](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes)).

Umfassende Informationen zur Krebsregistrierung sind hier verfügbar: [Manual der klinischen und epidemiologischen Krebsregistrierung](https://www.dkr.de/manual-der-krebsregistrierung) (Veröffentlichung 2018)

### Administrative und organisatorische Angaben

Das [Zentrum für Krebsregisterdaten (ZfKD)](https://www.krebsdaten.de/) des RKI ist zuständig für die bundesweite Krebsberichterstattung und stellt Dritten auf Antrag Daten für überregionale Forschungsprojekte zur Verfügung. Es prüft die Qualität der von den Krebsregistern übermittelten Daten und gibt den Krebsregistern diesbezüglich Rückmeldung.  

Inhaltliche Fragen zur Datenerhebung, Datenauswertung und Datenkuration können direkt an das ZfKD gestellt werden (E-Mail-Adresse für Anfragen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)).

### Datenübermittlung an das ZfKD  

Das 2009 verabschiedete BKRG regelt die jährliche Zusammenführung der wesentlichen Daten aus den Krebsregistern am ZfKD. Die Übermittlung erfolgt jeweils am Jahresende und enthält Informationen zu allen Fällen, die bis zum Ende des vorherigen Kalenderjahres diagnostiziert wurden, so dass auch Nachmeldungen und Korrekturen sowie Informationen zum Follow-up (z. B. Sterbefälle und Wegzüge) früherer Erkrankungsfälle enthalten sind.

Vor der Novellierung des BKRG in 2021 wurde lediglich der deutlich kleinere epidemiologische Datensatz (mit Angaben zur Diagnose und zum Sterbezeitpunkt) an das ZfKD übermittelt. Dieser Datensatz wird bundesweit seit 2009 erfasst. Die Mehrzahl der Bundesländer hat zwischen 1998 und 2007 mit der landesweiten Erfassung begonnen.

Seit der Datenlieferung zum 31. Dezember 2022 und rückwirkend ab dem Diagnosejahr 2020 liefern die Krebsregister [auch klinische Angaben](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#informationen-zum-entstehungskontext-des-zfkd-datensatzes). Die am ZfKD vorliegenden Daten enthalten allerdings nicht den gesamten Datenbestand der Register, beispielsweise sind keine Angaben zu den behandelnden Einrichtungen verfügbar.

Außerdem sind die Daten in den Krebsregistern bearbeitet worden: So wurden Meldungen aus verschiedenen Quellen zum gleichen Erkrankungsfall zusammengeführt und weitgehend um Widersprüche bereinigt ("best-of"). Der Datensatz des ZfKD ist daher fall- und nicht meldungsbasiert, mehrere Tumorerkrankungen derselben Person können anhand einer von den Registern einmal vergebenen Personidentifikationsnummer zugeordnet werden. Die Übermittlung der Daten an das ZfKD erfolgt nach dem Wohnortprinzip (zum Zeitpunkt der Diagnose), so dass Doppelmeldungen weitgehend ausgeschlossen sind. Zwischen den Bundesländern erfolgt ein regelmäßiger Austausch von Daten, die außerhalb des Wohnortbundeslandes der Erkrankten erhoben und zunächst an das Krebsregister des Behandlungsortes gemeldet wurden.

> 💡 Eine fallweise Verknüpfung (Record Linkage) der am ZfKD vorliegenden Daten mit externen Datensätzen (Studien, Krankenkassen) ist nicht möglich.

## Struktur des bundesweiten klinischen Krebsregisterdatensatzes  

Der klinische Datensatz wird als `oBDS-RKI` bezeichnet. Die Bezeichnung geht zurück auf den zwischen ADT, GEKID und Plattform § 65c abgestimmten `einheitlichen onkologischen Basisdatensatz` (`oBDS`), der für die Entwicklung des `oBDS-RKI` als Vorlage und Arbeitsgrundlage diente (siehe [Informationen zum Datensatz und Entstehungskontext](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#informationen-zum-entstehungskontext-des-zfkd-datensatzes)).

Weil er die Struktur und Inhalte der von den Landeskrebsregistern ans ZfKD zu liefernden Daten definiert, wird der `oBDS-RKI` auch als `ZfKD-Lieferdatensatz` bezeichnet.

### Datenschema

Das Datenschema umfasst mehr als 120 Variablen, die verschiedenen Elementen zugeordnet sind. Die klinischen Daten können nicht in einer einfachen "Rechtecktabelle" wiedergegeben werden, da sie zum Teil komplexe Krankheitsverläufe abbilden. Im klinischen Datensatz sind die Daten daher in einem verschachtelten XML-Schema strukturiert.  

Der klinische Datensatz wird durch folgende Elemente gegliedert:

- Die _Person_ bildet die grundlegende Einheit im Datensatz.
- Der Person zugeordnet ist mindestens ein Element _Tumor_.
- Das Element _Tumor_ enthält ein verpflichtendes Element _Primärdiagnose_. Dieses enthält u. a. Angaben zum Tumorstadium, zur Histologie und Lokalisation des Tumors.
- Darüber hinaus sind dem Element _Tumor_ mehrere optionale Elemente zugeordnet, in denen Angaben zur Behandlung (Elemente _OP_, _ST_ und _SYST_) und zu Folgeereignissen (Element _Folgeereignis_) wie Remissionen und Rezidiven erfasst werden können.

Bestimmte Variablen sind Pflichtangaben, z. B. das _Geburtsdatum_, der _Inzidenzort_ und der _Diagnoseschlüssel_. Viele Angaben sind optional, z. B. die den Elementen cTNM und pTNM zugeordneten Variablen (_T-Kategorie_, _UICC-Stadium_, _m-Suffix_ usw.). Einige Angaben sind nur unter der Bedingung verpflichtend, dass das übergeordnete, optionale Element verwendet wird: Beispielsweise ist das Element Histologie optional. Wird jedoch in der zugehörigen Variable _Morphologie_ ein Eintrag vorgenommen, ist auch eine Angabe zum _Grading_ verpflichtend. Angaben zur Zahl untersuchter Lymphknoten bleiben optional.

Bei Auswertungen ist zu beachten, dass optionale Inhalte möglicherweise nicht gleichermaßen aus allen Bundesländern vorliegen.

Die Elemente _Primärdiagnose_, _Folgeereignis_, _OP_, _ST_ und _SYST_ können mehrfach verwendet werden, so dass auch komplexe Krankheitsverläufe abgebildet werden können. Die Inhalte eines Elements können in ein tabellarisches Format überführt und über eine fallbezogene Nummer mit anderen Tabellen aus dem Datensatz verknüpft werden. Auf diese Weise entsteht ein auswertbares Format, in dem die bewilligten Daten an den Datenempfänger übermittelt werden können..  

![Abbildung: Vereinfachtes Datenschema (mit ausgewählten Variablen). Quelle: [krebsdaten.de](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdaten/Informationen_datensatz/klinischer_datensatz/klinischer_datensatz_node.html).](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/.github/images/2023-06-30_Datenschema_einfach.png?raw=true)  

Im Folgenden sind die Variablen des Datensatzes aufgeführt, gruppiert nach Elementen.

#### Person

| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Geschlecht <br>`text`	| Geschlecht der erkrankten Person. |M = männlich <br> W = weiblich <br> D = divers <br> X = keine Angabe/unbestimmt <br> U = unbekannt |
| Geburtsdatum_Genauigkeit <br> `text` | 	Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. | M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Geburtsdatum <br> `date`	| Geburtsdatum der erkrankten Person im internationalen Datumsformat YYYY-MM-DD. |	Datum YYYY-MM-DD |
| Verstorben <br> `text` | Vitalstatus: Gibt an, ob die erkrankte Person verstorben ist (Ja/Nein).	| J = Ja <br> N = Nein |
| Datum_Vitalstatus_Genauigkeit <br> `text`| Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. | M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Datum_Vitalstatus <br> `date` | Wenn Verstorben = Nein, gibt diese Variable das Datum der letzten Erhebung des Vitalstatus an. Wenn Verstorben = Ja, gibt diese Variable das imputierte Sterbedatum an. Bei DCO-Fällen werden Sterbe- und Diagnosedatum gleichgesetzt. | Datum YYYY-MM-DD |

#### Todesursachen

| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| IsGrundleiden <br> `text`	| Angabe, ob die kodierte Todesursache als amtliches Grundleiden laut Todesbescheinigung bzw. wie vom statistischen Landesamt übermittelt wurde. | J = Ja <br> N = Nein |
| Code <br> `text`|	Zusätzliche, im Register vorliegende Todesursache(n), kodiert nach ICD-10. |	ICD-10-Code |
| Version <br> `text`| Für die Kodierung zusätzlicher Todesursachen verwendete Ausgabe der ICD-10.	| ICD-10-Ausgabe |

#### Primärdiagnose

| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Diagnosedatum_Genauigkeit <br> `text` | Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. | M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Diagnosedatum <br> `date`|  Datum der Erstdiagnose im internationalen Datumsformat YYYY-MM-DD. Erstdiagnosejahr und -monat werden von den Registern an das ZfKD übermittelt. Der Tag der Erstdiagnose wird von den Registern nicht übermittelt, er wird nachträglich auf einen willkürlichen Wert festgelegt. Bei DCO-Fällen werden Sterbe- und Diagnosedatum gleichgesetzt. | 	Datum YYYY-MM-DD | 
| Diagnosejahr <br> `date`| Jahr der Erstdiagnose. Bei DCO-Fällen werden Sterbe- und Diagnosejahr gleichgesetzt.	| Datum YYYY |
| Diagnosealter <br> `int` | Ganzzahliger Abstand in Jahren zwischen Geburt und Erstdiagnose.	|Alter (Jahre) |
| Inzidenzort <br> `text`	| Ziffern 1-5 des amtlichen Gemeindeschlüssels des Wohnortes der erkrankten Person zum Zeitpunkt der Erstdiagnose.	| Kreiskennziffer, 5-stellig |
| Diagnose_ICD10_Code <br> `text`|	Tumordiagnose nach ICD-10.	| ICD-10-Kode, 4-stellig |
| Diagnose_ICD10_Version <br> `text`| Diagnose, ICD-Version |	Für die Kodierung der Tumordiagnose verwendete Ausgabe der ICD-10.	| ICD-10-Version |
| Topographie_Code <br> `text` | Kodierung der Tumorlokalisation nach ICD-O-3. |	ICD-O-3-Kode (Kapitel T), 4-stellig |
| Topographie_Version <br> `int` |	Für die Kodierung der Topographie verwendete Ausgabe der ICD-O-3. |	31 = ICD-O-3, 2003 <br> 32 = ICD-O-3, 1. Revision 2014 <br> 33 = ICD-O-3, 2. Revision 2019|
| Morphologie_Code <br> `text`| Kodierung des Histologiebefunds nach ICD-O-3. Die fünfte Stelle des Kodes bezeichnet das biologische Verhalten des Tumors (/0 Gutartig<br> /1 Unsicher<br> /2 Carcinoma in situ<br> /3 Bösartig, Primärtumor). | ICD-O-3-Kode (Kapitel M), 5-stellig|
| Morphologie_Version <br> `text`| Für die Kodierung der Morphologie verwendete Referenz (ICD-O-3, WHO Blue Books). | 31 = ICD-O-3, 2003 <br> 32 = ICD-O-3, 1. Revision 2014 <br> 33 = ICD-O-3, 2. Revision 2019 <br> bb = WHO Blue Books |
| Grading <br> `text`	|	Differenzierungsgrad des Tumors gemäß "WHO Classification of Tumours".	| 0 = Malignes Melanom der Konjunktiva <br> 1 = Gut differenziert <br> 2 = Mäßig differenziert <br> 3 = Schlecht differenziert <br> 4 = Undifferenziert <br> X = Nicht bestimmbar <br> L = Low grade (G1 oder G2) <br> M = Intermediate (G2 oder G3) <br> H = High grade (G3 oder G4) <br> B = Borderline <br> U = Unbekannt <br> T = Trifft nicht zu |
| LK_untersucht <br> `int` |	Anzahl der untersuchten Lymphknoten.|(n) = Anzahl Lymphknoten |
| LK_befallen <br> `int` | Anzahl der befallenen Lymphknoten.| (n) = Anzahl Lymphknoten | 
| Sentinel_LK_untersucht <br> `int`|	Anzahl der untersuchten Lymphknoten, davon Sentinel	| (n) = Anzahl Lymphknoten |
| Sentinel_LK_befallen	<br> `int`| Anzahl der befallenen Lymphknoten, davon Sentinel |	(n) = Anzahl Lymphknoten|
| TNM_Auflage_c <br> `text`| Ausgabe der TNM, die für die Beurteilung des klinischen Tumorstadiums verwendet wurde. | 6 = 6. Auflage TNM <br> 7 = 7. Auflage TNM <br> 8 = 8. Auflage TNM <br> 9 = 9. Auflage TNM |
| y_Symbol_c <br> `text` | Gibt an, ob das klinische Tumorstadium vor oder nach/während der initialen multimodalen Therapie beurteilt wurde. | y = klinische Klassifikation erfolgte nach einer initialen multimodalen Therapie <br> (leer) = klinische Klassifikation erfolgte vor einer initialen multimodalen Therapie oder es hat keine initiale multimodale Therapie stattgefunden | 
| r_Symbol_c <br> `text` | Gibt an, ob das klinische Tumorstadium eines Rezidivs beurteilt wurde.	| r = klinische Klassifikation erfolgte zur Beurteilung eines Rezidivs <br> (leer) = klinische Klassifikation erfolgte vor Eintreten eines Rezidivs |
| a_Symbol_c <br> `text`| Gibt an, ob das Tumorstadium mittels Autopsie bestimmt wurde. | a = Klassifikation erfolgte durch Autopsie <br> (leer) = Klassifikation erfolgte klinisch oder pathologisch |
| T_c <br> `text`| Beschreibt die Ausdehnung des Primärtumors. | Klassifikation nach TNM entsprechend Tumorentität.	| T-Stadium, entitätsspezifisch |
| N_c	<br> `text`| Beschreibt das Ausmaß regionärer Lymphknotenmetastasen. | Klassifikation nach TNM entsprechend Tumorentität.	| N-Stadium, entitätsspezifisch |
| M_c	<br> `text`| Beschreibt das Vorliegen von Fernmetastasen. | Klassifikation nach TNM |M-Stadium, teilweise entitätsspezifisch <br> M0 = keine Fernmetastasen <br> M1 = Fernmetastasen |
| c_p_u_Praefix_T_c <br> `text`	| Gibt an, ob das T-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.| c = T-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = T-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = T-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| c_p_u_Praefix_N_c <br> `text`	| Gibt an, ob das N-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	| c = N-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = N-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = N-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| c_p_u_Praefix_M_c <br> `text`	| Gibt an, ob das M-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	| c = M-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = M-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = M-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| m_Symbol_c <br> `text` | Kennzeichnet Vorhandensein multipler Primärtumoren in einem anatomischen Bezirk. | m = multiple Tumoren ohne Angabe der Zahl <br> (n) = Anzahl der multiplen Tumoren <br> (leer) = keine multiplen Tumoren |
| L_c <br> `text`	| Beschreibt das Ausmaß der Lymphgefäßinvasion. Wird im Allgemeinen im Rahmen eines pTNM festgestellt. | LX = Lymphgefäßinvasion kann nicht beurteilt werden <br> L0 = keine Lymphgefäßinvasion <br> L1 = Lymphgefäßinvasion |
| V_c <br> `text` |	Beschreibt das Ausmaß der Veneninvasion. Wird im Allgemeinen im Rahmen eines pTNM festgestellt.	| VX = Veneninvasion kann nicht beurteilt werden <br> V0 = keine Veneninvasion <br> V1 = mikroskopische Veneninvasion <br> V2 = makroskopische Veneninvasion |
| Pn_c <br> `text`| Beschreibt das Ausmaß der Perineuralinvasion. Wird im Allgemeinen im Rahmen eines pTNM festgestellt. | PnX = perineurale Invasion kann nicht beurteilt werden <br> Pn0 = keine perineurale Invasion <br> Pn1 = perineurale Invasion |
| S_c <br> `text`| Bei Vorliegen eines Hodentumors: Beschreibt die Erhöhung von Serumtumormarkern (AFP, HCG, LDH). S1-S3: Schwellenwerte siehe TNM |SX = Werte der Serumtumormarker nicht verfügbar oder entsprechende Untersuchungen nicht vorgenommen <br> S0 = Serumtumormarker innerhalb der normalen Grenzen <br> S1-S3 = Serumtumormarker erhöht |
| UICC_Stadium_c <br> `text` | UICC-Stadium nach TNM-Klassifikation. Beschreibt die anatomische Ausdehnung der Tumorerkrankung. |	UICC-Stadium, entitätsspezifisch |
| TNM_Auflage_p	<br> `text`|	Ausgabe der TNM, die für die Beurteilung des pathologischen Tumorstadiums verwendet wurde.	| 6 = 6. Auflage TNM <br> 7 = 7. Auflage TNM <br> 8 = 8. Auflage TNM |
| y_Symbol_p <br> `text` | Gibt an, ob das pathologische Tumorstadium vor oder nach/während der initialen multimodalen Therapie beurteilt wurde. |	y = Klassifikation erfolgte nach einer initialen multimodalen Therapie <br> (leer) = Klassifikation erfolgte vor einer initialen multimodalen Therapie oder es hat keine initiale multimodale Therapie stattgefunden |
| r_Symbol_p <br> `text`|	Gibt an, ob das pathologische Tumorstadium eines Rezidivs beurteilt wurde.	| r = Klassifikation erfolgte zur Beurteilung eines Rezidivs <br> (leer) = „native“ Klassifikation vor Eintreten eines Rezidivs |
| a_Symbol_p <br> `text`| Gibt an, ob das pathologische Tumorstadium durch Autopsie festgestellt wurde. | a = Klassifikation erfolgte durch Autopsie <br> (leer) = Klassifikation erfolgte klinisch und/oder pathologisch |
| T_p <br> `text`|	Beschreibt die Ausdehnung des Primärtumors. Klassifikation nach TNM entsprechend Tumorentität. |	T-Stadium, entitätsspezifisch |
| N_p <br> `text`| Beschreibt das Ausmaß regionärer Lymphknotenmetastasen. Klassifikation nach TNM entsprechend Tumorentität. |	N-Stadium, entitätsspezifisch |
| M_p <br> `text` |	Beschreibt das Vorliegen von Fernmetastasen. Klassifikation nach TNM.	| M-Stadium, teilweise entitätsspezifisch <br> M0 = keine Fernmetastasen <br> M1 = Fernmetastasen |
| c_p_u_Praefix_T_p <br> `text` | Gibt an, ob das T-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	|  c = T-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = T-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = T-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| c_p_u_Praefix_N_p <br> `text` | Gibt an, ob das N-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde. | c = N-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = N-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = N-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| c_p_u_Praefix_M_p <br> `text` |	Gibt an, ob das M-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	| c = M-Stadium wurde durch klinische Angaben festgestellt oder erfüllt nicht die Kriterien für "p" <br> p = M-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = M-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| m_Symbol_p <br> `text` | Kennzeichnet Vorhandensein multipler Primärtumoren in einem anatomischen Bezirk. |	m = multiple Tumoren ohne Angabe der Zahl <br> (n) = Anzahl der multiplen Tumoren <br> (leer) = keine multiplen Tumoren |
| L_p <br> `text` | Beschreibt das Ausmaß der Lymphgefäßinvasion. | LX = Lymphgefäßinvasion kann nicht beurteilt werden <br> L0 = keine Lymphgefäßinvasion <br> L1 = Lymphgefäßinvasion |
| V_p <br> `text`	| Beschreibt das Ausmaß der Veneninvasion. | VX = Veneninvasion kann nicht beurteilt werden <br> V0 = keine Veneninvasion <br> V1 = mikroskopische Veneninvasion <br> V2 = makroskopische Veneninvasion |
| Pn_p <br> `text` | Beschreibt das Ausmaß der Perineuralinvasion. |	PnX = perineurale Invasion kann nicht beurteilt werden <br> Pn0 = keine perineurale Invasion <br> Pn1 = perineurale Invasion |
| S_p <br> `text` | Bei Vorliegen eines Hodentumors: Beschreibt die Erhöhung von Serumtumormarkern (AFP, HCG, LDH). S1-S3: Schwellenwerte siehe TNM. | SX = Werte der Serumtumormarker nicht verfügbar oder entsprechende Untersuchungen nicht vorgenommen <br> S0 = Serumtumormarker innerhalb der normalen Grenzen <br> S1-S3 = Serumtumormarker erhöht |
| UICC_Stadium_p <br> `text`| UICC-Stadium nach TNM-Klassifikation. Beschreibt die anatomische Ausdehnung der Tumorerkrankung.	| UICC-Stadium, entitätsspezifisch |
| Lokalisation <br> `text` | Beschreibt die Lokalisation der Fernmetastase (n). |	PUL = Lunge <br> OSS = Knochen <br> HEP = Leber <br> BRA = Hirn <br> LYM = Lymphknoten <br> MAR = Knochenmark <br> PLE = Pleura <br> PER = Peritoneum <br> ADR = Nebennieren <br> SKI = Haut <br> OTH = Andere Organe <br> GEN = Generalisierte Metastasierung |
| Name <br> `text` |	Name/Typ sonstiger verwendeter Klassifikationssysteme.	| (Name, Typ) = Bezeichnung des Klassifikationssystems, z. B. Ann-Arbor-Klassifikation, WHO Classification of CNS Tumors, AJCC |
| Stadium	<br> `text`| weitere Klassifikation: Stadium (Ausprägung)	| Einstufung/Stadium nach sonstigem verwendeten Klassifikationssystem. |	(Stadium) = Stadium gemäß verwendetem Klassifikationssystem |
| Diagnosesicherung <br>`text`|	Wertigkeit der Diagnosesicherung.	| 0 = DCO <br> 1 = klinisch, ausschließlich körperliche Untersuchung (ohne tumorspezifische Diagnostik) <br> 2 = klinisch, inkl. Bildgebung, Endoskopie, Laparatomie, Autopsie (ohne histopathologische Untersuchung) <br> 4 = spezifische Tumormarker <br> 5 = zytologisch <br> 7.1 = Histologie des Primärtumors <br> 7.2 = Histologie einer Metastase <br> 7.3 = Histologie der Autopsie <br> 8 = zytogenetisch und/oder molekularer Test <br> 9 = unbekannt|
| Seitenlokalisation <br> `text`| Bei paarigen Organen: Gibt an, welche Körperseite betroffen ist. |	L = links <br> R = rechts <br> B = beidseitig <br> M = mittig <br> U = unbekannt <br> T = trifft nicht zu (z. B. bei Systemerkrankung) |
| DCN <br> `text`	| Gibt an, ob die Quelle der ersten Information über einen Erkrankungsfall im Register eine Todesbescheinigung bzw. eine amtlich übermittelte Todesursache war. |	J = Ja <br> N = Nein |

#### Primärdiagnose: Modul Mamma
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Anzahl_Tage_Diagnose_Tod <br> `int`	| Zeitlicher Abstand zwischen Diagnose und Tod (in Tagen).	| (n) = Anzahl Tage |
| TumorgroesseInvasiv <br> `int`	| Maximaler Durchmesser des invasiven Karzinoms (in mm).	| (n) = Tumorgröße in mm |
| TumorgroesseDCIS <br> `int` | Maximaler Durchmesser des duktalen in situ-Karzinoms (in mm).	| (n) = DCIS-Größe in mm |
| Praetherapeutischer_Menopausenstatus <br> `text` |	Prätherapeutischer Menopausenstatus der Patientin. Postmenopausal bedeutet: entweder a) keine Menstruationsblutung für länger als ein Jahr oder b) E2 und FSH im eindeutigen postmenopausalen Bereich. |	1 = prämenopausal (umfasst perimenopausal) <br> 3 = postmenopausal <br> U = unbekannt |
| HormonrezeptorStatus_Oestrogen <br> `text` | Östrogenrezeptorstatus gemäß Immunreaktivem Score (IRS).|	P = Positiv (IRS >= 1) <br> N = Negativ <br> U = Unbekannt |
| HormonrezeptorStatus_Progesteron <br> `text` |	Progesteronrezeptorstatus gemäß Immunreaktivem Score (IRS). | P = Positiv (IRS >= 1) <br> N = Negativ <br> U = Unbekannt |
| Her2neuStatus <br> `text`	| HER2 (ERBB2)-Status | P = Positiv (ICH+++ oder: ICH++ und ISH positiv) <br> N = Negativ <br> U = Unbekannt |

### Primärdiagnose: Modul Prostata
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| PSA <br> `float`	| Aktuell relevanter PSA-Wert (in ng/mL). |	(n) = Wert in ng/mL |
| DatumPSA_Genauigkeit <br> `text` |	Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt.	| M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| DatumPSA <br> `date` |	Monat und Jahr der PSA-Wert-Bestimmung. |	Datum YYYY-MM-DD |
| GradPrimaer <br> `int` |	 Primärer Gleason-Grad.	| 1, 2, 3, 4 oder 5 |
| GradSekundaer <br> `int` |	Sekundärer Gleason-Grad. |	1, 2, 3, 4 oder 5 |
| ScoreErgebnis <br> `text`	| Gleason-Score.	| 2, 3, 4, 5, 6, 7, 7a, 7b, 8, 9 oder 10 |
| AnlassGleasonScore <br> `text` |	Anlass der Bestimmung. |	O = OP <br> S = Stanzbiopsie <br> U = Unbekannt |

#### Primärdiagnose: Modul Melanom
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Tumordicke <br> `float` |	Tumordicke (in mm).	| (n) = Dicke in mm |
| Ulzeration <br> `text`|	Gibt an, ob Ulzeration (Geschwürbildung) vorliegt. |	J = Ja <br> N = Nein |
| LDH <br> `int` |	LDH-Wert (in Units pro Liter). | (n) = Wert in U/L |

#### Primärdiagnose: Modul Darm
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| RektumAbstandAnokutanlinie <br> `int` |Bei Rektumkarzinom: Beschreibt den Abstand des Tumorunterrandes von der Anokutanlinie (in cm). | (n) = Abstand zur Anokutanlinie in cm <br> U = unbekannt |
| RASMutation <br> `text` |	Gibt an, ob eine Mutation im K-ras-Onkogen vorliegt. | W = Wildtyp  <br> M = Mutation <br> U = Unbekannt <br> N = Nicht untersucht |

#### Operation
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Datum_OP_Genauigkeit <br> `text` |	Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. | M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Datum_OP <br> `date`| Operationsdatum.	| Datum YYYY-MM-DD |
| Code <br> `text`	| Art der Operation nach Operationen- und Prozedurenschlüssel (OPS). |	OPS-Kode |
| Version <br> `text`| Verwendete Ausgabe des OPS. |	OPS-Version |
| Intention <br> `text` |	Gibt an, mit welchem Ziel die Operation geplant wurde. Die Angabe S = Sonstiges wird bspw. bei Tracheostomie vor Radiochemotherapie bei Kopf/Hals verwendet.| K = kurativ <br> P = palliativ <br> D = diagnostisch <br> R = Revision/Komplikation <br> S = Sonstiges <br> x = fehlende Angabe |
| Lokale_Beurteilung_Residualstatus <br> `text` |	Bezeichnet den Residualstatus nach einer operativen Tumorentfernung, d. h. Anzeichen für im Körper des Patienten verbliebenes Resttumorgewebe. Klassifikation nach TNM. |	R0 = kein Residualtumor <br> R1 = mikroskopischer Residualtumor <br> R1(is) = in-situ-Rest <br> R1(cy+) = zytologischer Rest <br> R2 = makroskopischer Residualtumor <br> RX = Vorhandensein von Residualtumor kann nicht beurteilt werden <br> U = Residualtumorstatus ist nicht bekannt |
| Anzahl_Tage_Diagnose_OP <br> `int`| Anzahl der Tage zwischen dem Tag der Diagnose und dem Tag der Operation.|	(n) = Anzahl Tage |

#### Strahlentherapie
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Datum_Beginn_Bestrahlung_Genauigkeit <br> `text`|	Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. |	M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Datum_Beginn_Bestrahlung <br> `date`|	Monat und Jahr des Beginns der Strahlentherapie.	|Datum YYYY-MM-DD |
| Intention <br> `text` |	Gibt an, mit welcher Intention die Strahlentherapie geplant wurde. Prophylaktisch bzw. Salvage kann als "Kurativ" oder "Palliativ" kodiert werden. "Lokal kurativ" steht zwischen "Kurativ" und "Palliativ".	| K = kurativ <br> P = palliativ <br> O = lokal kurativ bei Oligometastasierung <br> S = sonstiges <br> x = keine Angabe |
| Stellung_OP <br> `text` | Gibt an, in welchem Bezug zu einer operativen Therapie die Strahlentherapie steht. "Adjuvant" gilt für Therapien nach R0-Resektion. "Additiv" gilt für Therapien nach R1/R2- und RX-Resektion. |	O = ohne Bezug zu einer operativen Therapie <br> A = adjuvant <br> N = neoadjuvant <br> I = interoperativ <br> Z = additiv <br> s = sonstiges |
| TypeOfST_TypBestrahlungApplikationsart <br> `text` |	Gibt an, mit welcher Technik die Strahlentherapie durchgeführt wurde. Die möglichen Applikationsarten enthalten untergeordnete Elemente (Details siehe XML-Schema).	| Perkutan <br> Kontakt <br> Metabolisch <br> Sonstige <br> Unbekannt |
| Radiochemo <br> `text` |	Beschreibt die Ausführung der perkutanen Radiochemotherapie (mit/ohne Sensibilisierung). |	RCJ = mit Chemotherapie/Sensitizer <br> RCN = ohne Chemotherapie/Sensitizer |
| Stereotaktisch <br> `text` |	Gibt an, ob die perkutane Strahlentherapie stereotaktisch durchgeführt wurde. |	ST = stereotaktisch |
| Atemgetriggert <br> `text` |	Gibt an, ob die perkutane Strahlentherapie atemgesteuert durchgeführt wurde.	| 4D = atemgetriggert|
| CodeVersion2014 <br> `text`|	Bezeichnet die behandelte anatomische Region. Kodierung gemäß oBDS-Version 2014. |	https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/94539aeabc532ccad47618c11488d17483ff2bf1/data/v2/Klassifikationen/zielgebiet_2014.csv | 
| CodeVersion2021 <br> `text` |	Bezeichnet die behandelte anatomische Region. Kodierung gemäß oBDS-Version 2021. |	https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/main/data/v2/Klassifikationen/zielgebiet_2021.csv?ref_type=heads | 
| Seite_Zielgebiet <br> `text` |	Bezeichnet die Körperseite der behandelten anatomischen Region. | L = links <br> R = rechts <br> B = beidseits <br> M = mittig <br> U = unbekannt <br> T = trifft nicht zu |
| Interstitiell_endokavitaer <br> `text` |	Gibt an, wie die Kontaktbestrahlung (Brachytherapie) durchgeführt wurde. |	I = interstitiell <br> K = endokavitär |
| Rate_Type	<br> `text` | Beschreibt die bei der Kontaktbestrahlung (Brachytherapie) eingesetzte Dosisleistung.	| HDR = high dose rate <br> LDR = low dose rate <br> PDR = pulsed dose rate |
| Metabolisch_Typ <br> `text` |	Bezeichnet den Typ der metabolischen Strahlentherapie.	| SIRT = selektive interne Radiotherapie <br> PRRT = Peptid-Radiorezeptor-Therapie <br> PSMA = PSMA-Therapie <br> RJT = Radiojod-Therapie <br> RIT = Radioimmun-Therapie |
| Anzahl_Tage_Bestrahlung_Dauer	<br> `int`|	Dauer der Strahlentherapie (in Tagen).	| (n) = Anzahl Tage |
| Anzahl_Tage_Diagnose_Bestrahlung <br> `int` |	Zeitlicher Abstand zwischen Diagnosedatum und Beginn der Strahlentherapie (in Tagen).	| (n) = Anzahl Tage |

#### Systemische Therapie
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Intention <br> `text` |	Gibt an, mit welcher Intention die systemische Therapie geplant wurde.	| K = kurativ <br> P = palliativ <br> S = sonstiges <br> x = keine Angabe |
| Stellung_OP	<br> `text`| 	Gibt an, in welchem Bezug zu einer operativen Therapie die systemische Therapie steht. | O = ohne Bezug zu einer operativen Therapie <br> A = adjuvant <br> N = neoadjuvant <br> I = intraoperativ <br> S = Sonstiges |
| Therapieart <br> `text`	| Gibt an, welche Art der Therapie durchgeführt wurde bzw. ob eine abwartende Strategie verfolgt wurde.  | CH = Chemotherapie <br> HO = Hormontherapie <br> IM = Immun-/Antikörpertherapie <br> ZS = zielgerichtete Substanzen <br> CI = Chemo- + Immun-/Antikörperthrapie <br> CZ = Chemotherapie + zielgerichtete Substanzen <br> CIZ = Chemo- + Immun-/Antikörpertherapie + zielgerichtete Substanzen <br> IZ = Immun-/Antikörpertherapie + zielgerichtete Substanzen <br> SZ = Stammzellentransplantation (inkl. Knochenmarktransplantation) <br> AS = Active Surveillance <br> WS = Wait and see <br> WW = Watchful Waiting <br> SO = Sonstiges|
| TypeOfSYST_TypSubstanz <br> `text` | Gibt an, mit welcher Substanz die Systemtherapie durchgeführt wurde. Mehrere Substanzen sind separat einzugeben.	| Bezeichnung oder: ATC-Kode + ATC-Version |
| TypeOfProtokoll_Typ <br> `text`	| Bezeichnung oder Kode/Kürzel des Therapieprotokolls | Bezeichnung oder: Protokollschlüssel |
| Protokoll_TypProtokollschluessel_Code <br> `text` |	Therapieprotokoll, Kode/Kürzel.	|Vorschlagsliste: https://plattform65c.atlassian.net/wiki/spaces/UMK/pages/15532519/Protokolle |
| Bezeichnung	<br> `text` | Bezeichnung des Therapieprotokolls (Freitext).	| (Protokoll) = Bezeichnung des Therapieprotokolls |
| Protokoll_TypProtokollschluessel_Version <br> `text`	| Version des Therapieprotokollkodes/-kürzels.	| (Version) = Version des verwendeten Therapieprotokolls |
| Datum_Beginn_SYST_Genauigkeit <br> `text`| 	Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt. | M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Datum_Beginn_SYST <br> `date`	|	Monat und Jahr des Beginns der systemischen Therapie.	| Datum YYYY-MM-DD |
| Anzahl_Tage_SYST_Dauer <br> `int`| Dauer der systemischen Therapie (in Tagen). |	(n) = Anzahl Tage |
| Anzahl_Tage_Diagnose_SYST <br> `int` | Zeitlicher Abstand zwischen Diagnosedatum und Beginn der systemischen Therapie (in Tagen). |	(n) = Anzahl Tage |

#### Folgeereignis
| **Technische Variable** <br> `Datentyp` | **Beschreibung** | **Ausprägungen** |
| :--- | :--- |:--- |
| Datum_Folgeereignis_Genauigkeit	<br> `text`| Gibt an, ob nur das Jahr des Datums sicher bekannt ist (M), ob Jahr und Monat sicher bekannt sind (T) bzw. ob weder Jahr noch Monat sicher bekannt sind (V). Wichtig: Die Angabe Tag wird von den Registern grundsätzlich nicht ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format Jahr-Monat-Tag vorliegt.	| M = nur das Jahr ist bekannt, der Monat wurde geschätzt (jahrgenau) <br> T = Jahr und Monat sind bekannt (monatsgenau) <br> V = Jahr und Monat wurden geschätzt |
| Datum_Folgeereignis <br> `date`	|	Datum der letzten Untersuchung zur Einschätzung des Tumorstatus.	| Datum YYYY-MM-DD |
| Version <br> `text`	|	Ausgabe der TNM, die für die Beurteilung des Tumorstadiums verwendet wurde. |6 = 6. Auflage TNM <br> 7 = 7. Auflage TNM <br> 8 = 8. Auflage TNM <br> 9 = 9. Auflage TNM |
| y_Symbol <br> `text` | Gibt an, ob das Tumorstadium vor oder nach/während der initialen multimodalen Therapie beurteilt wurde. |	y = Klassifikation erfolgte nach einer initialen multimodalen Therapie <br> (leer) = Klassifikation erfolgte vor einer initialen multimodalen Therapie oder es hat keine initiale multimodale Therapie stattgefunden |
| r_Symbol <br> `text` |	Gibt an, ob das Tumorstadium eines Rezidivs beurteilt wurde. |	r = Klassifikation erfolgte zur Beurteilung eines Rezidivs <br> (leer) = „native“ Klassifikation vor Eintreten eines Rezidivs |
| a_Symbol <br> `text`| Gibt an, ob das Tumorstadium durch Autopsie festgestellt wurde. |	a = Klassifikation erfolgte durch Autopsie <br> (leer) = Klassifikation erfolgte klinisch und/oder pathologisch |
| T <br>	`text`|	Beschreibt die Ausdehnung des Primärtumors. Klassifikation nach TNM entsprechend Tumorentität. |	T-Stadium, entitätsspezifisch |
| N	 <br> `text` | Beschreibt das Ausmaß regionärer Lymphknotenmetastasen. Klassifikation nach TNM entsprechend Tumorentität. |	N-Stadium, entitätsspezifisch |
| M	<br> `text`| Beschreibt das Vorliegen von Fernmetastasen. Klassifikation nach TNM. | M-Stadium, teilweise entitätsspezifisch <br> M0 = keine Fernmetastasen <br> M1 = Fernmetastasen |
| c_p_u_Praefix_T <br> `text`|  Gibt an, ob das T-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	| c = T-Stadium wurde durch klinische Angaben festgestellt oder erfüllt die Kriterien für "p" nicht <br> p = T-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = T-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert" |
| c_p_u_Praefix_N <br> `text` | Gibt an, ob das N-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde.	| c = N-Stadium wurde durch klinische Angaben festgestellt oder erfüllt die Kriterien für "p" nicht <br> p = N-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = N-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| c_p_u_Praefix_M <br> `text` |	Gibt an, ob das M-Stadium klinisch, histopathologisch oder mittels Ultraschall bestimmt wurde. |	c = M-Stadium wurde durch klinische Angaben festgestellt oder erfüllt die Kriterien für "p" nicht <br> p = M-Stadium wurde durch histopathologische Untersuchung festgestellt <br> u = M-Stadium wurde mittels Ultraschall festgestellt (Unterkategorie von "c") <br> (empty) =  wird als "c" interpretiert |
| m_Symbol <br> `text`| Kennzeichnet Vorhandensein multipler Primärtumoren in einem anatomischen Bezirk. | m = multiple Tumoren ohne Angabe der Zahl <br> (n) = Anzahl der multiplen Tumoren <br> (leer) = keine multiplen Tumoren |
| L <br> `text` | Beschreibt das Ausmaß der Lymphgefäßinvasion. | LX = Lymphgefäßinvasion kann nicht beurteilt werden <br> L0 = keine Lymphgefäßinvasion <br> L1 = Lymphgefäßinvasion |
| V	<br> `text`| Beschreibt das Ausmaß der Veneninvasion.	| VX = Veneninvasion kann nicht beurteilt werden <br> V0 = keine Veneninvasion <br> V1 = mikroskopische Veneninvasion <br> V2 = makroskopische Veneninvasion |
| Pn	<br> `text` |	Beschreibt das Ausmaß der Perineuralinvasion. | PnX = perineurale Invasion kann nicht beurteilt werden <br> Pn0 = keine perineurale Invasion <br> Pn1 = perineurale Invasion |
| S <br> `text`|	Bei Vorliegen eines Hodentumors: Beschreibt die Erhöhung von Serumtumormarkern (AFP, HCG, LDH). S1-S3: Schwellenwerte siehe TNM. | SX = Werte der Serumtumormarker nicht verfügbar oder entsprechende Untersuchungen nicht vorgenommen <br> S0 = Serumtumormarker innerhalb der normalen Grenzen <br> S1-S3 = Serumtumormarker erhöht |
| UICC_Stadium <br> `text` | UICC-Stadium nach TNM-Klassifikation. Beschreibt die anatomische Ausdehnung der Tumorerkrankung.	| UICC-Stadium, entitätsspezifisch |
| Name	<br> `text`| Name/Typ sonstiger verwendeter Klassifikation(en).	| z. B. Ann-Arbor-Klassifikation, WHO Classification of CNS Tumors, AJCC | 
| Stadium <br> `text`|	Stadium der verwendeten (sonstigen) Klassifikation. |	Stadium |
| Gesamtbeurteilung_Tumorstatus <br> `text`| Gesamtbeurteilung der Erkrankung unter Berücksichtigung aller Manifestationen. | V = Vollremission <br> T = Teilremission <br> K = keine Änderung <br> P = Progression <br> D = divergents Geschehen <br> B = klinische Besserung des Zustandes, Kriterien für Teilremission jedoch nicht erfüllt (minimal response, MR) <br> R = Vollremission mit residualen Auffälligkeiten <br> Y = Rezidiv <br> U = Beurteilung nicht möglich <br> X = fehlende Angaben |
| Verlauf_Lokaler_Tumorstatus <br> `text`| Beurteilung der Erkrankung im Bereich des Primärtumors. | K = kein Tumor nachweisbar <br> T = Tumorreste (Residualtumor) <br> P = Tumorreste (Residualtumor) Progress <br> N = Tumorreste (Residualtumor) No Change <br> R = Lokalrezidiv <br> F = fraglicher Befund <br> U = unbekannt <br> X = fehlende Angabe |
| Verlauf_Tumorstatus_Lymphknoten	<br> `text`|  Beurteilung der Situation im Bereich der regionären Lymphknoten.	| K = kein Lymphknotenbefall nachweisbar <br> T = bekannter Lymphknotenbefall, Residuen <br> P = bekannter Lymphknotenbefall, Progress <br> N = bekannter Lymphknotenbefall, No Change <br> R = neu aufgetretenes Lymphknotenrezidiv <br> F = fraglicher Befund <br> U = unbekannt <br> X = fehlende Angabe | 
| Verlauf_Tumorstatus_Fernmetastasen <br>	`text`| Beurteilung der Situation im Bereich der Fernmetastasen. "R" beschreibt eine Situation, in der zuvor Metastasenfreiheit bestanden hat oder durch Therapie erreicht wurde. "P" beschreibt neu hinzukommende (zu bereits bestehenden) Fernmetastasen. | K = keine Fernmetastasen nachweisbar <br> T = Fernmetastasen, Residuen <br> P = Fernmetastasen, Progress <br> N = Fernmetastasen, No Change <br> R = neu aufgetretene Fernmetastase(n) bzw. Metastasenrezidiv <br> F = fraglicher Befund <br>  U = unbekannt <br> X = fehlende Angabe |
| Lokalisation <br> `text` |	Beschreibt die Lokalisation der Fernmetastase(n).	|PUL = Lunge <br> OSS = Knochen <br> HEP = Leber <br> BRA = Hirn <br> LYM = Lymphknoten <br> MAR = Knochenmark <br> PLE = Pleura <br> PER = Peritoneum <br> ADR = Nebennieren <br> SKI = Haut <br> OTH = Andere Organe <br> GEN = Generalisierte Metastasierung |

#### Downloads

Das Datenschema wird in verschiedenen Formaten zum Download angeboten:

| Datei | Beschreibung | Download |
| :----- | :------------ | :--------: |
| XML-Schema | Die XML-Schema-Definition `.xsd` als eindeutige, vollständige und maschinenlesbare Repräsentation des gesamten Schemas mit allen Details.   | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.4_RKI_Schema.xsd) |
| TXT-Schema | Variablen und mögliche Ausprägungen in stark vereinfachter textueller Darstellung zur erleichterten Erkennung von Änderungen. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.4_RKI_Schema.txt) |
| Schema (Abbildung) | Die grafische Darstellung des XML-Schemas als `.png`. Hinweise zur Notation des XML-Schemas sind [hier](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/59015169/Legende+zur+grafischen+Notation+des+XML-Schemas) zu finden. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.4_RKI_Schema_Abbildung.png) |
| Schema (Liste) | Optisch gestaltete und "druckfreundliche" Kurzübersicht zu Variablen und möglichen Ausprägungen als `.pdf`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.4_RKI_Schema_Liste.pdf) |

#### XML-Schema des Datensatzes

Eine vollständige und maschinenlesbare Repräsentation des gesamten Datenschemas mit allen Details wird über das [XML-Schema](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.xsd) bereitgestellt.

XML (Extensible Markup Language)-Schemata definieren den erlaubten Aufbau der ihnen zugeordneten XML-Dokumente. XML ist eine Auszeichnungssprache mit definierter Struktur und Syntax. XML-Dokumente sind textbasiert und repräsentieren Daten in einer hierarchischen und strukturierten Weise. Der Hauptzweck von XML besteht darin, Daten so zu beschreiben, dass sie sowohl für Menschen als auch für Maschinen leicht verständlich und interpretierbar sind.

Ein XML-Schema, oft auch als XSD (XML Schema Definition) bezeichnet, bietet einen Rahmen zur Beschreibung der Struktur und Datentypen eines XML-Dokuments. XML-Schemata legen fest, welche Elemente und Attribute in einem XML-Dokument erscheinen können, wie diese strukturiert und organisiert sind und welche Datentypen sie enthalten können. XML-Schemata können dazu verwendet werden, um XML-Dokumente zu validieren. Hierbei wird überprüft, ob ein XML-Dokument der im Schema definierten Struktur entspricht.

Detaillierte technische Informationen zum abgestimmten XML-Schema sind auf der [Internetseite der Plattform § 65c abrufbar](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/2064400/XML-Schema) (bis Version `3.0.0.8a_RKI`).

Protokollierte Änderungen am Datenschema sind in den beigefügten [Release Notes](release-notes.md) der Versionen zu finden.

![Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes
Die obenstehende Abbildung veranschaulicht die Struktur des klinischen Datensatzes. ](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/.github/images/2023-06-28_XML-Schema_grob.png?raw=true)


### Klassifikationen

Die im Datenschema verwendeten Klassifikationen erfahren regelmäßige Änderungen. Damit die jeweiligen Arbeitsstände in automatisierten Prozessen abgerufen werden können, sind die Klassifikationen in einem eigenen, englischsprachigen [Repository](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references) zur Verfügung gestellt. Die dem Datenschema entsprechenden Referenztabellen sind im Repository unter [`docs/readme-tables.md`](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/main/docs/readme-tables.md) verfügbar.

> [https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references)

### Beispieldaten

Um die beim ZfKD beantragbaren Daten praktisch einschätzen zu können werden konforme Beispieldaten zur Verfügung gestellt, und können in Form einer [transportablen Datenbank](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-generator) abgerufen werden. Die Struktur dieser Beispieldaten ist exakt deckungsgleich mit den klinischen Krebsregisterdaten. Eine detaillierte Darstellung der dazu verwendeten [Tabellen und Relationen](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/main/docs/readme-dataset.md) erklärt, wie die Daten verknüpft werden können.

> [https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-generator](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-generator)

<!-- FOOTER_START: {"lang": "de"} -->

### Metadaten  

Zur Erhöhung der Auffindbarkeit sind die bereitgestellten Daten mit Metadaten beschrieben. Über GitHub Actions werden Metadaten an die entsprechenden Plattformen verteilt. Für jede Plattform existiert eine spezifische Metadatendatei, diese sind im Metadatenordner hinterlegt:  

> [Metadaten/](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/tree/main/Metadaten/) 

Versionierung und DOI-Vergabe erfolgt über [Zenodo.org](https://zenodo.org). Die für den Import in Zenodo bereitgestellten Metadaten sind in der [zenodo.json](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Metadaten/zenodo.json) hinterlegt. Die Dokumentation der einzelnen Metadatenvariablen ist unter [https://developers.zenodo.org/#representation](https://developers.zenodo.org/#representation) nachlesbar.
 
> [Metadaten/zenodo.json](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Metadaten/zenodo.json)  

In der zenodo.json ist neben dem Publikationsdatum (`"publication_date"`) auch der Datenstand in folgendem Format enthalten (Beispiel):  

```
  "dates": [
    {
      "start": "2023-09-11T15:00:21+02:00",
      "end": "2023-09-11T15:00:21+02:00",
      "type": "Created",
      "description": "Date when the published data was created"
    }
  ],
```    




## Hinweise zur Nachnutzung der Daten  

Offene Forschungsdaten des RKI werden auf [Zenodo.org](http://Zenodo.org/), [GitHub.com](http://GitHub.com/), [OpenCoDE](https://gitlab.opencode.de) und [Edoc.rki.de](http://Edoc.rki.de/) bereitgestellt:  

- [https://zenodo.org/communities/robertkochinstitut](https://zenodo.org/communities/robertkochinstitut)  
- [https://github.com/robert-koch-institut](https://github.com/robert-koch-institut)  
- [https://gitlab.opencode.de/robert-koch-institut](https://gitlab.opencode.de/robert-koch-institut)  
- [https://edoc.rki.de/](https://edoc.rki.de/) 


> [!NOTE]
> Darüber hinaus können die Studiendaten beim Forschungsdatenzentrum des RKI für wissenschaftliche Nachnutzungen beantragt werden.  
> [https://www.rki.de/fdz/](https://www.rki.de/fdz/) 



### Lizenz  

Der Datensatz "Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen" ist lizenziert unter der [Creative Commons Namensnennung 4.0 International Public License | CC-BY 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.de).  

Die im Datensatz bereitgestellten Daten sind, unter Bedingung der Namensnennung des Robert Koch-Instituts als Quelle, frei verfügbar. Das bedeutet, jede Person hat das Recht die Daten zu verarbeiten und zu verändern, Derivate des Datensatzes zu erstellen und sie für kommerzielle und nicht kommerzielle Zwecke zu nutzen. Weitere Informationen zur Lizenz finden sich in der [LICENSE](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/LICENSE) bzw. [LIZENZ](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/LIZENZ) Datei des Datensatzes.  
<!-- FOOTER_END -->
