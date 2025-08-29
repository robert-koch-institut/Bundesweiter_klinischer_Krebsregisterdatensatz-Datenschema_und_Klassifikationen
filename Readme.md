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
Meisegeier, S., Imhoff, M., Berg, K., & Kraywinkel, K. (2024). Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen [Data set]. Zenodo. [https://doi.org/10.5281/zenodo.10022040](https://doi.org/10.5281/zenodo.10022040)

<br>


<br>

---

E-Mail-Adresse für Rückmeldungen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)  

---

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

In diesem Repository werden begleitende Informationen zu [Struktur](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes) und [Klassifikationen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#klassifikationen) des bundesweiten ZfKD-Datensatzes bereitgestellt.

Die hier verwendeten [Klassifikationen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#klassifikationen) spiegeln den derzeitigen Arbeitsstand des ZfKD wider. Ein wesentliches Ziel des Repositories ist es, diesen Stand möglichst transparent abzubilden und beteiligte Akteure zur weiteren gemeinsamen Harmonisierung von Standards einzuladen.

> 💡 Der ZfKD-Datensatz ist nicht öffentlich zugänglich, kann aber auf Antrag für wissenschaftliche Forschungszwecke genutzt werden. Bitte verwenden Sie für Fragen zur Antragstellung die oben genannte E-Mail-Adresse oder das auf der Internetseite des ZfKD bereitgestellte [Kontaktformular](https://www.krebsdaten.de/SharedDocs/Kontaktformulare/A/Antrag-krebsdaten/Integrator_SCU.html). Informationen zum gesetzlichen Auftrag, zu Methoden und Veröffentlichungen des ZfKD erhalten Sie ebenfalls auf den [Internetseiten des ZfKD](https://www.krebsdaten.de/). Bitte beachten Sie, dass das ZfKD an den Daten, die von den Krebsregistern übermittelt wurden, keine Änderungen vornimmt.

## Informationen zum Entstehungskontext des ZfKD-Datensatzes

Für die Erhebung klinischer Krebsregisterdaten wurde mit dem [Krebsfrüherkennungs- und -registergesetz (KFRG)](https://www.bgbl.de/xaver/bgbl/start.xav?start=//*%5B@attr_id=%27bgbl113s0617.pdf%27%5D#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl113s0617.pdf%27%5D__1697181091765) im [§ 65c Fünftes Buch Sozialgesetzbuch (SGB V)](https://www.gesetze-im-internet.de/sgb_5/__65c.html) ein bundesrechtlicher Rahmen geschaffen. Die von den klinischen Krebsregistern zu erfassenden Angaben werden in dem von der Arbeitsgemeinschaft Deutscher Tumorzentren (ADT) und der Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID) erarbeiteten [onkologischen Basisdatensatz (oBDS)](https://basisdatensatz.de/) spezifiziert und regelmäßig überarbeitet. Die letzte Anpassung des oBDS wurde am 12. Juli 2021 [im Bundesanzeiger publiziert](https://www.bundesanzeiger.de/pub/publication/bRrUsRox5lQ14casCXs/content/bRrUsRox5lQ14casCXs/BAnz%20AT%2012.07.2021%20B4.pdf). Einmal jährlich übermitteln die Krebsregister Daten nach Maßgabe des [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) an das ZfKD.

Seit der Novellierung des BKRG durch das [Gesetz zur Zusammenführung von Krebsregisterdaten](https://www.bgbl.de/xaver/bgbl/start.xav#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl121s3890.pdf%27%5D__1697190045694) enthalten die ans ZfKD übermittelten Daten auch klinische Angaben, u. a. zum Krankheitsverlauf und zur Behandlung (ab Diagnosejahr 2020).

Die Inhalte und die Struktur der ans ZfKD zu übermittelnden Daten wurden in einer AG mit Vertretern des ZfKD und der Krebsregister abgestimmt, dabei diente der oBDS und das novellierte Bundeskrebsregisterdatengesetz (§5) als Arbeitsgrundlage.

Das Arbeitsergebnis ist das hier beschriebene, für die Datenübermittlung ans ZfKD zu verwendende XML-Schema (alternativ als oBDS-RKI oder ZfKD-Lieferdatensatz bezeichnet, siehe dazu [Struktur des bundesweiten klinischen Krebsregisterdatensatzes](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes)).

Umfassende Informationen zur Krebsregistrierung sind hier verfügbar: [Manual der klinischen und epidemiologischen Krebsregistrierung](https://www.gekid.de/download/1228/?tmstv=1697113791) (Veröffentlichung 2019)

### Administrative und organisatorische Angaben

Das [Zentrum für Krebsregisterdaten (ZfKD)](https://www.krebsdaten.de/) des RKI ist zuständig für die bundesweite Krebsberichterstattung und stellt Dritten auf Antrag Daten für überregionale Forschungsprojekte zur Verfügung. Es prüft die Qualität der von den Krebsregistern übermittelten Daten und gibt den Krebsregistern diesbezüglich Rückmeldung.  

Inhaltliche Fragen zur Datenerhebung, Datenauswertung und Datenkuration können direkt an das ZfKD gestellt werden (E-Mail-Adresse für Anfragen: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)).

### Datenübermittlung an das ZfKD  

Das 2009 verabschiedete BKRG regelt die jährliche Zusammenführung der wesentlichen Daten aus den Krebsregistern am ZfKD. Die Übermittlung erfolgt jeweils am Jahresende und enthält Informationen zu allen Fällen, die bis zum Ende des vorherigen Kalenderjahres diagnostiziert wurden, so dass auch Nachmeldungen und Korrekturen sowie Informationen zum Follow-up (z. B. Sterbefälle und Wegzüge) früherer Erkrankungsfälle enthalten sind.

Vor der Novellierung des BKRG in 2021 wurde lediglich der deutlich kleinere epidemiologische Datensatz (mit Angaben zur Diagnose und zum Sterbezeitpunkt) an das ZfKD übermittelt. Dieser Datensatz wird bundesweit seit 2009 erfasst. Die Mehrzahl der Bundesländer hat zwischen 1998 und 2007 mit der landesweiten Erfassung begonnen.

Seit der Datenlieferung zum 31. Dezember 2022 und rückwirkend ab dem Diagnosejahr 2020 liefern die Krebsregister [auch klinische Angaben](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#informationen-zum-entstehungskontext-des-zfkd-datensatzes). Die am ZfKD vorliegenden Daten enthalten allerdings nicht den gesamten Datenbestand der Register, beispielsweise sind keine Angaben zu den behandelnden Einrichtungen verfügbar.

Außerdem sind die Daten in den Krebsregistern bearbeitet worden: So wurden Meldungen aus verschiedenen Quellen zum gleichen Erkrankungsfall zusammengeführt und weitgehend um Widersprüche bereinigt („best-of“). Der Datensatz des ZfKD ist daher fall- und nicht meldungsbasiert, mehrere Tumorerkrankungen derselben Person können anhand einer von den Registern einmal vergebenen Personidentifikationsnummer zugeordnet werden. Die Übermittlung der Daten an das ZfKD erfolgt nach dem Wohnortprinzip (zum Zeitpunkt der Diagnose), so dass Doppelmeldungen weitgehend ausgeschlossen sind. Zwischen den Bundesländern erfolgt ein regelmäßiger Austausch von Daten, die außerhalb des Wohnortbundeslandes der Erkrankten erhoben und zunächst an das Krebsregister des Behandlungsortes gemeldet wurden.

> 💡 Eine fallweise Verknüpfung (Record Linkage) der am ZfKD vorliegenden Daten mit externen Datensätzen (Studien, Krankenkassen) ist nicht möglich.

## Struktur des bundesweiten klinischen Krebsregisterdatensatzes  

Der klinische Datensatz wird als `oBDS-RKI` bezeichnet. Die Bezeichnung geht zurück auf den zwischen ADT, GEKID und Plattform § 65c abgestimmten `einheitlichen onkologischen Basisdatensatz` (`oBDS`), der für die Entwicklung des `oBDS-RKI` als Vorlage und Arbeitsgrundlage diente (siehe [Informationen zum Datensatz und Entstehungskontext](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#informationen-zum-entstehungskontext-des-zfkd-datensatzes)).

Weil er die Struktur und Inhalte der von den Landeskrebsregistern ans ZfKD zu liefernden Daten definiert, wird der `oBDS-RKI` auch als `ZfKD-Lieferdatensatz` bezeichnet.

Zur Veranschaulichung der Datenstruktur werden zufällig generierte [Beispieldaten](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#beispieldaten) bereitgestellt.

Folgende Informationen sind enthalten:

- [**Datenschema**](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#datenschema) des Datensatzes in verschieden Formaten
- [**Klassifikationen**](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#klassifikationen): Referenztabellen für Variablen des Datensatzes und ihre definierten Ausprägungen
- [**Beispieldaten**](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#beispieldaten): zur Veranschaulichung des Bereitstellungsprozesses der Daten

### Datenschema

Das Datenschema umfasst mehr als 120 Variablen, die verschiedenen Elementen zugeordnet sind. Die klinischen Daten können nicht in einer einfachen „Rechtecktabelle“ wiedergegeben werden, da sie zum Teil komplexe Krankheitsverläufe abbilden. Im klinischen Datensatz sind die Daten daher in einem verschachtelten XML-Schema strukturiert.  

Der klinische Datensatz wird durch folgende Elemente gegliedert:

- Die _Person_ bildet die grundlegende Einheit im Datensatz.
- Der Person zugeordnet ist mindestens ein Element _Tumor_.
- Das Element _Tumor_ enthält ein verpflichtendes Element _Primärdiagnose_. Dieses enthält u. a. Angaben zum Tumorstadium, zur Histologie und Lokalisation des Tumors.
- Darüber hinaus sind dem Element _Tumor_ mehrere optionale Elemente zugeordnet, in denen Angaben zur Behandlung (Elemente _OP_, _ST_ und _SYST_) und zu Folgeereignissen (Element _Folgeereignis_) wie Remissionen und Rezidiven erfasst werden können.

Bestimmte Variablen sind Pflichtangaben, z. B. das _Geburtsdatum_, der _Inzidenzort_ und der _Diagnoseschlüssel_. Viele Angaben sind optional, z. B. die den Elementen cTNM und pTNM zugeordneten Variablen (_T-Kategorie_, _UICC-Stadium_, _m-Suffix_ usw.). Einige Angaben sind nur unter der Bedingung verpflichtend, dass das übergeordnete, optionale Element verwendet wird: Beispielsweise ist das Element Histologie optional. Wird jedoch in der zugehörigen Variable _Morphologie_ ein Eintrag vorgenommen, ist auch eine Angabe zum _Grading_ verpflichtend. Angaben zur Zahl untersuchter Lymphknoten bleiben optional.

Bei Auswertungen ist zu beachten, dass optionale Inhalte möglicherweise nicht gleichermaßen aus allen Bundesländern vorliegen.

Die Elemente _Primärdiagnose_, _Folgeereignis_, _OP_, _ST_ und _SYST_ können mehrfach verwendet werden, so dass auch komplexe Krankheitsverläufe abgebildet werden können. Die Inhalte eines Elements können in ein tabellarisches Format überführt und über eine fallbezogene Nummer mit anderen Tabellen aus dem Datensatz verknüpft werden. Auf diese Weise entsteht ein auswertbares Format, in dem die bewilligten Daten an den Datenempfänger übermittelt werden können (siehe [Beispieldaten](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#beispieldaten)).  

Protokollierte Änderungen am Datenschema sind in den beigefügten [Release Notes](release-notes.md) der Versionen zu finden.

![Abbildung: Vereinfachtes Datenschema (mit ausgewählten Variablen). Quelle: [krebsdaten.de](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/forschungsdatensatz_node.html).](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/.github/images/2023-06-30_Datenschema_einfach.png)  
> Abbildung: Vereinfachtes Datenschema (mit ausgewählten Variablen). Quelle: [krebsdaten.de](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/forschungsdatensatz_node.html).

#### Downloads

Das Datenschema wird in verschiedenen Formaten zum Download angeboten:

| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| XML-Schema | Die XML-Schema-Definition `.xsd` als eindeutige, vollständige und maschinenlesbare Repräsentation des gesamten Schemas mit allen Details.   | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.xsd) |
| XLSX-Schema | Variablen und mögliche Ausprägungen in tabellarischer Darstellung als `.xlsx`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.xlsx) |
| TXT-Schema | Variablen und mögliche Ausprägungen in stark vereinfachter textueller Darstellung zur erleichterten Erkennung von Änderungen. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.txt) |
| PDF-Schema (Abbildung) | Die grafische Darstellung des XML-Schemas als `.pdf`. Aufgrund der Komplexität des Gesamtschemas sind nicht alle Elemente abgebildet. Hinweise zur Notation des XML-Schemas sind [hier](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/59015169/Legende+zur+grafischen+Notation+des+XML-Schemas) zu finden. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema_Abbildung.pdf) |
| PDF-Schema (Liste) | Optisch gestaltete und "druckerfreundliche" Kurzübersicht zu Variablen und möglichen Ausprägungen als `.pdf`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema_Liste.pdf) |

#### XML-Schema des Datensatzes

Eine vollständige und maschinenlesbare Repräsentation des gesamten Datenschemas mit allen Details ist wird über das [XML-Schema](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.xsd) bereitgestellt.

XML (Extensible Markup Language)-Schemata definieren den erlaubten Aufbau der ihnen zugeordneten XML-Dokumente. XML ist eine Auszeichnungssprache mit definierter Struktur und Syntax. XML-Dokumente sind textbasiert und repräsentieren Daten in einer hierarchischen und strukturierten Weise. Der Hauptzweck von XML besteht darin, Daten so zu beschreiben, dass sie sowohl für Menschen als auch für Maschinen leicht verständlich und interpretierbar sind.

Ein XML-Schema, oft auch als XSD (XML Schema Definition) bezeichnet, bietet einen Rahmen zur Beschreibung der Struktur und Datentypen eines XML-Dokuments. XML-Schemata legen fest, welche Elemente und Attribute in einem XML-Dokument erscheinen können, wie diese strukturiert und organisiert sind und welche Datentypen sie enthalten können. XML-Schemata können dazu verwendet werden, um XML-Dokumente zu validieren. Hierbei wird überprüft, ob ein XML-Dokument der im Schema definierten Struktur entspricht.

Detaillierte technische Informationen zum abgestimmten XML-Schema sind auf der [Internetseite der Plattform § 65c abrufbar](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/2064400/XML-Schema) (bis Version `3.0.0.8_RKI`).

![Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes
Die obenstehende Abbildung veranschaulicht die Struktur des klinischen Datensatzes. ](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/.github/images/2023-06-28_XML-Schema_grob.png)
> Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes. Quelle: eigene Darstellung.

### Klassifikationen

Die für einzelne Variablen erwarteten Ausprägungen und ihre Beschreibung sind in [Referenztabellen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#referenztabellen) hinterlegt. Einzelne Referenzen werden für mehrere Variablen genutzt: Beispielsweise wird für den Östrogen-Rezeptorstatus und den Progesteron-Rezeptorstatus die gleiche Kodierung verwendet. Ebenso werden für die Angaben zur klinischen und pathologischen TNM die gleichen Referenztabellen genutzt.

Größtenteils handelt es sich bei den Referenzen um Vereinbarungen, die bei der Erarbeitung des ZfKD-Lieferdatensatzes getroffen wurden (z. B. Ausprägungen von Variablen im Element Strahlentherapie, Ausprägungen von _Diagnosesicherung_). Teilweise handelt es sich bei den Referenzen um internationale oder nationale Standards (z. B. TNM, ATC-Klassifikation für den deutschen Arzneimittelmarkt). Informationen zu Quelle und Version der jeweiligen Referenzwerte, zu ihrer Interpretation und zu gegebenenfalls bestehenden Nutzungsbedingungen der Herausgeber sind im Abschnitt [Ergänzungen zu den Referenztabellen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#ergänzungen-zu-den-referenztabellen) zusammengestellt.

> 💡 Einige Referenztabellen geben Inhalte von Standards wieder, die von Dritten herausgegeben werden. Unter Umständen verbinden diese Anbieter die Nutzung ihrer Produkte mit Bedingungen. Die Nutzungsbedingungen sind an den jeweils zutreffenden Stellen verlinkt. Wir bitten Sie diese zu beachten.

#### Referenztabellen

In der folgenden Übersicht sind die verwendeten Referenztabellen aufgeführt. Die Tabellen bilden den Wertebereich aller _kodierten_ Variablen als Klassifikationen ab.

Bedeutung der Spalten:

- **Klassifikation** ausformulierte Bezeichnung der Klassifikation
- **Element** `technische Variablenbezeichnung` Elternknoten im XML-Schema sowie der technische Name der entsprechenden Variable. Dieser Name wird u.a. auch im exportierten Datensatz verwendet.
- **Datei** Name der Klassifikationsdatei

| Klassifikation | *Element* `technische Variablenbezeichnung` | Datei |
| -------------- | ------------------------------------------- | ----- |
| Angabe zur perkutanen Strahlentherapie |*Strahlentherapie* `Atemgetriggert` | [atemgetriggert.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/atemgetriggert.csv) |
| Folgeereignis - Gesamtbeurteilung Tumorstatus |*Folgeereignis* `Gesamtbeurteilung_Tumorstatus` | [beurteilung_gesamt.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/beurteilung_gesamt.csv) |
| Folgeereignis - Beurteilung Primärtumor |*Folgeereignis* `Verlauf_Lokaler_Tumorstatus` | [beurteilung_lokal.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/beurteilung_lokal.csv) |
| Wertigkeit der Diagnosesicherung |*Primärdiagnose* `Diagnosesicherung` | [diagnosesicherung.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/diagnosesicherung.csv) |
| DCN (death certificate notified) |*Primärdiagnose* `DCN` | [dcn.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/dcn.csv) |
| Lokalisation der Fernmetastasen |*Primärdiagnose* `Lokalisation`, *Folgeereignis* `Lokalisation` | [fm_lokalisation.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/fm_lokalisation.csv) |
| Geschlecht |*Person* `Geschlecht` | [geschlecht.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/geschlecht.csv) |
| Modul Prostata: Anlass der Probenahme |*Primärdiagnose* `AnlassGleasonScore` | [gleason_anlass.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/gleason_anlass.csv) |
| Modul Prostata: Gleason-Score |*Primärdiagnose* `ScoreErgebnis` | [gleason_score.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/gleason_score.csv) |
| Differenzierungsgrad |*Primärdiagnose* `Grading` | [grading.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/grading.csv) |
| Modul Mamma: Her2neu Status |*Primärdiagnose* `Her2NeuStatus` | [her2neu.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/her2neu.csv) |
| Modul Mamma: Hormonrezeptorstatus |*Primärdiagnose* `HormonrezeptorStatus_Oestrogen`, *Primärdiagnose* `HormonrezeptorStatus_Progesteron` | [hormonrezeptor.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/hormonrezeptor.csv) |
| [Todesursache, Grundleiden nach ICD-10](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#todesursache-grundleiden-nach-icd-10) |*Todesursachen* `Code` | [icd10_todesursache.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/icd10_todesursache.csv) |
| Ausgabe der ICD-10 |*Todesursachen* `Version`, *Primärdiagnose* `Diagnose_ICD10_Version` | [icd10_version.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/icd10_version.csv) |
| [Diagnose nach ICD-10](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#diagnose-nach-icd-10) |*Primärdiagnose* `Diagnose_ICD10_Code` | [icd10.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/icd10.csv) |
| Angabe zur Kontaktbestrahlung |*Strahlentherapie* `Interstitiell_endokavitaer` | [interstitiell.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/interstitiell.csv) |
| [Wohnort bei Diagnose](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#wohnort-bei-diagnose) |*Primärdiagnose* `Inzidenzort` | [landkreis.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/landkreis.csv) |
| Modul Mamma: Menopausenstatus |*Primärdiagnose* `Praetherapeutischer_Menopausenstatus` | [menopausenstatus.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/menopausenstatus.csv) |
| Typ der metabolischen Strahlentherapie |*Strahlentherapie* `Metabolisch_Typ` | [metabolisch.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/metabolisch.csv) |
| Quelle Morphologie |*Primärdiagnose* `Morphologie_Version` | [morphologie_version.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/morphologie_version.csv) |
| Morphologie |*Primärdiagnose* `Morphologie_Code` | [morphologie.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/morphologie.csv) |
| Intention der OP |*Operation* `Intention` | [op_intention.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/op_intention.csv) |
| [Operationen- und Prozedurenschlüssel (OPS)](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#operationen--und-prozedurenschlüssel-ops) |*Operation* `Code` | [ops.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/ops.csv) |
| [Therapieprotokoll](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#therapieprotokoll) |*Systemische Therapie* `Protokoll_TypProtokollschluessel_Code` | [protokoll.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/protokoll.csv) |
| Ausführung der perkutanen Radiochemotherapie |*Strahlentherapie* `Radiochemo` | [radiochemo.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/radiochemo.csv) |
| Modul Darm: Mutation K-ras-Onkogen |*Primärdiagnose* `RASMutation` | [rasmutation.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/rasmutation.csv) |
| Dosisleistung Kontaktbestrahlung |*Strahlentherapie* `Rate_Type` | [rate_type.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/rate_type.csv) |
| Körperseite der bestrahlten Region |*Strahlentherapie* `Seite_Zielgebiet` | [seite_zielgebiet.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/seite_zielgebiet.csv) |
| Seitenlokalisation bei paarigen Organen |*Primärdiagnose* `Seitenlokalisation` | [seitenlokalisation.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/seitenlokalisation.csv) |
| Intention der Strahlentherapie |*Strahlentherapie* `Intention` | [st_intention.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/st_intention.csv) |
| Bezug Strahlentherapie - OP |*Strahlentherapie* `Stellung_OP` | [st_op_stellung.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/st_op_stellung.csv) |
| Angabe zur perkutanen Strahlentherapie |*Strahlentherapie* `Stereotaktisch` | [stereotaktisch.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/stereotaktisch.csv) |
| [Verwendete Substanzen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#verwendete-substanzen) |*Systemische Therapie* `TypeOfSYST_TypSubstanz` | [substanz.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/substanz.csv) |
| Intention der systemischen Therapie |*Systemische Therapie* `Intention` | [syst_intention.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/syst_intention.csv) |
| Bezug systemische Therapie - OP |*Systemische Therapie* `Stellung_OP` | [syst_op_stellung.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/syst_op_stellung.csv) |
| Art der systemischen Therapie |*Systemische Therapie* `Therapieart` | [therapieart.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/therapieart.csv) |
| TNM-Ausgabe |*Primärdiagnose* `TNM_Auflage_c`, *Primärdiagnose* `TNM_Auflage_p`, *Folgeereignis* `Version` | [tnm_auflage.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_auflage.csv) |
| TNM-Präfix (c, p, u) |*Primärdiagnose* `c_p_u_Praefix_T_c`, *Primärdiagnose* `c_p_u_Praefix_N_c`, *Primärdiagnose* `c_p_u_Praefix_M_c`, *Primärdiagnose* `c_p_u_Praefix_T_p`, *Primärdiagnose* `c_p_u_Praefix_N_p`, *Primärdiagnose* `c_p_u_Praefix_M_p`, *Folgeereignis* `c_p_u_Praefix_T`, *Folgeereignis* `c_p_u_Praefix_N`, *Folgeereignis* `c_p_u_Praefix_M` | [tnm_cpu.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_cpu.csv) |
| TNM: Lymphgefäßinvasion |*Primärdiagnose cTNM* `L_p`, *Primärdiagnose pTNM* `L_p`, *Folgeereignis* `L` | [tnm_l.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_l.csv) |
| TNM: Fernmetastasierung |*Primärdiagnose cTNM* `M_c`, *Primärdiagnose pTNM* `M_p`, *Folgeereignis* `M` | [tnm_m.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_m.csv) |
| [TNM: Regionäre Lymphknotenmetastasierung](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#tnm-regionäre-lymphknotenmetastasierung) |*Primärdiagnose cTNM* `N_c`, *Primärdiagnose pTNM* `N_p`, *Folgeereignis* `N` | [tnm_n.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_n.csv) |
| TNM: Perineuralinvasion |*Primärdiagnose cTNM* `Pn_c`, *Primärdiagnose pTNM* `Pn_p`, *Folgeereignis* `Pn` | [tnm_pn.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_pn.csv) |
| TNM: Serumtumormarker |*Primärdiagnose cTNM* `S_c`, *Primärdiagnose pTNM* `S_p`, *Folgeereignis* `S` | [tnm_s.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_s.csv) |
| TNM: Ausdehnung des Primärtumors |*Primärdiagnose cTNM* `T_c`, *Primärdiagnose pTNM* `T_p`, *Folgeereignis* `T` | [tnm_t.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_t.csv) |
| TNM: UICC-Stadium |*Primärdiagnose cTNM* `UICC_Stadium_c`, *Primärdiagnose pTNM* `UICC_Stadium_p`, *Folgeereignis* `UICC_Stadium` | [tnm_uicc.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_uicc.csv) |
| TNM: Veneninvasion |*Primärdiagnose cTNM* `V_c`, *Primärdiagnose pTNM* `V_p`, *Folgeereignis* `V` | [tnm_v.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_v.csv) |
| Ausgabe der ICD-O |*Primärdiagnose* `Topographie_Version` | [topographie_version.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/topographie_version.csv) |
| [ICD-O Topographie](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#icd-o-topographie) |*Primärdiagnose* `Topographie_Code` | [topographie.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/topographie.csv) |
| Verlauf: Fernmetastasierung |*Folgeereignis* `Verlauf_Tumorstatus_Fernmetastasen` | [verlauf_fern.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/verlauf_fern.csv) |
| Verlauf: Lokaler Tumorstatus |*Folgeereignis* `Verlauf_Lokaler_Tumorstatus` | [verlauf_lokal.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/verlauf_lokal.csv) |
| Verlauf: Regionärer Lymphknotenstatus |*Folgeereignis* `Verlauf_Tumorstatus_Lymphknoten` | [verlauf_lymphe.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/verlauf_lymphe.csv) |
| Zielgebiet Strahlentherapie oBDS2014 |*Strahlentherapie Perkutan* `CodeVersion2014`, *Strahlentherapie Kontakt* `CodeVersion2014`, *Strahlentherapie Metabolisch* `CodeVersion2014`, *Strahlentherapie Sonstige* `CodeVersion2014`, *Strahlentherapie Unbekannt* `CodeVersion2014` | [zielgebiet_2014.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/zielgebiet_2014.csv) |
| Zielgebiet Strahlentherapie oBDS2021 |*Strahlentherapie Perkutan* `CodeVersion2021`, *Strahlentherapie Kontakt* `CodeVersion2021`, *Strahlentherapie Metabolisch* `CodeVersion2021`, *Strahlentherapie Sonstige* `CodeVersion2021`, *Strahlentherapie Unbekannt* `CodeVersion2021` | [zielgebiet_2021.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/zielgebiet_2021.csv) |

#### Datumsangaben

Die Angabe *Tag* wird von den Registern grundsätzlich *nicht* ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format `Jahr-Monat-Tag` vorliegt. Für jede Datumsangabe im Datensatz liegen jeweils zwei Variablen vor:

- das *Datum* im internationalen Datumsformat (ISO 8601) `yyyy-mm-dd` und
- die *Genauigkeit* des Datums in einer von drei möglichen Ausprägungen (`M`, `T`, `V`):
  `M` = nur das Jahr ist bekannt (jahrgenau)
  `T` = Jahr und Monat sind bekannt (monatsgenau)
  `V` = Jahr und Monat wurden geschätzt

#### Ergänzungen zu den Referenztabellen

In diesem Abschnitt werden ergänzende Informationen zu den Inhalten der [Referenztabellen](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#referenztabellen) bereitgestellt.

##### Diagnose nach ICD-10

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-10-GM (Version 2008) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html), unter Verwendung der [Empfehlungen des GKV-Spitzenverbands für die klinische Krebsregistrierung (Stand: 14.05.2020)](https://www.gkv-spitzenverband.de/krankenversicherung/qualitaetssicherung_2/klinisches_krebsregister.jsp) und unter Verwendung des [Umsetzungsleitfadens der Plattform § 65c (Stand: 15.11.2023)](https://plattform65c.atlassian.net/wiki/spaces/UMK/pages/15532944/Meldepflichtige+Diagnosen+nach+ICD).  
Die Nutzungsbedingungen der ICD-10 des BfArM sind [hier](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Kontextmaterialien/Nutzungsbedingungen_bfarm_tou_icd10_ops.pdf) hinterlegt.

> [Klassifikationen/icd10.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/icd10.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10-Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10-Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z. B. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  ICD-10-Diagnoseschlüssel, 3-stellig |
| epi_valide| Boolean | `TRUE`, `FALSE`  | Information, ob die Diagnose im [epidemiologischen Datensatz](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/Informationen_datensatz/epidemiologischer_datensatz/epidemiologischer_datensatz_node.html) des ZfKD enthalten ist |
| p65_valide| Boolean| `TRUE`, `FALSE`  | Es besteht eine Meldepflicht für den klinischen Datensatz (lt. Plattform § 65c-Umsetzungsleitfaden). |

##### Todesursache, Grundleiden nach ICD-10

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-10-GM (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html). Die Nutzungsbedingungen der ICD-10 des BfArM sind [hier](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Kontextmaterialien/Nutzungsbedingungen_bfarm_tou_icd10_ops.pdf) hinterlegt.

Um die internationale Vergleichbarkeit zu gewährleisten, ist für die [Verschlüsselung von Todesursachen die ICD-10-WHO](https://www.bfarm.de/DE/Kodiersystemehttps://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/ICD/ICD-10-WHO/Todesursachenstatistik/_node.html) vorgesehen. Aktuell wird bei der Übermittlung von Todesursachen ans ZfKD vorwiegend (noch) die Verwendung der ICD-10-GM angegeben.

> [Klassifikationen/icd10_todesursache.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/icd10_todesursache.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10-Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10-Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z. B. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  ICD-10-Diagnoseschlüssel, 3-stellig |
| chapter   | Integer | z. B. `1`  |  ICD-10-Kapitelnummer |


##### ICD-O Topographie

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der [ICD-O-3 (2. Revision, Version 2019) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html) und unter Zuhilfenahme des [Umsetzungsleitfadens der Plattform § 65c (Stand: 15.11.2023)](https://plattform65c.atlassian.net/wiki/spaces/UMK/pages/15533189/Paarige+Organe).
Die Nutzungsbedingungen der ICD-O-3 des BfArM sind [hier](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Kontextmaterialien/Nutzungsbedingungen_bfarm_tou_icdo3.pdf) hinterlegt.

Für paarige Organe (Ausprägung *istPaarig* = `1`, lt. Plattform § 65c-Umsetzungsleitfaden) wird bei der Variable *Seitenlokalisation* die Angabe der betroffenen Körperseite(n) erwartet.

> [Klassifikationen/topographie.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/topographie.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id        | String | z. B. `C021`  | ICD-10 Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt |
| code      | String | z. B. `C02.1`  | ICD-10 Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt |
| name      | String | z. B. `Bösartige Neubildung...`  | Beschreibung der Diagnose  |
| id3       | String | z. B. `C02`  |  3-stelliger Diagnoseschlüssel |
| istPaarig   | Integer | z. B. `1`  |  1 = es handelt sich um ein paariges Organ und es wird bei der Variable *Seitenlokalisation* die Angabe der betroffenen Körperseite(n) erwartet. |


##### Operationen- und Prozedurenschlüssel (OPS)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung des [Operationen- und Prozedurenschlüssels (OPS) (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM)](https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html). Die Nutzungsbedingungen der Operationen- und Prozedurenschlüssels (OPS) des BfArM [hier](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Kontextmaterialien/Nutzungsbedingungen_bfarm_tou_icd10_ops.pdf) hinterlegt.

> [Klassifikationen/ops.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/ops.csv)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| id | String | z. B. `1-202`  | ID, maximal 6-stellig |
| chapter | Integer | z. B. `1`  | OPS-Kapitel |
| group | String | z. B. `1-20 - 1-33`  | OPS-Gruppe, -Bereich |
| code3 | String | z. B. `1-20`  | OPS-Kategorie/-Kode, 3-stellig |
| code | String | z. B. `1-202`  | OPS-Kategorie/-Kode, 4-stellig |
| code5 | String | z. B. `1-202.-`  | OPS-Kategorie/-Kode, 5-stellig |
| code6 | String | z. B. `1-202.--`  | OPS-Kategorie/-Kode, 6-stellig |
| name | String | z. B. `Diagnostik zur Feststellung ...`  | Klassentitel der Maßnahme |

##### Substanzen

Die Erstellung der Referenztabelle erfolgte unter Verwendung des [Umsetzungsleitfadens der Plattform § 65c](https://plattform65c.atlassian.net/wiki/spaces/UMK/pages/15532506/Substanzen) in der Version 2021. Die dort hinterlegte Tabelle wurde für unsere Zwecke in folgenden Schritten geringfügig überarbeitet:

- der Eintrag `Larotrectinib` lag als Duplikat vor, dies wurde korrigiert
- die Spalte `Code` wurde ergänzt, hier sind gültige ATC-Codes verknüpft, sofern anwendbar
- für die Zuordnung der ATC-Codes wurde auf das Kapitel `L` beschränkt (_Antineoplastic and immunomodulating agents_)

> [Klassifikationen/substanz.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/substanz.csv)

Für die Verknüpfung von Substanzbezeichnung und ATC-Code wurde auf die ATC-Klassifikation für den deutschen Arzneimittelmarkt zurückgegriffen:
>[GKV-Arzneimittelindex im Wissenschaftlichen Institut der AOK (WIdO), AOK Bundesverband GbR Stand 04/2023](https://www.wido.de/publikationen-produkte/analytik/arzneimittel-klassifikation/)

Variablen und Ausprägungen der Referenztabelle:

| Variable  | Typ | Ausprägungen | Beschreibung |
| --------- | --- | ------------ | ------------ |
| Therapieart | String | z. B. `HO`  | Art der Therapie |
| Substanz| Sting | z. B. `Abacavir`  | Bezeichnung des Arzneimittels |
| Code | String | z. B. `J05AF06`  | ATC-Kode, Ebene 5 |

##### Therapieprotokoll

Bei der verwendeten Referenztabelle handelt es sich um eine *Vorschlagsliste* der [Plattform § 65c](https://confluence.basisdatensatz.de/display/UMK/Protokolle). Diese Vorschlagsliste stellt keine verbindliche Festlegung dar. Ein anerkannter Standard für die Kodierung von Systemtherapie-Protokollen ist uns nicht bekannt. Vorschläge für eine standardisierte Nomenklatur ([Rubinstein et al, 2020](https://doi.org/10.1200/CCI.19.00122)), Referenzsysteme ([HemOnc.org](https://hemonc.org/), [National Cancer Institute Thesaurus (NCIT)](https://bioportal.bioontology.org/ontologies/NCIT/?p=classes&conceptid=http%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23C62634)) und kommerzielle Produkte für die medizinische Dokumentation ([Onkopti®](https://onkopti.de/protokollsuche/)) wurden von anderen entwickelt. Wir verweisen hier auf eine Auswahl dieser Arbeiten und Systeme.

> Rubinstein, S. M., Yang, P. C., Cowan, A. J., & Warner, J. L. (2020). Standardizing Chemotherapy Regimen Nomenclature: A Proposal and Evaluation of the HemOnc and National Cancer Institute Thesaurus Regimen Content. JCO clinical cancer informatics, 4, 60–70. [https://doi.org/10.1200/CCI.19.00122](https://doi.org/10.1200/CCI.19.00122)  
> [Onkopti® – die Datenbank digitalisierter onkologischer Therapieprotokolle](https://onkopti.de/protokollsuche/)

##### TNM: Regionäre Lymphknotenmetastasierung

Die Variable beschreibt den Status der regionären Lympknotenmetastasierung (N-Kategorie der TNM).

> [Klassifikationen/tnm_n.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/tnm_n.csv)

###### Zusatz (1mi), Mammakarzinom

Anwendung bei: Mikrometastase(n), > 0,2 mm und/oder mehr als 200 Tumorzellen, aber nicht größer als 0,2 cm
Stadium IB nach TNM8: T0, T1 N1mi M0

> Quellen:
[Kapitel  11.3, Interdisziplinäre S3-Leitlinie für die Früherkennung, Diagnostik, Therapie und Nachsorge des Mammakarzinoms (2021)](https://www.leitlinienprogramm-onkologie.de/leitlinien/mammakarzinom/); 
[TNM Classification of Malignant Tumours, 8th edition](https://www.wiley.com/en-gb/TNM+Classification+of+Malignant+Tumours%2C+8th+Edition-p-9781119263579)

###### Zusatz (sn)

| Ausprägung | Beschreibung |
| ---------- | ------------ |
| `(p)NX(sn)` | Schildwächterlymphknoten kann histologisch nicht beurteilt werden |
| `(p)N0(sn)` | Histologisch keine Lymphknotenmetastasen in Schildwächterlymphknoten |
| `(p)N1(sn)` | Befall des (der) Schildwächterlymphknoten |

> Quelle: [TNM Classification of Malignant Tumours, 8th edition](https://www.wiley.com/en-gb/TNM+Classification+of+Malignant+Tumours%2C+8th+Edition-p-9781119263579)

###### Zusatz (i+), (mol+)

| Ausprägung | Beschreibung |
| ---------- | ------------ |
| `(p)N0` | Histologisch keine Lymphknotenmetastasen, keine Untersuchung zum Nachweis isolierter Tumorzellen | 
| `(p)N0(i–)` | Histologisch keine Lymphknotenmetastasen, kein morphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(i+)` | Histologisch keine Lymphknotenmetastasen, morphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(mol–)` | Histologisch keine Lymphknotenmetastasen, kein nichtmorphologischer Nachweis von isolierten Tumorzellen |
| `(p)N0(mol+)`| Histologisch keine Lymphknotenmetastasen, nicht-morphologischer Nachweis von isolierten Tumorzellen |

> Quelle: [TNM Classification of Malignant Tumours, 8th edition](https://www.wiley.com/en-gb/TNM+Classification+of+Malignant+Tumours%2C+8th+Edition-p-9781119263579)

##### Wohnort bei Diagnose

Angegeben ist hier der Wohnort zum Zeitpunkt der Diagnosestellung auf Basis des Amtlichen Gemeindeschlüssels [(AGS)](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html). Verwendet werden die ersten 5 Ziffern des AGS, was der Landkreisebene entspricht.
In Abwandlung der amtlichen Daten sind in der Liste alle Regionen konsistent als 5-Steller kodiert. Konkret werden die 3-stelligen AGS der Regierungsbezirke um `99` ergänzt, die 2-stelligen AGS der Bundesländer um `099`.

> [Klassifikationen/landkreis.csv](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Klassifikationen/landkreis.csv)

> Quelle: angepasste Auflistung auf Basis von Daten des Bundesamtes für Kartographie und Geodäsie [BKG](https://gdz.bkg.bund.de/). Abruf der amtlichen Daten: [link](https://sg.geodatenzentrum.de/web_public/gdz/dokumentation/deu/vg5000.pdf). Datenstand: 31.12.2019

| Ausprägung | Beschreibung |
| ---------- | ------------ |
| `RS` | erste 5 Ziffern des AGS, tlw. umkodiert |
| `GEN` | Geografischer Name |
| `NUTS` | Europäischer Statistikschlüssel |
| `WSK` | Datum der Wirksamkeit |

### Beispieldaten

In diesem Repository soll der Bereitstellungsprozess für klinische Daten veranschaulicht werden.

Zum einen ist ein XML-Rohdatensatz hinterlegt für die Lieferung der Daten aus den klinischen Krebsregistern der Länder. Dieser entspricht den gemeinsam erarbeiteten Vorgaben des `oBDS-RKI` und wird im ZfKD zu einem deutschlandweiten Gesamtdatensatz verarbeitet. Der "rohe" Datensatz bestehend aus XML-Daten und bildet den Ausgangspunkt der weiteren Verarbeitung, wird aber vom ZfKD _nicht_ ausgegeben.

Zum anderen wird hier simuliert, wie eine definierte Teilmenge des verarbeiteten Gesamtdatensatzes auf Antrag übermittelt wird. Zur Veranschaulichung dieser Datenbereitstellung dient der Ordner `Beispieldaten/csv`. Werden im Rahmen einer Antragsverfahren im ZfKD Daten übermittelt, entsprechen diese in Form und Aufbau exakt den hier abgelegten Beispieldateien. Die csv-Dateien in diesem Ordner sind aus dem XML-Rohdatensatz generiert.

Dabei ist zu beachten, dass aufgrund der vielfältigen Beziehungen der Bestandteile im [Datenschema](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#datenschema) die Integration in eine einzelne Tabelle / Datei meist nicht zielführend ist. Es werden daher die angefragten Entitäten als einzelne Tabellen / Dateien exportiert. Die hier verwendeten Identifikatoren können in einem relationalen Modell wieder korrekt zusammengeführt werden (so sind etwa Einträge der Tumortabelle den jeweiligen Patienten zuordenbar). Hilfestellung bei den relationalen Beziehungen bietet das angehangene [ER-Modell](/.github/images/2023-09-28_Entity-Relationship-Modell.jpg), als strukturiertes Konzept zur Darstellung und Analyse von Daten in einer Datenbank.

> 💡 Die in den Beispieldateien hinterlegten Daten sind künstlich erzeugt, folgen einfachen Verteilungen und berücksichtigen keine medizinischen Zusammenhänge. Die Identifikatoren sind zufällig erzeugt. Es besteht daher keinerlei Verbindung zu realen Daten.

| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| Rohdatensatz | Ein einfacher Testdatensatz als `.xml`-Datei, bestehend aus Angaben zu 30 fiktiven Patienten. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/xml/oBDS_v3.0.0.8a_RKI_Sample.xml) |
| Applikationsart | Angaben zu Applikationsarten als `.csv` Testdatensatz mit Referenz auf `Bestrahlung`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/applikationsart.csv) |
| Bestrahlung | Angaben zu Bestrahlungen als `.csv` Testdatensatz mit Referenz auf `ST`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/bestrahlung.csv) |
| FM | Angaben zu Fernmetastasen (Tumor) als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/fm.csv) |
| Folgeereignis FM | Angaben zu Fernmetastasen als `.csv` Testdatensatz mit Referenz auf `Folgeereignis`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/folgeereignis_fm.csv) |
| Folgeereignis Weitere Klassifikationen | Angaben zu Weitere Klassifikationen als `.csv` Testdatensatz mit Referenz auf `Folgeereignis`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/folgeereignis_weitere_klassifikation.csv) |
| Folgeereignis | Angaben zu Folgeereignissen als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/folgeereignis.csv) |
| OP | Angaben zu Operationen als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/op.csv) |
| OPS | Angaben zu OP-Kodes als `.csv` Testdatensatz mit Referenz auf `OP`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/ops.csv) |
| Patient | Angaben zu Patienten als `.csv` Testdatensatz. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/patient.csv) |
| Protokoll | Angaben zu Therapieprotokollen als `.csv` Testdatensatz mit Referenz auf `SYST`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/protokoll.csv) |
| ST | Angaben zu Strahlentherapien als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/st.csv) |
| Substanz | Angaben zu Substanzen als `.csv` Testdatensatz mit Referenz auf `SYST`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/substanz.csv) |
| SYST | Angaben zu systemischen Therapien als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/syst.csv) |
| Todesursache | Angaben zu Todesursachen als `.csv` Testdatensatz mit Referenz auf `Patient`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/todesursache.csv) |
| Tumor | Angaben zu Tumoren als `.csv` Testdatensatz mit Referenz auf `Patient`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/tumor.csv) |
| Weitere Klassifikationen | Angaben zu Weitere Klassifikationen als `.csv` Testdatensatz mit Referenz auf `Tumor`. | [💾](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Beispieldaten/csv/weitere_klassifikation.csv) |


<!-- FOOTER_START: {"lang": "de"} -->



### Metadaten  

Zur Erhöhung der Auffindbarkeit sind die bereitgestellten Daten mit Metadaten beschrieben. Über GitHub Actions werden Metadaten an die entsprechenden Plattformen verteilt. Für jede Plattform existiert eine spezifische Metadatendatei, diese sind im Metadatenordner hinterlegt:  

> [Metadaten/](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/tree/main/Metadaten/) 

Versionierung und DOI-Vergabe erfolgt über [Zenodo.org](https://zenodo.org). Die für den Import in Zenodo bereitgestellten Metadaten sind in der [zenodo.json](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Metadaten/zenodo.json) hinterlegt. Die Dokumentation der einzelnen Metadatenvariablen ist unter https://developers.zenodo.org/#representation nachlesbar.
 
> [Metadaten/zenodo.json](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Metadaten/zenodo.json)  

In der zenodo.json ist neben dem Publikationsdatum (`"publication_date"`) auch der Datenstand in folgendem Format enthalten (Beispiel):  

```
  "dates": [
    {
      "start": "2023-09-11T15:00:21+02:00",
      "end": "2023-09-11T15:00:21+02:00",
      "type": "Collected",
      "description": "Date when the Dataset was created"
    }
  ],
```    




## Hinweise zur Nachnutzung der Daten  

Offene Forschungsdaten des RKI werden auf [Zenodo.org](http://Zenodo.org/), [GitHub.com](http://GitHub.com/), [OpenCoDE](https://gitlab.opencode.de) und [Edoc.rki.de](http://Edoc.rki.de/) bereitgestellt:  

- https://zenodo.org/communities/robertkochinstitut  
- https://github.com/robert-koch-institut  
- https://gitlab.opencode.de/robert-koch-institut  
- https://edoc.rki.de/  
 
### Lizenz  

Der Datensatz "Bundesweiter klinischer Krebsregisterdatensatz - Datenschema und Klassifikationen" ist lizenziert unter der [Creative Commons Namensnennung 4.0 International Public License | CC-BY 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.de).  

Die im Datensatz bereitgestellten Daten sind, unter Bedingung der Namensnennung des Robert Koch-Instituts als Quelle, frei verfügbar. Das bedeutet, jede Person hat das Recht die Daten zu verarbeiten und zu verändern, Derivate des Datensatzes zu erstellen und sie für kommerzielle und nicht kommerzielle Zwecke zu nutzen. Weitere Informationen zur Lizenz finden sich in der [LICENSE](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/LICENSE) bzw. [LIZENZ](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/LIZENZ) Datei des Datensatzes.  
<!-- FOOTER_END -->