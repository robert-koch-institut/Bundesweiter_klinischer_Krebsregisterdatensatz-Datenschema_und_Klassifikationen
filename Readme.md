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

In diesem Repository werden begleitende Informationen zur **Struktur** des bundesweiten ZfKD-Datensatzes [bereitgestellt](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen#struktur-des-bundesweiten-klinischen-krebsregisterdatensatzes). Ein weiteres wesentliches Element der Krebsregisterdaten stellen **Klassifikationen** dar - Referenztabellen für Variablen des Datensatzes und ihre definierten Ausprägungen. Diese Tabellen werden durch beteiligte Akteure kontinuierlich harmonisiert. 

> [!NOTE]
> Der ZfKD-Datensatz ist nicht öffentlich zugänglich, kann aber auf Antrag für wissenschaftliche Forschungszwecke genutzt werden. Bitte verwenden Sie für Fragen zur Antragstellung die  E-Mail-Adresse des ZfKD: [krebsdaten@rki.de](mailto:krebsdaten@rki.de)  oder das auf der Internetseite des ZfKD bereitgestellte [Kontaktformular](https://www.krebsdaten.de/SharedDocs/Kontaktformulare/A/Antrag-krebsdaten/Integrator_SCU.html). Informationen zum gesetzlichen Auftrag, zu Methoden und Veröffentlichungen des ZfKD erhalten Sie ebenfalls auf den [Internetseiten des ZfKD](https://www.krebsdaten.de/). Bitte beachten Sie, dass das ZfKD an den Daten, die von den Krebsregistern übermittelt wurden, keine Änderungen vornimmt.

## Informationen zum Entstehungskontext des ZfKD-Datensatzes

Für die Erhebung klinischer Krebsregisterdaten wurde mit dem [Krebsfrüherkennungs- und -registergesetz (KFRG)](https://www.bgbl.de/xaver/bgbl/start.xav?start=//*%5B@attr_id=%27bgbl113s0617.pdf%27%5D#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl113s0617.pdf%27%5D__1697181091765) im [§ 65c Fünftes Buch Sozialgesetzbuch (SGB V)](https://www.gesetze-im-internet.de/sgb_5/__65c.html) ein bundesrechtlicher Rahmen geschaffen. Die von den klinischen Krebsregistern zu erfassenden Angaben werden in dem von der Arbeitsgemeinschaft Deutscher Tumorzentren (ADT) und der Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID, jetzt DKR e.V.) erarbeiteten [onkologischen Basisdatensatz (oBDS)](https://basisdatensatz.de/) spezifiziert und regelmäßig überarbeitet. Die letzte Anpassung des oBDS wurde am 12. Juli 2021 [im Bundesanzeiger publiziert](https://www.bundesanzeiger.de/pub/publication/bRrUsRox5lQ14casCXs/content/bRrUsRox5lQ14casCXs/BAnz%20AT%2012.07.2021%20B4.pdf). Einmal jährlich übermitteln die Krebsregister Daten nach Maßgabe des [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) an das ZfKD.

Seit der Novellierung des BKRG durch das [Gesetz zur Zusammenführung von Krebsregisterdaten](https://www.bgbl.de/xaver/bgbl/start.xav#__bgbl__%2F%2F*%5B%40attr_id%3D%27bgbl121s3890.pdf%27%5D__1697190045694) enthalten die ans ZfKD übermittelten Daten auch klinische Angaben, u. a. zum Krankheitsverlauf und zur Behandlung (ab Diagnosejahr 2020).

Die Inhalte und die Struktur der ans ZfKD zu übermittelnden Daten wurden in einer AG mit Vertretern des ZfKD und der Krebsregister abgestimmt, dabei diente der oBDS und das novellierte Bundeskrebsregisterdatengesetz (§ 5) als Arbeitsgrundlage.

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

### Datenschema

Das Datenschema umfasst mehr als 120 Variablen, die verschiedenen Elementen zugeordnet sind. Die klinischen Daten können nicht in einer einfachen „Rechtecktabelle“ wiedergegeben werden, da sie zum Teil komplexe Krankheitsverläufe abbilden. Im klinischen Datensatz sind die Daten daher in einem verschachtelten XML-Schema strukturiert.  

Der klinische Datensatz wird durch folgende Elemente gegliedert:

- Die _Person_ bildet die grundlegende Einheit im Datensatz.
- Der Person zugeordnet ist mindestens ein Element _Tumor_.
- Das Element _Tumor_ enthält ein verpflichtendes Element _Primärdiagnose_. Dieses enthält u. a. Angaben zum Tumorstadium, zur Histologie und Lokalisation des Tumors.
- Darüber hinaus sind dem Element _Tumor_ mehrere optionale Elemente zugeordnet, in denen Angaben zur Behandlung (Elemente _OP_, _ST_ und _SYST_) und zu Folgeereignissen (Element _Folgeereignis_) wie Remissionen und Rezidiven erfasst werden können.

Bestimmte Variablen sind Pflichtangaben, z. B. das _Geburtsdatum_, der _Inzidenzort_ und der _Diagnoseschlüssel_. Viele Angaben sind optional, z. B. die den Elementen cTNM und pTNM zugeordneten Variablen (_T-Kategorie_, _UICC-Stadium_, _m-Suffix_ usw.). Einige Angaben sind nur unter der Bedingung verpflichtend, dass das übergeordnete, optionale Element verwendet wird: Beispielsweise ist das Element Histologie optional. Wird jedoch in der zugehörigen Variable _Morphologie_ ein Eintrag vorgenommen, ist auch eine Angabe zum _Grading_ verpflichtend. Angaben zur Zahl untersuchter Lymphknoten bleiben optional.

Bei Auswertungen ist zu beachten, dass optionale Inhalte möglicherweise nicht gleichermaßen aus allen Bundesländern vorliegen.

Die Elemente _Primärdiagnose_, _Folgeereignis_, _OP_, _ST_ und _SYST_ können mehrfach verwendet werden, so dass auch komplexe Krankheitsverläufe abgebildet werden können. Die Inhalte eines Elements können in ein tabellarisches Format überführt und über eine fallbezogene Nummer mit anderen Tabellen aus dem Datensatz verknüpft werden. Auf diese Weise entsteht ein auswertbares Format, in dem die bewilligten Daten an den Datenempfänger übermittelt werden können..  

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

Eine vollständige und maschinenlesbare Repräsentation des gesamten Datenschemas mit allen Details wird über das [XML-Schema](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/oBDS_v3.0.0.8a_RKI_Schema.xsd) bereitgestellt.

XML (Extensible Markup Language)-Schemata definieren den erlaubten Aufbau der ihnen zugeordneten XML-Dokumente. XML ist eine Auszeichnungssprache mit definierter Struktur und Syntax. XML-Dokumente sind textbasiert und repräsentieren Daten in einer hierarchischen und strukturierten Weise. Der Hauptzweck von XML besteht darin, Daten so zu beschreiben, dass sie sowohl für Menschen als auch für Maschinen leicht verständlich und interpretierbar sind.

Ein XML-Schema, oft auch als XSD (XML Schema Definition) bezeichnet, bietet einen Rahmen zur Beschreibung der Struktur und Datentypen eines XML-Dokuments. XML-Schemata legen fest, welche Elemente und Attribute in einem XML-Dokument erscheinen können, wie diese strukturiert und organisiert sind und welche Datentypen sie enthalten können. XML-Schemata können dazu verwendet werden, um XML-Dokumente zu validieren. Hierbei wird überprüft, ob ein XML-Dokument der im Schema definierten Struktur entspricht.

Detaillierte technische Informationen zum abgestimmten XML-Schema sind auf der [Internetseite der Plattform § 65c abrufbar](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/2064400/XML-Schema) (bis Version `3.0.0.8a_RKI`).

Protokollierte Änderungen am Datenschema sind in den beigefügten [Release Notes](release-notes.md) der Versionen zu finden.

![Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes
Die obenstehende Abbildung veranschaulicht die Struktur des klinischen Datensatzes. ](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/.github/images/2023-06-28_XML-Schema_grob.png)
> Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes. Quelle: eigene Darstellung.

### Klassifikationen

Die im Datenschema verwendeten Klassifikationen erfahren regelmäßige Änderungen. Damit die jeweiligen Arbeitsstände in automatisierten Prozessen abgerufen werden können, sind die Klassifikationen in einem eigenen, englischsprachigen [Repository](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references) zur Verfügung gestellt. Die dem Datenschema entsprechenden Referenztabellen sind im Repository unter [`docs/readme-tables.md`](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/main/docs/readme-tables.md) verfügbar.

> https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references

### Beispieldaten

Um die beim ZfKD beantragbaren Daten praktisch einschätzen zu können werden konforme Beispieldaten zur Verfügung gestellt, und können in Form einer [transportablen Datenbank](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-generator) abgerufen werden. Die Struktur dieser Beispieldaten ist exakt deckungsgleich mit den klinischen Krebsregisterdaten. Eine detaillierte Darstellung der dazu verwendeten [Tabellen und Relationen](https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-references/-/blob/main/docs/readme-dataset.md) erklärt, wie die Daten verknüpft werden können.

> https://gitlab.opencode.de/robert-koch-institut/zentrum-fuer-krebsregisterdaten/cancerdata-generator

<!-- FOOTER_START: {"lang": "de"} -->

### Metadaten  

Zur Erhöhung der Auffindbarkeit sind die bereitgestellten Daten mit Metadaten beschrieben. Über GitHub Actions werden Metadaten an die entsprechenden Plattformen verteilt. Für jede Plattform existiert eine spezifische Metadatendatei, diese ist im Metadatenordner hinterlegt:  

> [Metadaten/](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/tree/main/Metadaten/) 

Versionierung und DOI-Vergabe erfolgen über [Zenodo.org](https://zenodo.org). Die für den Import in Zenodo bereitgestellten Metadaten sind in der [zenodo.json](https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen/blob/main/Metadaten/zenodo.json) hinterlegt. Die Dokumentation der einzelnen Metadatenvariablen ist unter https://developers.zenodo.org/#representation nachlesbar.
 
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
