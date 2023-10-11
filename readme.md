# Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen

**[Robert Koch-Institut | RKI](https://rki.de)**  
Nordufer 20  
13353 Berlin  

**Zentrum für Krebsregisterdaten | ZfKD**  
[Klaus Kraywinkel](https://orcid.org/0000-0002-9250-6003 "ORCiD") (Leitung ZfKD), [Stefan Meisegeier](https://orcid.org/0000-0003-2347-1836 "ORCiD") (Projektleitung), [Maren Imhoff](https://orcid.org/0009-0001-0030-566X "ORCiD") (Data Manager), Karsten Berg (Data Analyst)  

E-Mail-Adresse für Rückmeldungen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)  

---

**Zitieren**  
Zentrum für Krebsregisterdaten (2023): Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen. Berlin:Zenodo. DOI:[10.5281/zenodo.8383547](https://doi.org/10.5281/zenodo.8383547)  

## Einleitung

In Deutschland wird die Krebsregistrierung von den Bundesländern auf landesrechtlicher Grundlage organisiert, wobei diverse medizinische Einrichtungen zur Meldung verplfichtet sind. Für die Meldungen legt das 2013 eingeführte Krebsfrüherkennungs- und registergesetz (KFRG) legt einen bundesweiten Standard für die Krebsregistrierung fest. Ein zentrales Element ist der onkologische Basisdatensatz (oBDS) der von mehreren okologischen fachgesellschaften entwickelt unf gepflegt wird.  
Das 2021 novellierte [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) zielt darauf ab, eine erweiterte Datenbasis für die Krebsforschung bereitzustellen. Vor diesem Hintergund führt das Zentrum für Krebsregisterdaten (ZfKD) nach Vorgabe des Bundeskrebsregisterdatengesetzes Daten der Landeskrebsregister zu einem bundesweiten klinischen Datensatz zusammen und stellt sie [auf Antrag für wissenschaftliche Forschungsprojekte](https://www.krebsdaten.de/info_antrag) zur Verfügung.  

Im vorliegenden Datensatz werden die _Metadaten_ und begleitende Informationen zur [Struktur](#Datenschema) und [Klassifikationen](#Klassifikationen) des bundesweiten klinischen Krebsregisterdatensatz des ZfKD zur Verfügung, sowie Beispieldaten bereitgestellt.

> 💡 Der onkologischen Basisdatensatz des RKI selbst ist nicht öffentlich zugänglich, kann aber auf Antrag für wissenschaftliche Forschungszwecke genutzt werden. Bitte verwenden Sie für Fragen zur Antragstellung das auf der Internetseite des ZfKD bereitgestellte [Kontaktformular](https://www.krebsdaten.de/SharedDocs/Kontaktformulare/A/Antrag-krebsdaten/Integrator_SCU.html). Informationen zum gesetzlichen Auftrag, zu Methoden und Veröffentlichungen des ZfKD erhalten Sie ebenfalls auf den [Internetseiten des ZfKD](https://www.krebsdaten.de/).  


## Informationen zum Datensatz und Entstehungskontext  

Die Krebsregistrierung in Deutschland wird von den Bundesländern auf Basis landesrechtlicher Vorgaben organisiert, meldepflichtig sind alle Ärztinnen und Ärzte bzw. Einrichtungen, die Krebserkrankungen diagnostizieren und behandeln. Dies sind im Wesentlichen Kliniken, niedergelassene Ärztinnen und Ärzte, pathologische Institute und Screeningeinheiten. Das 2013 verabschiedete Krebsfrüherkennungs- und registergesetz (KFRG) gibt einen bundesrechtlichen Rahmen vor, der u.a. eine einheitliche Finanzierung (durch Krankenkassen und Länder) und einen einheitlichen Meldedatensatz vorsieht - [den onkologischen Basidatensatz (oBDS)](https://basisdatensatz.de/). Letzterer wurde von zwei Fachgesellschaften, der Arbeitsgemeinschaft Deutscher Tumorzentren (ADT) und Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID) festgelegt. Er enthält seit einigen Jahren (Start variiert je nach Bundesland) neben epidemiologischen Daten auch klinische Angaben zur Therapie und zum Krankhe.csverlauf, und wird regelmäßig überarbeitet. Beide Gesellschafen haben den gesetzlichen Auftrag nach [§ 65c SGB V](https://www.gesetze-im-internet.de/sgb_5/__65c.html), den bundesweit einheitlichen Onkologischen Basisdatensatz mit spezifischen Modulen festzulegen und zu pflegen.  

Im Jahr 2021 wurde das Bundeskrebsregisterdatengesetz (BKRG) novelliert mit dem Ziel, eine umfangreichere Datenbasis für die Krebsforschung bereit zu stellen. Zur Ausgestaltung wurde eine Arbeitsgruppe gegründet, bestehend aus Mitgliedern des ZfKD  sowie der AG Daten, einem Gremium unter Beteiligung von ADT, GEKID und Plattform § 65C (P65c). Als Ergebnis entstand die Defintion eines abgestimmten Lieferdatensatzes, welcher abgeleitet ist vom oBDS. Auf Grundlage dieser Festlegung wurden technische Schnittstellen wie das hier beschriebene XML-Schema erarbeitet, welche für die Übermittlung der in den Landesregistern vorliegende Krebsdaten an das ZfKD genutzt werden.

Der aktualisierte Basisdatensatz wurde am 12. Juli 2021 im Bundesanzeiger publiziert. 

> [Bekanntmachung Aktualisierter einheitlicher onkologischer Basisdatensatz
der Arbeitsgemeinschaft Deutscher Tumorzentren e. V. (ADT) und der Gesellschaft der epidemiologischen Krebsregister in Deutschland e. V. (GEKID)](https://www.bundesanzeiger.de/pub/publication/bRrUsRox5lQ14casCXs/content/bRrUsRox5lQ14casCXs/BAnz%20AT%2012.07.2021%20B4.pdf?inline)

### Adminstrative und Organisatorische Angaben

Die Umsetzung der gesetzlichen Vorgaben erfolgt in der AG Daten, die sich aus stimmberechtigten Vertretenden von ADT und GEKID und Plattform § 65C zusammensetzt. Weitere beratende Organisationen sind mit Gaststatus beteiligt, darunter die Deutsche Krebsgesellschaft, die Patientenvertretung, das IT-Netzwerk der P65c sowie die Deutsche Krebshilfe/CCC Dokumentation.

Das [Zentrum für Krebsregisterdaten](https://www.krebsdaten.de/Krebs/DE/Home/homepage_node.html) des RKIs ist zuständig für die bundesweite Berichterstattung und stellt auf Antrag Daten für überregionale Forschungsprojekte an Dritte zur Verfügung. Außerdem werden Vollzähligkeit und Qualität der Daten beurteilt und den Registern zurückgemeldet.  
Inhaltliche Fragen bezüglich der Datenerhebung, der Datenauswertung oder Datenkuration können direkt an das ZfKD unter E-Mail-Adresse für Rückmeldungen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de) gestellt werden.

### Datenerhebung und Übermittlung

Das 2009 verabschiedete [BKRG](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) regelt die jährliche Zusammenführung der wesentlichen Daten aus den Landeskrebsregistern am ZfKD. Die Übermittlung erfolgt jeweils am Jahresende und enthält Informationen zu allen Fällen, die bis zum Ende des vorherigen Kalenderjahres diagnostiziert wurden, so dass auch Nachmeldungen und Korrekturen sowie Informationen zum Follow-up (z.B. Sterbefälle und Wegzüge) früherer Erkrankungsfälle enthalten sind.

Vor der Novellierung in 2021 wurde lediglich der deutlich kleinere epidemiologische Datensatz (mit Angaben zur Diagnose und zum Sterbezeitpunkt) an das ZfKD übermittelt, Dieser Datensatz wird bundesweit seit 2009 erfasst. Die Mehrzahl der Bundesländer hat zwischen 1998 und 2007 mit der landesweiten Erfassung begonnen.

### Datenerhebung

siehe https://plattform65c.atlassian.net/wiki/spaces 
- **Datenherhebung in den Kliniken und übermittlung an die LKR**
- **das ist leider keine persistnete Quelle... :(**

### Datenübermittlung an das ZfKD  

Seit der Datenlieferung zum 31.12.2022 und rückwirkend ab dem Diagnosejahr 2020 liefern die Register auch die oben genannten klinischen Angaben. Die am ZfKD vorliegenden Daten enthalten allerdings nicht den gesamten Datenbestand der Register, u.a. sind keine Angaben zu den behandelnden Einrichtungen verfügbar. Außerdem sind die Daten in den Krebsregistern bearbeitet worden: So wurden Meldungen aus verschiedenen Quellen zum gleichen Erkrankungsfall zusammengeführt und weitgehend um Widersprüche bereinigt („best-of“). Der Datensatz des ZfKD ist daher fall- und nicht meldungsbasiert, mehrere Tumorerkrankungen derselben Person können anhand einer von den Registern einmal vergebenen Personidentifikationsnummer zugeordnet werden. Die Übermittlung der Daten an das ZfKD erfolgt nach dem Wohnortprinzip (zum Zeitpunkt der Diagnose), so dass Doppelmeldungen weitgehend ausgeschlossen sind. Zwischen den Bundesländern erfolgt ein regelmäßiger Austausch von Daten, die außerhalb des Wohnortbundeslandes der Erkrankten erhoben und zunächst an das Krebsregister des Behandlungsortes gemeldet wurden. Eine fallweise Verknüpfung (Record Linkage) der Daten am ZfKD mit externen Datensätzen (Studien, Krankenkassen) ist nicht möglich.

- **Was ist mit folgendem Textbaustein?**

Der klinischen Datensatzes wird als `oBDS-RKI` bezeichnet. Die Bezeichnung geht zurück auf den zwischen der Arbeitsgemeinschaft Deutscher Tumorzentren e. V. (ADT), der Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID) und der Plattform § 65c abgestimmten `einheitlichen onkologischen Basisdatensatz` (`oBDS`), der für die Entwicklung des `oBDS-RKI` als Vorlage und Arbeitsgrundlage diente. An der Entwicklung des `oBDS-RKI` waren Vertreterinnen und Vertreter der Plattform § 65c, der ADT, der GEKID und des ZfKD beteiligt.

Weil er die Struktur und Inhalte der von den Landeskrebsregistern ans ZfKD zu liefernden Daten definiert, wird der `oBDS-RKI` auch als `ZfKD-Lieferdatensatz` bezeichnet.


#### Verpflichtende und optionale Angaben 

- **gehört das zum ZfKD oder zur allegemeinen Erhebung?**

Bestimmte Variablen sind Pflichtangaben, z. B. das _Geburtsdatum_, der _Inzidenzort_ und der _Diagnoseschlüssel_. Viele Angaben sind optional, z. B. die den Elementen cTNM und pTNM zugeordneten Variablen (_T-Kategorie_, _UICC-Stadium_, _m-Suffix_ usw.). Einige Angaben sind nur unter der Bedingung verpflichtend, dass das übergeordnete, optionale Element verwendet wird: Beispielsweise ist das Element Histologie optional. Wird jedoch in der zugehörigen Variable _Morphologie_ ein Eintrag vorgenommen, ist auch eine Angabe zum _Grading_ verpflichtend. Angaben zur Zahl untersuchter Lymphknoten bleiben optional.

Bei Auswertungen ist zu beachten, dass optionale Inhalte möglicherweise nicht gleichermaßen aus allen Bundesländern vorliegen.

## Struktur des bundesweiten klinischer Krebsregisterdatensatz  

Im vorligenden Datensatz wird Struktur des bundesweiten klinischer Krebsregisterdatensatz beschrieben, so wie er beim Zentrum für Krebsregisterdaten des RKIs vorliegt. Der Datensatz enhält keine Daten des bundesweiten klinischer Krebsregisterdatensatz. Zur Veranschaulichung werden jedoch zufällig generierte [Beispieldaten](#Beispieldaten) bereitgestellt.   

Folgende Informationen sind enthalten:

- [**Datenschema**](#Datenschema) des Datensatzes in verschieden Formaten
- [**Klassifikationen**](#Klassifikationen): Referenztabellen für Variablen des Datensatzes und ihre definierten Ausprägungen
- [**Beispieldaten**](#Beispieldaten): Ordner zur Veranschaulichung des Bereitstellungsprozesses der Daten
- [**Kontexmaterialien**](#Kontexmaterialien): Einige Referenztabellen geben Inhalte von Standards wieder, die von Dritten (z. B. BfArM, WIdO) herausgegeben werden. Unter Umständen verbinden diese Anbieter die Nutzung ihrer Produkte mit Bedingungen. Die Nutzungsbedingungen sind hier abgelegt. Wir bitten Sie diese zu beachten.


### Datenschema

Das Datenschema umfasst mehr als 120 Variablen, die verschiedenen Elementen zugeordnet sind. Die klinischen Daten können nicht in einer einfachen „Rechtecktabelle“ abgebildet werden, da es sich zum teil um komplexe Krankhe.csverälufe handelt. Im klinischen Datensatz sind die Daten in einem verschachtelten XML-Schema strukturiert.  
Der klinische Datensatz wird durch folgende Elemente gegliedert:

- Die _Person_ bildet die grundlegende Einheit im Datensatz.
- Der Person zugeordnet ist mindestens ein Element _Tumor_.
- Das Element _Tumor_ enthält ein verpflichtendes Element _Primärdiagnose_. Dieses enthält u. a. Angaben zum Tumorstadium, zur Histologie und Lokalisation des Tumors.
- Darüber hinaus sind dem Element _Tumor_ mehrere optionale Elemente zugeordnet, in denen Angaben zur Behandlung (Elemente _OP_, _ST_ und _SYST_) und zu Folgeereignissen (Element _Folgeereignis_) wie Remissionen und Rezidiven erfasst werden können.

Die Elemente _Primärdiagnose_, _Folgeereignis_, _OP_, _ST_ und _SYST_ können mehrfach verwendet werden, so dass auch komplexe Krankhe.csverläufe abgebildet werden können. Die Inhalte eines Elements können in ein tabellarisches Format überführt und über eine fallbezogene Nummer mit anderen Tabellen aus dem Datensatz verknüpft werden. Auf diese Weise entsteht ein auswertbares Format, in dem die bewilligten Daten an den Datenempfänger übermittelt werden können (siehe [Abs. Beispieldaten](#Beispieldaten)).  

Änderungen am Datenschema sind in [Release Notes](release-notes.md) zu finden. 

![Abbildung: Vereinfachtes Datenschema (mit ausgewählten Variablen). Quelle: [krebsdaten.de](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/forschungsdatensatz_node.html).](/.github/images/2023-06-30_Datenschema_einfach.png)  


#### Downloads

Das Datenschema wird in verschiedenen Formaten zum Download angeboten: 

| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| XML-Schema | Die XML-Schema-Definition `.xsd` als eindeutige, vollständige und maschinenlesbare Repräsentation des gesamten Schemas mit allen Details.   | [💾](/oBDS_v3.0.0.8a_RKI_Schema.xsd) |
| CSV-Schema | Variablen und mögliche Ausprägungen in tabellarischer Darstellung als `.csv`. | [💾](/oBDS_v3.0.0.8a_Variablen.csv) |
|TXT-Schema | Variablen und mögliche Ausprägungen in textuelle Darstellung zur erleichterten erkennung von Änderungen. | [💾](/oBDS_v3.0.0.8a_Variablen.txt) |
| PDF-Schema | Die grafische Darstellung des XML-Schemas als `.pdf`. Nicht alle Elemente sind abgebildet. Hinweise zur Notation des XML-Schemas sind [hier](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/59015169/Legende+zur+grafischen+Notation+des+XML-Schemas) zu finden. | [💾](/oBDS_v3.0.0.8a_Schema.pdf) |

#### XML-Schema des Datesatzes

Eine vollständige und maschinenlesbare Repräsentation des gesamten Datenschemas mit allen Details ist wir über des XML-Schema bereitgestellt.

> [oBDS_v3.0.0.8a_RKI_Schema.xsd](/oBDS_v3.0.0.8a_RKI_Schema.xsd)

Ein XML(Extensible Markup Language) Schema, oft auch als XSD (XML Schema Definition) bezeichnet, bietet einen Rahmen zur Beschreibung der Struktur und Datentypen eines XML-Dokuments. XML Schemata legen fest, welche Elemente und Attribute in einem XML-Dokument erscheinen können, wie diese strukturiert und organisiert sind und welche Datentypen sie enthalten können.  

XML Schemta können dazu verwendet werden, um XML-Dokumente zu validieren. Hierbei wird überprüft, ob ein XML-Dokument der im Schema definierten Struktur entspricht.
Die bereitgestellten "[oBDS_v3.0.0.8a_RKI_Sample.xml](/Beispieldaten/oBDS_v3.0.0.8a_RKI_Sample.xml)" können beispielsweise so auf ihre Schema-Konformität geprüft werden. 

Detaillierte technische Informationen zum XML-Schema sind auf der [Internetseite der Plattform § 65c abrufbar](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/2064400/XML-Schema) (bis Version `3.0.0.8_RKI`).

![Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes
Die obenstehende Abbildung veranschaulicht die Struktur des klinischen Datensatzes. ](/.github/images/2023-06-28_XML-Schema_grob.png)

### Klassifikationen

Die für einzelne Variablen erwarteten Ausprägungen und ihre Beschreibung sind in [Referenztabellen](#referenztabellen) hinterlegt. Einzelne Referenzen werden für mehrere Variablen genutzt: Beispielsweise wird für den Östrogen-Rezeptorstatus und den Progesteron-Rezeptorstatus die gleiche Kodierung verwendet. Ebenso werden für die Angaben zur klinischen und pathologischen TNM die gleichen Referenztabellen genutzt.

Größtenteils handelt es sich bei den Referenzen um Vereinbarungen, die bei der Erarbeitung des ZfKD-Lieferdatensatzes getroffen wurden (z. B. Ausprägungen von Variablen im Element Strahlentherapie, Ausprägungen von _Diagnosesicherung_). Teilweise handelt es sich bei den Referenzen um internationale oder nationale Standards (z. B. TNM, ATC-Klassifikation für den deutschen Arzneimittelmarkt). Informationen zu Quelle und Version der jeweiligen Referenzwerte, zu ihrer Interpretation und zu gegebenenfalls bestehenden Nutzungsbedingungen der Herausgeber sind im Abschnitt [Details](#details) zusammengestellt.

#### Referenztabellen

- ***Element* `technische Variablenbezeichnung`** erklären
- **vielleicht `technische` streichen**

| Klassifikation | *Element* `technische Variablenbezeichnung` | Datei |
| -------------- | ------------------------------------------- | ----- |
| Angabe zur perkutanen Strahlentherapie |*Strahlentherapie* `Atemgetriggert` | [atemgetriggert.csv](/Klassifikationen/atemgetriggert.csv) |
| Folgeereignis - Gesamtbeurteilung Tumorstatus |*Folgeereignis* `Gesamtbeurteilung_Tumorstatus` | [beurteilung_gesamt.csv](/Klassifikationen/beurteilung_gesamt.csv) |
| Folgeereignis - Beurteilung Primärtumor |*Folgeereignis* `Verlauf_Lokaler_Tumorstatus` | [beurteilung_lokal.csv](/Klassifikationen/beurteilung_lokal.csv) |
| Wertigkeit der Diagnosesicherung |*Primärdiagnose* `Diagnosesicherung` | [diagnosesicherung.csv](/Klassifikationen/diagnosesicherung.csv) |
| Lokalisation der Fernmetastasen |*Primärdiagnose* `Lokalisation`, *Folgeereignis* `Lokalisation` | [fm_lokalisation.csv](/Klassifikationen/fm_lokalisation.csv) |
| Geschlecht |*Person* `Geschlecht` | [geschlecht.csv](/Klassifikationen/geschlecht.csv) |
| Modul Prostata: Anlass der Probenahme |*Primärdiagnose* `AnlassGleasonScore` | [gleason_anlass.csv](/Klassifikationen/gleason_anlass.csv) |
| Modul Prostata: Gleason-Score |*Primärdiagnose* `ScoreErgebnis` | [gleason_score.csv](/Klassifikationen/gleason_score.csv) |
| Differenzierungsgrad |*Primärdiagnose* `Grading` | [grading.csv](/Klassifikationen/grading.csv) |
| Modul Mamma: Hormonrezeptorstatus |*Primärdiagnose* `HormonrezeptorStatus_Oestrogen`, *Primärdiagnose* `HormonrezeptorStatus_Progesteron` | [hormonrezeptor.csv](/Klassifikationen/hormonrezeptor.csv) |
| [Todesursache, Grundleiden nach ICD-10](#Todesursache-Grundleiden-nach-ICD-10) |*Todesursachen* `Code` | [icd10_todesursache.csv](/Klassifikationen/icd10_todesursache.csv) |
| Ausgabe der ICD-10 |*Todesursachen* `Version`, *Primärdiagnose* `Diagnose_ICD10_Version` | [icd10_version.csv](/Klassifikationen/icd10_version.csv) |
| [Diagnose nach ICD-10](#Diagnose-nach-ICD-10) |*Primärdiagnose* `Diagnose_ICD10_Code` | [icd10.csv](/Klassifikationen/icd10.csv) |
| Angabe zur Kontaktbestrahlung |*Strahlentherapie* `Interstitiell_endokavitaer` | [interstitiell.csv](/Klassifikationen/interstitiell.csv) |
| Wohnort bei Diagnose |*Primärdiagnose* `Inzidenzort`, *Primärdiagnose* `Inzidenzort_BL` | [landkreis.csv](/Klassifikationen/landkreis.csv) |
| Modul Mamma: Menopausenstatus |*Primärdiagnose* `Praetherapeutischer_Menopausenstatus` | [menopause.csv](/Klassifikationen/menopause.csv) |
| Typ der metabolischen Strahlentherapie |*Strahlentherapie* `Metabolisch_Typ` | [metabolisch.csv](/Klassifikationen/metabolisch.csv) |
| Quelle Morphologie |*Primärdiagnose* `Morphologie_Version` | [morphologie_version.csv](/Klassifikationen/morphologie_version.csv) |
| Morphologie |*Primärdiagnose* `Morphologie_Code` | [morphologie.csv](/Klassifikationen/morphologie.csv) |
| Intention der OP |*Operation* `Intention` | [op_intention.csv](/Klassifikationen/op_intention.csv) |
| [Operationen- und Prozedurenschlüssels (OPS)](Operationen--und-Prozedurenschlüssels-OPS) |*Operation* `Code` | [ops.csv](/Klassifikationen/ops.csv) |
| [Therapieprotokoll](Therapieprotokoll) |*Systemische Therapie* `Protokoll_TypProtokollschluessel_Code` | [protokoll.csv](/Klassifikationen/protokoll.csv) |
| Ausführung der perkutanen Radiochemotherapie |*Strahlentherapie* `Radiochemo` | [radiochemo.csv](/Klassifikationen/radiochemo.csv) |
| Modul Darm: Mutation K-ras-Onkogen |*Primärdiagnose* `RASMutation` | [rasmutation.csv](/Klassifikationen/rasmutation.csv) |
| Dosisleistung Kontaktbestrahlung |*Strahlentherapie* `Rate_Type` | [rate.csv](/Klassifikationen/rate.csv) |
| Körperseite der bestrahlten Region |*Strahlentherapie* `Seite_Zielgebiet` | [seite_zielgebiet.csv](/Klassifikationen/seite_zielgebiet.csv) |
| Seitenlokalisation bei paarigen Organen |*Primärdiagnose* `Seitenlokalisation` | [seitenlokalisation.csv](/Klassifikationen/seitenlokalisation.csv) |
| Intention der Strahlentherapie |*Strahlentherapie* `Intention` | [st_intention.csv](/Klassifikationen/st_intention.csv) |
| Bezug Strahlentherapie - OP |*Strahlentherapie* `Stellung_OP` | [st_op_stellung.csv](/Klassifikationen/st_op_stellung.csv) |
| Angabe zur perkutanen Strahlentherapie |*Strahlentherapie* `Stereotaktisch` | [stereotaktisch.csv](/Klassifikationen/stereotaktisch.csv) |
| [Verwendete Substanzen](#Verwendete-Substanzen) |*Systemische Therapie* `TypeOfSYST_TypSubstanz` | [substanz.csv](/Klassifikationen/substanz.csv) |
| Intention der systemischen Therapie |*Systemische Therapie* `Intention` | [syst_intention.csv](/Klassifikationen/syst_intention.csv) |
| Bezug systemische Therapie - OP |*Systemische Therapie* `Stellung_OP` | [syst_op_stellung.csv](/Klassifikationen/syst_op_stellung.csv) |
| Art der systemischen Therapie |*Systemische Therapie* `Therapieart` | [therapieart.csv](/Klassifikationen/therapieart.csv) |
| TNM-Ausgabe |*Primärdiagnose* `TNM_Auflage_c`, *Primärdiagnose* `TNM_Auflage_p`, *Folgeereignis* `Version` | [tnm_auflage.csv](/Klassifikationen/tnm_auflage.csv) |
| TNM-Präfix (c, p, u) |*Primärdiagnose* `c_p_u_Praefix_T_c`, *Primärdiagnose* `c_p_u_Praefix_N_c`, *Primärdiagnose* `c_p_u_Praefix_M_c`, *Primärdiagnose* `c_p_u_Praefix_T_p`, *Primärdiagnose* `c_p_u_Praefix_N_p`, *Primärdiagnose* `c_p_u_Praefix_M_p`, *Folgeereignis* `c_p_u_Praefix_T`, *Folgeereignis* `c_p_u_Praefix_N`, *Folgeereignis* `c_p_u_Praefix_M` | [tnm_cpu.csv](/Klassifikationen/tnm_cpu.csv) |
| TNM: Lymphgefäßinvasion |*Primärdiagnose cTNM* `L_p`, *Primärdiagnose pTNM* `L_p`, *Folgeereignis* `L` | [tnm_l.csv](/Klassifikationen/tnm_l.csv) |
| TNM: Fernmetastasierung |*Primärdiagnose cTNM* `M_c`, *Primärdiagnose pTNM* `M_p`, *Folgeereignis* `M` | [tnm_m.csv](/Klassifikationen/tnm_m.csv) |
| [TNM: Regionäre Lymphknotenmetastasierung](#TNM-Regionäre-Lymphknotenmetastasierung) |*Primärdiagnose cTNM* `N_c`, *Primärdiagnose pTNM* `N_p`, *Folgeereignis* `N` | [tnm_n.csv](/Klassifikationen/tnm_n.csv) |
| TNM: Perineuralinvasion |*Primärdiagnose cTNM* `Pn_c`, *Primärdiagnose pTNM* `Pn_p`, *Folgeereignis* `Pn` | [tnm_pn.csv](/Klassifikationen/tnm_pn.csv) |
| TNM: Serumtumormarker |*Primärdiagnose cTNM* `S_c`, *Primärdiagnose pTNM* `S_p`, *Folgeereignis* `S` | [tnm_s.csv](/Klassifikationen/tnm_s.csv) |
| TNM: Ausdehnung des Primärtumors |*Primärdiagnose cTNM* `T_c`, *Primärdiagnose pTNM* `T_p`, *Folgeereignis* `T` | [tnm_t.csv](/Klassifikationen/tnm_t.csv) |
| TNM: UICC-Stadium |*Primärdiagnose cTNM* `UICC_Stadium_c`, *Primärdiagnose pTNM* `UICC_Stadium_p`, *Folgeereignis* `UICC_Stadium` | [tnm_uicc.csv](/Klassifikationen/tnm_uicc.csv) |
| TNM: Veneninvasion |*Primärdiagnose cTNM* `V_c`, *Primärdiagnose pTNM* `V_p`, *Folgeereignis* `V` | [tnm_v.csv](/Klassifikationen/tnm_v.csv) |
| Ausgabe der ICD-O |*Primärdiagnose* `Topographie_Version` | [topographie_version.csv](/Klassifikationen/topographie_version.csv) |
| [ICD-O Topographie](#ICD-O-Topographie) |*Primärdiagnose* `Topographie_Code` | [topographie.csv](/Klassifikationen/topographie.csv) |
| Verlauf: Fernmetastasierung |*Folgeereignis* `Verlauf_Tumorstatus_Fernmetastasen` | [verlauf_fern.csv](/Klassifikationen/verlauf_fern.csv) |
| Verlauf: Lokaler Tumorstatus |*Folgeereignis* `Verlauf_Lokaler_Tumorstatus` | [verlauf_lokal.csv](/Klassifikationen/verlauf_lokal.csv) |
| Verlauf: Regionärer Lymphknotenstatus |*Folgeereignis* `Verlauf_Tumorstatus_Lymphknoten` | [verlauf_lymphe.csv](/Klassifikationen/verlauf_lymphe.csv) |
| Zielgebiet Strahlentherapie oBDS2014 |*Strahlentherapie Perkutan* `CodeVersion2014`, *Strahlentherapie Kontakt* `CodeVersion2014`, *Strahlentherapie Metabolisch* `CodeVersion2014`, *Strahlentherapie Sonstige* `CodeVersion2014`, *Strahlentherapie Unbekannt* `CodeVersion2014` | [zielgebiet2014.csv](/Klassifikationen/zielgebiet2014.csv) |
| Zielgebiet Strahlentherapie oBDS2021 |*Strahlentherapie Perkutan* `CodeVersion2021`, *Strahlentherapie Kontakt* `CodeVersion2021`, *Strahlentherapie Metabolisch* `CodeVersion2021`, *Strahlentherapie Sonstige* `CodeVersion2021`, *Strahlentherapie Unbekannt* `CodeVersion2021` | [zielgebiet2021.csv](/Klassifikationen/zielgebiet2021.csv) |

#### Datumsangaben

Die Angabe *Tag* wird von den Registern grundsätzlich *nicht* ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format `Jahr-Monat-Tag` vorliegt. Für jede Datumsangabe im Datensatz liegen jeweils zwei Variablen vor:

- das *Datum* im internationalen Datumsformat (ISO 8061) `yyyy-mm-dd` und
- die *Genauigkeit* des Datums in einer von drei möglichen Ausprägungen (`M`, `T`, `V`):
  `M` = nur das Jahr ist bekannt (jahrgenau)
  `T` = Jahr und Monat sind bekannt (monatsgenau)
  `V` = Jahr und Monat wurden geschätzt

#### Ergänzungen zu den Referenztabellen

In diesem Abschnitt werdenergänzende Informationen zu den Inhalten der [Referenztabellen](#referenztabellen) bereitgestellt.

##### Diagnose nach ICD-10

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-10-GM (Version 2008) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html), unter Verwendung der [Empfehlungen des GKV-Spitzenverbands für die klinische Krebsregistrierung (Stand: 14.05.2020)](https://www.gkv-spitzenverband.de/krankenversicherung/qualitaetssicherung_2/klinisches_krebsregister.jsp) und unter Verwendung des [Umsetzungsleitfadens der Plattform § 65c (Stand: 06.06.2023)](https://confluence.basisdatensatz.de/display/UMK/Meldepflichtige+Diagnosen+nach+ICD).  
Die Nutzungsbedingungnen der ICD-10 des BfArM sind in den [Kontextmaterialien](#Kontextmaterialien) hinterlegt.

> [/Klassifikationen/icd10.csv](/Klassifikationen/icd10.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10 Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10 Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z.b. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  3-stelliger Diagnoseschlüssel |
| epi_valide| Boolen | `TRUE`, `FALSE`  | Information ob die Diagnose im [epidemiologischen Datensatz](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/Informationen_datensatz/epidemiologischer_datensatz/epidemiologischer_datensatz_node.html) des ZfKD enthalten ist |
| p65_valide| Boolen| `TRUE`, `FALSE`  | Es besteht eine Meldepflicht für den klinischen Datensatz (lt. Plattform § 65c-Umsetzungsleitfaden | 

##### Todesursache, Grundleiden nach ICD-10

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-10-GM (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html). Die Nutzungsbedingungnen der ICD-10 des BfArM sind in den [Kontextmaterialien](#Kontextmaterialien) hinterlegt.

Um die internationale Vergleichbarkeit zu gewährleisten, ist für die [Verschlüsselung von Todesursachen die ICD-10-WHO](https://www.bfarm.de/DE/Kodiersysteme/Klassifikationen/ICD/ICD-10-WHO/Todesursachenstatistik/_node.html) vorgesehen. Aktuell wird bei der Übermittlung von Todesursachen ans ZfKD vorwiegend (noch) die Verwendung der ICD-10-GM angegeben.

> [/Klassifikationen/icd10_todesursache.csv](/Klassifikationen/icd10_todesursache.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10 Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10 Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z.b. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  3-stelliger Diagnoseschlüssel |
| chapter   | Integer | z. B. `1`  |  Kapitel der ICD-10 |


##### ICD-O Topographie

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-O-3 (2. Revision, Version 2019) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html) und unter Zuhilfenahme des [Umsetzungsleitfadens der Plattform § 65c (Stand: 10.05.2023)](https://confluence.basisdatensatz.de/display/UMK/Paarige+Organe). 
Die Nutzungsbedingungnen der ICD-O-3 des BfArM sind in den [Kontextmaterialien](#Kontextmaterialien) hinterlegt.

Für paarige Organe (Ausprägung *istPaarig* = `1`, lt. Plattform § 65c-Umsetzungsleitfaden) wird bei der Variable *Seitenlokalisation* die Angabe der betroffenen Körperseite(n) erwartet.

> [Klassifikationen/topographie.csv](Klassifikationen/topographie.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10 Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10 Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z.b. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  3-stelliger Diagnoseschlüssel |
| istPaarig   | Integer | z. B. `1`  |  1 = es handelt sich um ein paariges Organ und es wird bei der Variable *Seitenlokalisation* die Angabe der betroffenen Körperseite(n) erwartet. |

- **Boolean statt 1 und 0?**


##### Operationen- und Prozedurenschlüssels (OPS)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung des [Operationen- und Prozedurenschlüssels (OPS) (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html). Die Nutzungsbedingungnen der Operationen- und Prozedurenschlüssels (OPS) des BfArM sind in den [Kontextmaterialien](#Kontextmaterialien) hinterlegt.

> [Klassifikationen/ops.csv](/Klassifikationen/ops.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| ops_id | String | z. B. `1-202`  | ID, maximal 6-stellig |
| ops_chapter | Integer | z. B. `1`  | OPS-Kapitel |
| ops_group | String | z. B. `1-20 - 1-33`  | OPS-Gruppe, -Bereich |
| ops_three_digits | String | z. B. `1-20`  | OPS-Kategorie/-Kode, 3-stellig |
| ops_four_digits | String | z. B. `1-202`  | OPS-Kategorie/-Kode, 4-stellig |
| ops_five_digits | String | z. B. `1-202.-`  | OPS-Kategorie/-Kode, 5-stellig |
| ops_six_digits | String | z. B. `1-202.--`  | OPS-Kategorie/-Kode, 6-stellig |
| ops_description | String | z. B. `Diagnostik zur Feststellung ...`  | Klassentitel der Maßnahme |

##### Therapieprotokoll

Bei der verwendeten Referenztabelle handelt es sich um eine *Vorschlagsliste* der [Plattform § 65c](https://confluence.basisdatensatz.de/display/UMK/Protokolle). Diese Vorschlagsliste stellt keine verbindliche Festlegung dar. Ein anerkannter Standard für die Kodierung von Systemtherapie-Protokollen ist uns nicht bekannt. Vorschläge für eine standardisierte Nomenklatur ([Rubinstein et al, 2020](https://doi.org/10.1200/CCI.19.00122)), Referenzsysteme ([HemOnc.org](https://hemonc.org/), [National Cancer Institute Thesaurus (NCIT)](https://bioportal.bioontology.org/ontologies/NCIT/?p=classes&conceptid=http%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23C62634)) und kommerzielle Produkte für die medizinische Dokumentation ([Onkopti®](https://onkopti.de/protokollsuche/)) wurden von anderen entwickelt. Wir verweisen hier auf eine Auswahl dieser Arbeiten und Systeme.

> Rubinstein, S. M., Yang, P. C., Cowan, A. J., & Warner, J. L. (2020). Standardizing Chemotherapy Regimen Nomenclature: A Proposal and Evaluation of the HemOnc and National Cancer Institute Thesaurus Regimen Content. JCO clinical cancer informatics, 4, 60–70. [https://doi.org/10.1200/CCI.19.00122](https://doi.org/10.1200/CCI.19.00122)  

> [Onkopti® – die Datenbank digitalisierter onkologischer Therapieprotokolle](https://onkopti.de/protokollsuche/)

##### Verwendete Substanzen

Die Erstellung der Referenztabelle erfolgte unter Verwendung der [Anatomisch-therapeutisch-chemischen Klassifikation (ATC-Klassifikation) für den deutschen Arzneimittelmarkt (Version 2022)](https://www.wido.de/publikationen-produkte/arzneimittel-klassifikation/), herausgegeben vom Wissenschaftlichen Institut der AOK (WIdO). Die Nutzungsbedingungnen der ATC-Klassifikation des WIdO sind in den [Kontextmaterialien](#Kontextmaterialien) hinterlegt.

> [/Klassifikationen/substanz.csv](/Klassifikationen/substanz.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| code | String | z. B. `J05AF06`  | ATC-Kode, Ebene 5 |
| name| Sting | z. B. `Abacavir`  | Bezeichnung des Arzneimittels |


##### TNM: Regionäre Lymphknotenmetastasierung

- **einleitender Satz**
- **was ist S3-Leitlinie Mammakarzinom und TMN8?**
 
> [/Klassifikationen/tnm_n.csv](/Klassifikationen/tnm_n.csv)
 
###### **Zusatz (1mi), Mammakarzinom**

Anwendung bei: Mikrometastase(n), > 0,2 mm und/oder mehr als 200 Tumorzellen, aber nicht größer als 0,2 cm
Stadium IB nach TNM8: T0, T1 N1mi M0

> *Quelle: S3-Leitlinie Mammakarzinom, TNM8*

###### **Zusatz (sn)**

| Ausprägung | Beschreibung | 
| ---------- | ------------ | 
| `(p)NX(sn)` | Schildwächterlymphknoten kann histologisch nicht beurteilt werden | 
| `(p)N0(sn)` | Histologisch keine Lymphknotenmetastasen in Schildwächterlymphknoten |
| `(p)N1(sn)` | Befall des (der) Schildwächterlymphknoten |


> *Quelle: TNM8*

###### **Zusatz (i+), (mol+)**

| Ausprägung | Beschreibung | 
| ---------- | ------------ | 
| `(p)N0` | Histologisch keine Lymphknotenmetastasen, keine Untersuchung zum Nachweis isolierter Tumorzellen | 
| `(p)N0(i–)` | Histologisch keine Lymphknotenmetastasen, kein morphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(i+)` | Histologisch keine Lymphknotenmetastasen, morphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(mol–)` | Histologisch keine Lymphknotenmetastasen, kein nichtmorphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(mol+)`| Histologisch keine Lymphknotenmetastasen, nicht-morphologischer Nachweis von isolierten Tumorzellen |

> *Quelle: TNM8*

### Beispieldaten

In diesem Repository soll der [Beantragungsprozess](https://www.krebsdaten.de/info_antrag) für klinische Daten veranschaulicht werden.

Zum einen ist ein [Spieldatensatz](/Beispieldaten/oBDS_v3.0.0.8a_RKI_Sample.xml) hinterlegt für die Lieferung der Daten aus den klinischen Krebsregistern der Länder. Dieser entspricht den gemeinsam erarbeiteten Vorgaben des `oBDS-RKI` und wird im ZfKD zu einem deutschlandweiten Gesamtdatensatz verarbeitet. Der "rohe" Datensatz bestehend aus xml-Dateien bildet den Ausgangspunkt der weiteren Verarbeitung, wird aber vom ZfKD nicht ausgegeben.

XML ist eien Auszeichungssprache mit definiert Struktur und Syntax. XML-Dokumente sind textbasiert und repräsentieren Daten in einer hierarchischen und strukturierten Weise. Der Hauptzweck von XML besteht darin, Daten so zu beschreiben, die sowohl für Menschen als auch für Maschinen leicht verständlich und interpretierbar ist.

Zum anderen wird hier simuliert, wie eine definierte Teilmenge des verarbeiteten Gesamtdatensatzes auf Antrag übermittelt wird.
Beispielhaft enthält der Ordner `04_sample-output` unter `data` eine Sammlung von csv-Dateien. Format und Aufbau dieser Dateien entsprechen exakt einer Datenlieferung auf Antrag.

Verwendete Identifikatoren können in einem relationalen Modell wieder korrekt zusammengeführt werden (so sind etwa Einträge der Tumortabelle den jeweiligen Patienten zuordenbar). Hilfestellung bietet hier das angehangene [ER-Modell](/.github/images/2023-09-28_Entity-Relationship-Modell.jpg).

_(Die in den Beispieldateien hinterlegten Daten sind künstlich erzeugt, folgen einfachen Verteilungen und berücksichtigen keine medizinischen Zusammenhänge. Die Identifikatoren sind zufällig erzeugt)_


| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| Testdatensatz | Ein einfacher Testdatensatz als `.xml`-Datei mit Werten in zufälliger Verteilung. Medizinische Zusammenhänge sind nicht berücksichtigt. Näheres unter [Beispieldaten](#beispieldaten) | [💾](/Beispieldaten/oBDS_v3.0.0.8a_RKI_Sample.xml) |

- **Ergänzung der Tabelle um die weiteren Entetys (.csv)**
- **beschreibung des ERM**


### Kontextmaterialien

- **kurze Hinweise zu den Nutzungbedingungne BfArm WIDO**
- **(eventuell kann die beschreibung auch zu den Klassifikationen)**

### Metadaten

Zur Erhöhung der Auffindbarkeit sind die bereitgestellten Daten mit Metadaten beschrieben. Über GitHub Actions werden Metadaten an die entsprechenden Plattformen verteilt. Für jede Plattform existiert eine spezifische Metadatendatei, diese sind im Metadatenordner hinterlegt:  

> [Metadaten/](https://github.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/blob/main/Metadaten/)  

Versionierung und DOI-Vergabe erfolgt über [Zenodo.org](https://zenodo.org). Die für den Import in Zenodo bereitgestellten Metadaten sind in der [zenodo.json](https://github.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/blob/main/Metadaten/zenodo.json) hinterlegt. Die Dokumentation der einzelnen Metadatenvariablen ist unter https://developers.zenodo.org/representation nachlesbar.   

> [Metadaten/zenodo.json](https://github.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/blob/main/Metadaten/zenodo.json)  


## Hinweise zur Nachnutzung der Daten  

Offene Forschungsdaten des RKI werden auf [Zenodo.org](http://Zenodo.org/), [GitHub.com](http://GitHub.com/), [OpenCoDE](https://gitlab.opencode.de) und [Edoc.rki.de](http://Edoc.rki.de/) bereitgestellt:

- https://zenodo.org/communities/robertkochinstitut
- https://github.com/robert-koch-institut
- https://gitlab.opencode.de/robert-koch-institut
- https://edoc.rki.de/

### Lizenz  

Der Datensatz "Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen" ist lizenziert unter der [Creative Commons Namensnennung 4.0 International Public License | CC-BY ](https://creativecommons.org/licenses/by/4.0/deed.de).  

Die im Datensatz bereitgestellten Daten sind, unter Bedingung der Namensnennung des Robert Koch-Instituts als Quelle, frei verfügbar. Das bedeutet, jede Person hat das Recht die Daten zu verarbeiten und zu verändern, Derivate des Datensatzes zu erstellen und sie für kommerzielle und nicht kommerzielle Zwecke zu nutzen. Weitere Informationen zur Lizenz finden sich in der [LICENSE](https://github.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/blob/main/LICENSE) bzw. [LIZENZ](https://github.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/blob/main/LIZENZ) Datei des Datensatzes.
