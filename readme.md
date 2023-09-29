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

## Einleitung (inkl. Abtract)

Das Zentrum für Krebsregisterdaten (ZfKD) führt nach Vorgabe des [Bundeskrebsregisterdatengesetzes (BKRG)](https://www.gesetze-im-internet.de/bkrg/BJNR270700009.html) Daten der Landeskrebsregister zu einem bundesweiten klinischen Datensatz zusammen und stellt sie [auf Antrag für wissenschaftliche Forschungsprojekte](https://www.krebsdaten.de/info_antrag) zur Verfügung.  

> 💡 Der onkologischen Basisdatensatz des RKI selbst ist nicht öffentlich zugänglich, kann aber auf Antrag für wissenschaftliche Forschungszwecke genutzt werden. Bitte verwenden Sie für Fragen zur Antragstellung das auf der Internetseite des ZfKD bereitgestellte [Kontaktformular](https://www.krebsdaten.de/SharedDocs/Kontaktformulare/A/Antrag-krebsdaten/Integrator_SCU.html). Informationen zum gesetzlichen Auftrag, zu Methoden und Veröffentlichungen des ZfKD erhalten Sie ebenfalls auf den [Internetseiten des ZfKD](https://www.krebsdaten.de/)

Im vorliegenden Datensatz stellen wir _Metadaten_ und begleitende Informationen zur [Struktur](#struktur-des-datensatzes) und zu [Inhalten](#inhalte-des-datensatzes) des bundesweiten klinischen Krebsregisterdatensatz (auch onkologischer Basisdatensatz des RKIs) zur Verfügung: 

- **Schema-Dateien** des Datensatzes in verschieden Formaten, näheres [hier](#struktur-des-datensatzes)
- **Klassifikationen**: Referenztabellen für Variablen des Datensatzes und ihre definierten Ausprägungen, näheres [hier](#inhalte-des-datensatzes)
- **Kontexmaterialien**: Einige Referenztabellen geben Inhalte von Standards wieder, die von Dritten (z. B. BfArM, WIdO) herausgegeben werden. Unter Umständen verbinden diese Anbieter die Nutzung ihrer Produkte mit Bedingungen. Die Nutzungsbedingungen sind hier abgelegt. Wir bitten Sie diese zu beachten.
- **Beispieldaten**: Ordner zur Veranschaulichung des Bereitstellungsprozesses der Daten. Näheres unter [Beispieldaten](#beispieldaten)


## Informationen zum Datensatz und Entstehungskontext


- hier informationen zu den Krebsregistern, dem Zfkd und wie der Datensatz zustande gekommen ist. rechtliche Grundlagen etc. 
- Verhältniss der Landes KR zum ZFKD


### Adminstrative und Organisatorische Angaben

- rolle des ZFKD 
- Ansprechpartner:innen

## Datenerhebung und Übermittlung

- kurze Einleitung

### Datenerhebung

- Datenherhebung in den Kliniken und übermittlung an die LKR

### Datenübermittlung an das ZfKD



#### Verpflichtende und optionale Angaben

Bestimmte Variablen sind Pflichtangaben, z. B. das _Geburtsdatum_, der _Inzidenzort_ und der _Diagnoseschlüssel_. Viele Angaben sind optional, z. B. die den Elementen cTNM und pTNM zugeordneten Variablen (_T-Kategorie_, _UICC-Stadium_, _m-Suffix_ usw.). Einige Angaben sind nur unter der Bedingung verpflichtend, dass das übergeordnete, optionale Element verwendet wird: Beispielsweise ist das Element Histologie optional. Wird jedoch in der zugehörigen Variable _Morphologie_ ein Eintrag vorgenommen, ist auch eine Angabe zum _Grading_ verpflichtend. Angaben zur Zahl untersuchter Lymphknoten bleiben optional.

Zusammenhänge und Abhängigkeiten zwischen den Variablen veranschaulicht die im [Downloadbereich](#downloads) verfügbare Abbildung.

Bei Auswertungen ist zu beachten, dass optionale Inhalte möglicherweise nicht gleichermaßen aus allen Bundesländern vorliegen.


### Datenauswertung

- wenn, wie werden die Daten für den Datensatz transformiert 

## Struktur des okologischen Basisdatensatzes  

Das Datenschema umfasst mehr als 120 Variablen, die verschiedenen Elementen zugeordnet sind (siehe [Struktur](#struktur-des-datensatzes)).

Die klinischen Daten werden nicht - wie ursprünglich die [epidemiologischen Daten des ZfKD](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/Informationen_datensatz/epidemiologischer_datensatz/epidemiologischer_datensatz_node.html) (basierend auf dem BKRG in seiner Fassung vom 18.08.2009) - in einer einfachen „Rechtecktabelle“ abgebildet, in der Erkrankungsfälle als Zeilen und Variablen als Spalten dargestellt sind. Im klinischen Datensatz sind die Daten in einem verschachtelten XML-Schema strukturiert.

Der klinische Datensatz wird durch folgende Elemente gegliedert:

- Die _Person_ bildet die grundlegende Einheit im Datensatz.
- Der Person zugeordnet ist mindestens ein Element _Tumor_.
- Das Element _Tumor_ enthält ein verpflichtendes Element _Primärdiagnose_. Dieses enthält u. a. Angaben zum Tumorstadium, zur Histologie und Lokalisation des Tumors.
- Darüber hinaus sind dem Element _Tumor_ mehrere optionale Elemente zugeordnet, in denen Angaben zur Behandlung (Elemente _OP_, _ST_ und _SYST_) und zu Folgeereignissen (Element _Folgeereignis_) wie Remissionen und Rezidiven erfasst werden können.

Die Elemente _Primärdiagnose_, _Folgeereignis_, _OP_, _ST_ und _SYST_ können mehrfach verwendet werden, so dass auch komplexe Krankheitsverläufe abgebildet werden können. Die Inhalte eines Elements können in ein tabellarisches Format überführt und über eine fallbezogene Nummer mit anderen Tabellen aus dem Datensatz verknüpft werden. Auf diese Weise entsteht ein auswertbares Format, in dem die bewilligten Daten an den Datenempfänger übermittelt werden können (beispielsweise als `.csv`).

![Abbildung: Vereinfachtes Datenschema (mit ausgewählten Variablen). Quelle: [krebsdaten.de](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/forschungsdatensatz_node.html).](/.github/images/2023-06-30_Datenschema_einfach.png)

### Downloads

An dieser Stelle können die XML-Schema-Definition und weitere ergänzende Dateien zur Datensatz-Struktur heruntergeladen werden.

| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| XML-Schema | Die XML-Schema-Definition `.xsd` als eindeutige, vollständige und maschinenlesbare Repräsentation des gesamten Schemas mit allen Details. Zur Betrachtung der Inhalte dieser Datei ist die Verwendung einer geeigneten Software empfohlen. Detaillierte [technische Informationen zum XML-Schema](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/2064400/XML-Schema) sind auf der Internetseite der Plattform § 65c abrufbar (bis Version `3.0.0.8_RKI`). | [💾](/oBDS_v3.0.0.8a_RKI_Schema.xsd) |
| CSV-Schema | Variablen und mögliche Ausprägungen in tabellarischer Darstellung als `.csv`. | [💾](/oBDS_v3.0.0.8a_Variablen.csv) |
| PDF-Schema | Die grafische Darstellung des XML-Schemas als `.pdf`. Nicht alle Elemente sind abgebildet. Hinweise zur Notation des XML-Schemas sind [hier](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/59015169/Legende+zur+grafischen+Notation+des+XML-Schemas) zu finden. | [💾](/oBDS_v3.0.0.8a_Schema.pdf) |

### XML-Schema 

as [XML-Schema](#xml-schema) des klinischen Datensatzes wird als `oBDS-RKI` bezeichnet. Die Bezeichnung geht zurück auf den zwischen der Arbeitsgemeinschaft Deutscher Tumorzentren e. V. (ADT), der Gesellschaft der epidemiologischen Krebsregister in Deutschland (GEKID) und der Plattform § 65c abgestimmten `einheitlichen onkologischen Basisdatensatz` (`oBDS`), der für die Entwicklung des `oBDS-RKI` als Vorlage und Arbeitsgrundlage diente. An der Entwicklung des `oBDS-RKI` waren Vertreterinnen und Vertreter der Plattform § 65c, der ADT, der GEKID und des ZfKD beteiligt.

Weil er die Struktur und Inhalte der von den Landeskrebsregistern ans ZfKD zu liefernden Daten definiert, wird der `oBDS-RKI` auch als `ZfKD-Lieferdatensatz` bezeichnet.

Näheres zur Abstimmung und Entwicklung des klinischen Datensatzes erfahren Sie auf den Internetseiten der [Plattform § 65c](https://plattform65c.atlassian.net/wiki/spaces/P6/overview).

![Abbildung: Übersicht zum XML-Schema des klinischen Datensatzes
Die obenstehende Abbildung veranschaulicht die Struktur des klinischen Datensatzes. ](/.github/images/2023-06-28_XML-Schema_grob.png)

### Release Notes

Die release notes zu den Versionen des XML-Schemas sind [hier](release-notes.md) zu finden

## Klassifikationen

Die für einzelne Variablen erwarteten Ausprägungen und ihre Beschreibung sind in [Referenztabellen](#referenztabellen) hinterlegt. Einzelne Referenzen werden für mehrere Variablen genutzt: Beispielsweise wird für den Östrogen-Rezeptorstatus und den Progesteron-Rezeptorstatus die gleiche Kodierung verwendet. Ebenso werden für die Angaben zur klinischen und pathologischen TNM die gleichen Referenztabellen genutzt.

Größtenteils handelt es sich bei den Referenzen um Vereinbarungen, die bei der Erarbeitung des ZfKD-Lieferdatensatzes getroffen wurden (z. B. Ausprägungen von Variablen im Element Strahlentherapie, Ausprägungen von _Diagnosesicherung_). Teilweise handelt es sich bei den Referenzen um internationale oder nationale Standards (z. B. TNM, ATC-Klassifikation für den deutschen Arzneimittelmarkt). Informationen zu Quelle und Version der jeweiligen Referenzwerte, zu ihrer Interpretation und zu gegebenenfalls bestehenden Nutzungsbedingungen der Herausgeber sind im Abschnitt [Details](#details) zusammengestellt.

### Referenztabellen

| Tabelle | Eigenschaft | verwendet für *Element* `technische Variablenbezeichnung` |
| --- | --- | --- |
| [atemgetriggert.tsv](/Klassifikationen/atemgetriggert.tsv) | Angabe zur perkutanen Strahlentherapie | _Strahlentherapie_ `Atemgetriggert` |
| [beurteilung_gesamt.tsv](/Klassifikationen/beurteilung_gesamt.tsv) | Folgeereignis - Gesamtbeurteilung Tumorstatus | _Folgeereignis_ `Gesamtbeurteilung_Tumorstatus` |
| [beurteilung_lokal.tsv](/Klassifikationen/beurteilung_lokal.tsv) | Folgeereignis - Beurteilung Primärtumor | _Folgeereignis_ `Verlauf_Lokaler_Tumorstatus` |
| [diagnosesicherung.tsv](/Klassifikationen/diagnosesicherung.tsv) | Wertigkeit der Diagnosesicherung | _Primärdiagnose_ `Diagnosesicherung` |
| [fm_lokalisation.tsv](/Klassifikationen/fm_lokalisation.tsv) | Lokalisation der Fernmetastasen | _Primärdiagnose_ `Lokalisation`, _Folgeereignis_ `Lokalisation` |
| [geschlecht.tsv](/Klassifikationen/geschlecht.tsv) | Geschlecht | _Person_ `Geschlecht` |
| [gleason_anlass.tsv](/Klassifikationen/gleason_anlass.tsv) | Modul Prostata: Anlass der Probenahme | _Primärdiagnose_ `AnlassGleasonScore` |
| [gleason_score.tsv](/Klassifikationen/gleason_score.tsv) | Modul Prostata: Gleason-Score | _Primärdiagnose_ `ScoreErgebnis` |
| [grading.tsv](/Klassifikationen/grading.tsv) | Differenzierungsgrad | _Primärdiagnose_ `Grading` |
| [hormonrezeptor.tsv](/Klassifikationen/hormonrezeptor.tsv) | Modul Mamma: Hormonrezeptorstatus | _Primärdiagnose_ `HormonrezeptorStatus_Oestrogen`, _Primärdiagnose_ `HormonrezeptorStatus_Progesteron` |
| [icd10_todesursache.tsv](/Klassifikationen/icd10_todesursache.tsv) | Todesursache, Grundleiden nach ICD-10 | _Todesursachen_ `Code` |
| [icd10_version.tsv](/Klassifikationen/icd10_version.tsv) | Ausgabe der ICD-10 | _Todesursachen_ `Version`, _Primärdiagnose_ `Diagnose_ICD10_Version` |
| [icd10.tsv](/Klassifikationen/icd10.tsv) | Diagnose nach ICD-10 | _Primärdiagnose_ `Diagnose_ICD10_Code` |
| [interstitiell.tsv](/Klassifikationen/interstitiell.tsv) | Angabe zur Kontaktbestrahlung | _Strahlentherapie_ `Interstitiell_endokavitaer` |
| [landkreis.tsv](/Klassifikationen/landkreis.tsv) | Wohnort bei Diagnose | _Primärdiagnose_ `Inzidenzort`, _Primärdiagnose_ `Inzidenzort_BL` |
| [menopause.tsv](/Klassifikationen/menopause.tsv) | Modul Mamma: Menopausenstatus | _Primärdiagnose_ `Praetherapeutischer_Menopausenstatus` |
| [metabolisch.tsv](/Klassifikationen/metabolisch.tsv) | Typ der metabolischen Strahlentherapie | _Strahlentherapie_ `Metabolisch_Typ` |
| [morphologie_version.tsv](/Klassifikationen/morphologie_version.tsv) | Quelle Morphologie | _Primärdiagnose_ `Morphologie_Version` |
| [morphologie.tsv](/Klassifikationen/morphologie.tsv) | Morphologie | _Primärdiagnose_ `Morphologie_Code` |
| [op_intention.tsv](/Klassifikationen/op_intention.tsv) | Intention der OP | _Operation_ `Intention` |
| [ops.tsv](/Klassifikationen/ops.tsv) | Art der OP | _Operation_ `Code` |
| [protokoll.tsv](/Klassifikationen/protokoll.tsv) | Therapieprotokoll | _Systemische Therapie_ `Protokoll_TypProtokollschluessel_Code` |
| [radiochemo.tsv](/Klassifikationen/radiochemo.tsv) | Ausführung der perkutanen Radiochemotherapie | _Strahlentherapie_ `Radiochemo` |
| [rasmutation.tsv](/Klassifikationen/rasmutation.tsv) | Modul Darm: Mutation K-ras-Onkogen | _Primärdiagnose_ `RASMutation` |
| [rate.tsv](/Klassifikationen/rate.tsv) | Dosisleistung Kontaktbestrahlung | _Strahlentherapie_ `Rate_Type` |
| [seite_zielgebiet.tsv](/Klassifikationen/seite_zielgebiet.tsv) | Körperseite der bestrahlten Region | _Strahlentherapie_ `Seite_Zielgebiet` |
| [seitenlokalisation.tsv](/Klassifikationen/seitenlokalisation.tsv) | Seitenlokalisation bei paarigen Organen | _Primärdiagnose_ `Seitenlokalisation` |
| [st_intention.tsv](/Klassifikationen/st_intention.tsv) | Intention der Strahlentherapie | _Strahlentherapie_ `Intention` |
| [st_op_stellung.tsv](/Klassifikationen/st_op_stellung.tsv) | Bezug Strahlentherapie - OP | _Strahlentherapie_ `Stellung_OP` |
| [stereotaktisch.tsv](/Klassifikationen/stereotaktisch.tsv) | Angabe zur perkutanen Strahlentherapie | _Strahlentherapie_ `Stereotaktisch` |
| [substanz.tsv](/Klassifikationen/substanz.tsv) | Verwendete Substanz(en) | _Systemische Therapie_ `TypeOfSYST_TypSubstanz` |
| [syst_intention.tsv](/Klassifikationen/syst_intention.tsv) | Intention der systemischen Therapie | _Systemische Therapie_ `Intention` |
| [syst_op_stellung.tsv](/Klassifikationen/syst_op_stellung.tsv) | Bezug systemische Therapie - OP | _Systemische Therapie_ `Stellung_OP` |
| [therapieart.tsv](/Klassifikationen/therapieart.tsv) | Art der systemischen Therapie | _Systemische Therapie_ `Therapieart` |
| [tnm_auflage.tsv](/Klassifikationen/tnm_auflage.tsv) | TNM-Ausgabe | _Primärdiagnose_ `TNM_Auflage_c`, _Primärdiagnose_ `TNM_Auflage_p`, _Folgeereignis_ `Version` |
| [tnm_cpu.tsv](/Klassifikationen/tnm_cpu.tsv) | TNM-Präfix (c, p, u) | _Primärdiagnose_ `c_p_u_Praefix_T_c`, _Primärdiagnose_ `c_p_u_Praefix_N_c`, _Primärdiagnose_ `c_p_u_Praefix_M_c`, _Primärdiagnose_ `c_p_u_Praefix_T_p`, _Primärdiagnose_ `c_p_u_Praefix_N_p`, _Primärdiagnose_ `c_p_u_Praefix_M_p`, _Folgeereignis_ `c_p_u_Praefix_T`, _Folgeereignis_ `c_p_u_Praefix_N`, _Folgeereignis_ `c_p_u_Praefix_M` |
| [tnm_l.tsv](/Klassifikationen/tnm_l.tsv) | TNM: Lymphgefäßinvasion | _Primärdiagnose cTNM_ `L_p`, _Primärdiagnose pTNM_ `L_p`, _Folgeereignis_ `L` |
| [tnm_m.tsv](/Klassifikationen/tnm_m.tsv) | TNM: Fernmetastasierung | _Primärdiagnose cTNM_ `M_c`, _Primärdiagnose pTNM_ `M_p`, _Folgeereignis_ `M` |
| [tnm_n.tsv](/Klassifikationen/tnm_n.tsv) | TNM: Regionäre Lymphknotenmetastasierung | _Primärdiagnose cTNM_ `N_c`, _Primärdiagnose pTNM_ `N_p`, _Folgeereignis_ `N` |
| [tnm_pn.tsv](/Klassifikationen/tnm_pn.tsv) | TNM: Perineuralinvasion | _Primärdiagnose cTNM_ `Pn_c`, _Primärdiagnose pTNM_ `Pn_p`, _Folgeereignis_ `Pn` |
| [tnm_s.tsv](/Klassifikationen/tnm_s.tsv) | TNM: Serumtumormarker | _Primärdiagnose cTNM_ `S_c`, _Primärdiagnose pTNM_ `S_p`, _Folgeereignis_ `S` |
| [tnm_t.tsv](/Klassifikationen/tnm_t.tsv) | TNM: Ausdehnung des Primärtumors | _Primärdiagnose cTNM_ `T_c`, _Primärdiagnose pTNM_ `T_p`, _Folgeereignis_ `T` |
| [tnm_uicc.tsv](/Klassifikationen/tnm_uicc.tsv) | TNM: UICC-Stadium | _Primärdiagnose cTNM_ `UICC_Stadium_c`, _Primärdiagnose pTNM_ `UICC_Stadium_p`, _Folgeereignis_ `UICC_Stadium` |
| [tnm_v.tsv](/Klassifikationen/tnm_v.tsv) | TNM: Veneninvasion | _Primärdiagnose cTNM_ `V_c`, _Primärdiagnose pTNM_ `V_p`, _Folgeereignis_ `V` |
| [topographie_version.tsv](/Klassifikationen/topographie_version.tsv) | Ausgabe der ICD-O | _Primärdiagnose_ `Topographie_Version` |
| [topographie.tsv](/Klassifikationen/topographie.tsv) | Topographie | _Primärdiagnose_ `Topographie_Code` |
| [verlauf_fern.tsv](/Klassifikationen/verlauf_fern.tsv) | Verlauf: Fernmetastasierung | _Folgeereignis_ `Verlauf_Tumorstatus_Fernmetastasen` |
| [verlauf_lokal.tsv](/Klassifikationen/verlauf_lokal.tsv) | Verlauf: Lokaler Tumorstatus | _Folgeereignis_ `Verlauf_Lokaler_Tumorstatus` |
| [verlauf_lymphe.tsv](/Klassifikationen/verlauf_lymphe.tsv) | Verlauf: Regionärer Lymphknotenstatus | _Folgeereignis_ `Verlauf_Tumorstatus_Lymphknoten` |
| [zielgebiet2014.tsv](/Klassifikationen/zielgebiet2014.tsv) | Zielgebiet Strahlentherapie oBDS2014 | _Strahlentherapie Perkutan_ `CodeVersion2014`, _Strahlentherapie Kontakt_ `CodeVersion2014`, _Strahlentherapie Metabolisch_ `CodeVersion2014`, _Strahlentherapie Sonstige_ `CodeVersion2014`, _Strahlentherapie Unbekannt_ `CodeVersion2014` |
| [zielgebiet2021.tsv](/Klassifikationen/zielgebiet2021.tsv) | Zielgebiet Strahlentherapie oBDS2021 | _Strahlentherapie Perkutan_ `CodeVersion2021`, _Strahlentherapie Kontakt_ `CodeVersion2021`, _Strahlentherapie Metabolisch_ `CodeVersion2021`, _Strahlentherapie Sonstige_ `CodeVersion2021`, _Strahlentherapie Unbekannt_ `CodeVersion2021` |

#### Datumsangaben

Die Angabe _Tag_ wird von den Registern grundsätzlich _nicht_ ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format _Jahr-Monat-Tag_ vorliegt.

Für jede Datumsangabe im Datensatz liegen jeweils zwei Variablen vor:

- das `Datum` im internationalen Datumsformat _YYYY-MM-DD_ und
- die `Genauigkeit` des Datums in einer von drei möglichen Ausprägungen (_M_, _T_, _V_):
  _M_ = nur das Jahr ist bekannt (jahrgenau)
  _T_ = Jahr und Monat sind bekannt (monatsgenau)
  _V_ = Jahr und Monat wurden geschätzt

### Details

In diesem Abschnitt stellen wir sukzessive ergänzende Informationen zu den Inhalten der [Referenztabellen](#referenztabellen) zusammen (Hinweise zu Spaltenbezeichnungen, genutzten Quellen usw.).

#### [ICD-10-GM Diagnose](/Klassifikationen/icd10.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der ICD-10-GM (Version 2008) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) (1), unter Verwendung der Empfehlungen des GKV-Spitzenverbands für die klinische Krebsregistrierung (Stand: 14.05.2020) (2) und unter Verwendung des Umsetzungsleitfadens der Plattform § 65c (Stand: 06.06.2023) (3).

Spalten der Referenztabelle:

- `id`: Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt (z. B. C021)
- `code`: Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt (z. B. C02.1)
- `name`: Beschreibung der Diagnose (deutschsprachig)
- `id3`: 3-stelliger Diagnoseschlüssel
- `epi_valide`: TRUE = Diagnose ist im [epidemiologischen Datensatz](https://www.krebsdaten.de/Krebs/DE/Content/Forschungsdatensatz/Informationen_datensatz/epidemiologischer_datensatz/epidemiologischer_datensatz_node.html) des ZfKD enthalten
- `p65_valide`: TRUE = es besteht eine Meldepflicht für den klinischen Datensatz (lt. Plattform § 65c-Umsetzungsleitfaden)

> Referenzen:
> (1) ICD-10-GM, BfArM: https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html -- **[Nutzungsbedingungen](nutzungsbedingungen/bfarm_tou_icd10_ops.pdf)**
> (2) GKV-Spitzenverband: https://www.gkv-spitzenverband.de/krankenversicherung/qualitaetssicherung_2/klinisches_krebsregister.jsp
> (3) Plattform § 65c: https://confluence.basisdatensatz.de/display/UMK/Meldepflichtige+Diagnosen+nach+ICD

#### [ICD-10 Todesursache](/Klassifikationen/icd10_todesursache.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der ICD-10-GM (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) (1).

Um die internationale Vergleichbarkeit zu gewährleisten, ist für die Verschlüsselung von Todesursachen die ICD-10-WHO vorgesehen. (2) Aktuell wird bei der Übermittlung von Todesursachen ans ZfKD vorwiegend (noch) die Verwendung der ICD-10-GM angegeben.

Spalten der Referenztabelle:

- `id`: Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt (z. B. C021)
- `code`: Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt (z. B. C02.1)
- `id3`: 3-stelliger Diagnoseschlüssel
- `chapter`: Kapitel der ICD-10 (als arabische Zahl)
- `name`: Beschreibung der Diagnose (deutschsprachig)

> Referenzen:
> (1) ICD-10-GM, BfArM: https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html -- **[Nutzungsbedingungen](nutzungsbedingungen/bfarm_tou_icd10_ops.pdf)**
> (2) BfArM, Todesursachenstatistik: https://www.bfarm.de/DE/Kodiersysteme/Klassifikationen/ICD/ICD-10-WHO/Todesursachenstatistik/_node.html

#### [ICD-O Topographie](/Klassifikationen/topographie.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung der ICD-O-3 (2. Revision, Version 2019) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) (1) und unter Zuhilfenahme des Umsetzungsleitfadens der Plattform § 65c (Stand: 10.05.2023) (2).

Für paarige Organe (Ausprägung `istPaarig`= 1) wird bei der Variable `Seitenlokalisation` die Angabe der betroffenen Körperseite(n) erwartet.

Spalten der Referenztabelle:

- `id`: Diagnoseschlüssel, 4-Steller werden ohne Trennzeichen dargestellt (z. B. C021)
- `code`: Diagnoseschlüssel, 4-Steller werden mit Trennzeichen dargestellt (z. B. C02.1)
- `name`: Beschreibung der Topographie
- `id3`: 3-stelliger Diagnoseschlüssel
- `istPaarig`: 1 = es handelt sich um ein paariges Organ (lt. Plattform § 65c-Umsetzungsleitfaden)

> Referenzen:
> (1) ICD-O, BfArM: https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html -- **[Nutzungsbedingungen](nutzungsbedingungen/bfarm_tou_icdo3.pdf)**
> (2) Plattform § 65c: https://confluence.basisdatensatz.de/display/UMK/Paarige+Organe

#### [Operationen- und Prozedurenschlüssels (OPS)](/Klassifikationen/ops.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der maschinenlesbaren Fassung des Operationen- und Prozedurenschlüssels (OPS) (Version 2022) des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) (1).

Spalten der Referenztabelle:

- `ops_id`: ID, maximal 6-stellig
- `ops_chapter`: OPS-Kapitel
- `ops_group`: OPS-Gruppe, -Bereich
- `ops_three_digits`: OPS-Kategorie/-Kode, 3-stellig
- `ops_four_digits`: OPS-Subkategorie, 4-stellig
- `ops_five_digits`: OPS-Subkategorie, 5-stellig
- `ops_six_digits`: OPS-Subkategorie, 6-stellig
- `ops_description`: Klassentitel der Maßnahme

> Referenzen:
> (1) OPS, BfArM: https://www.bfarm.de/DE/Kodiersysteme/Services/Downloads/_node.html -- **[Nutzungsbedingungen](nutzungsbedingungen/bfarm_tou_icd10_ops.pdf)**

#### [Protokoll](/Klassifikationen/protokoll.tsv)

Bei der verwendeten Referenztabelle handelt es sich um eine _Vorschlagsliste_ der Plattform § 65c ([externer Link](https://confluence.basisdatensatz.de/display/UMK/Protokolle)). Diese Vorschlagsliste stellt keine verbindliche Festlegung dar. Ein anerkannter Standard für die Kodierung von Systemtherapie-Protokollen ist uns nicht bekannt. Vorschläge für eine standardisierte Nomenklatur (1), Referenzsysteme (2,3) und kommerzielle Produkte für die medizinische Dokumentation (4) wurden von anderen entwickelt. Wir verweisen hier auf eine Auswahl dieser Arbeiten und Systeme.

> Referenzen:
> (1) Rubinstein, S. M., Yang, P. C., Cowan, A. J., & Warner, J. L. (2020). Standardizing Chemotherapy Regimen Nomenclature: A Proposal and Evaluation of the HemOnc and National Cancer Institute Thesaurus Regimen Content. JCO clinical cancer informatics, 4, 60–70. [https://doi.org/10.1200/CCI.19.00122](https://doi.org/10.1200/CCI.19.00122)
> (2) [HemOnc.org - A Free Hematology/Oncology Reference](https://hemonc.org/)
> (3) [National Cancer Institute Thesaurus (NCIT)](https://bioportal.bioontology.org/ontologies/NCIT/?p=classes&conceptid=http%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23C62634)
> (4) [Onkopti® – die Datenbank digitalisierter onkologischer Therapieprotokolle](https://onkopti.de/protokollsuche/)

#### [Substanz](/Klassifikationen/substanz.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der Anatomisch-therapeutisch-chemischen Klassifikation (ATC-Klassifikation) für den deutschen Arzneimittelmarkt (Version 2022), herausgegeben vom Wissenschaftlichen Institut der AOK (WIdO) (1).

Spalten der Referenztabelle:

- `code`: ATC-Kode, Ebene 5
- `name`: Bezeichnung des Arzneimittels

> Referenzen:
> (1) ATC, WIdO: https://www.wido.de/publikationen-produkte/arzneimittel-klassifikation/ -- **[Nutzungsbedingungen](nutzungsbedingungen/wido_atc.pdf)**

#### [pTNM N-Kategorie](/Klassifikationen/tnm_n.tsv)

**Zusatz (1mi), Mammakarzinom**
Anwendung bei: Mikrometastase(n), > 0,2 mm und/oder mehr als 200 Tumorzellen, aber nicht größer als 0,2 cm
Stadium IB nach TNM8: T0, T1 N1mi M0

> _Quelle: S3-Leitlinie Mammakarzinom, TNM8_

**Zusatz (sn)**
`(p)NX(sn)` Schildwächterlymphknoten kann histologisch nicht beurteilt werden
`(p)N0(sn)`Histologisch keine Lymphknotenmetastasen in Schildwächterlymphknoten
`(p)N1(sn)` Befall des (der) Schildwächterlymphknoten

> _Quelle: TNM8_

**Zusatz (i+), (mol+)**
`(p)N0` Histologisch keine Lymphknotenmetastasen, keine Untersuchung zum Nachweis isolierter Tumorzellen
`(p)N0(i–)` Histologisch keine Lymphknotenmetastasen, kein morphologischer Nachweis von isolierten Tumorzellen
`(p)N0(i+)` Histologisch keine Lymphknotenmetastasen, morphologischer Nachweis von isolierten Tumorzellen
`(p)N0(mol–)` Histologisch keine Lymphknotenmetastasen, kein nichtmorphologischer Nachweis von isolierten Tumorzellen
`(p)N0(mol+)` Histologisch keine Lymphknotenmetastasen, nicht-morphologischer Nachweis von isolierten Tumorzellen

> _Quelle: TNM8_


## Beispieldaten

In diesem Repository soll der [Beantragungsprozess](https://www.krebsdaten.de/info_antrag) für klinische Daten veranschaulicht werden.

Zum einen ist ein [Spieldatensatz](/Beispieldaten/oBDS_v3.0.0.8a_RKI_Sample.xml) hinterlegt für die Lieferung der Daten aus den klinischen Krebsregistern der Länder. Dieser entspricht den gemeinsam erarbeiteten Vorgaben des `oBDS-RKI` und wird im ZfKD zu einem deutschlandweiten Gesamtdatensatz verarbeitet. Der "rohe" Datensatz bestehend aus xml-Dateien bildet den Ausgangspunkt der weiteren Verarbeitung, wird aber vom ZfKD nicht ausgegeben.

Zum anderen wird hier simuliert, wie eine definierte Teilmenge des verarbeiteten Gesamtdatensatzes auf Antrag übermittelt wird.
Beispielhaft enthält der Ordner `04_sample-output` unter `data` eine Sammlung von csv-Dateien. Format und Aufbau dieser Dateien entsprechen exakt einer Datenlieferung auf Antrag.

Verwendete Identifikatoren können in einem relationalen Modell wieder korrekt zusammengeführt werden (so sind etwa Einträge der Tumortabelle den jeweiligen Patienten zuordenbar). Hilfestellung bietet hier das angehangene [ER-Modell](/.github/images/2023-09-28_Entity-Relationship-Modell.jpg).

_(Die in den Beispieldateien hinterlegten Daten sind künstlich erzeugt, folgen einfachen Verteilungen und berücksichtigen keine medizinischen Zusammenhänge. Die Identifikatoren sind zufällig erzeugt)_


| Datei | Beschreibung | Download |
| ----- | ------------ | -------- |
| Testdatensatz | Ein einfacher Testdatensatz als `.xml`-Datei mit Werten in zufälliger Verteilung. Medizinische Zusammenhänge sind nicht berücksichtigt. Näheres unter [Beispieldaten](#beispieldaten) | [💾](/Beispieldaten/oBDS_v3.0.0.8a_RKI_Sample.xml) |

- Ergänzung der Tabelle um die weiteren Entetys (.csv)
- beschreibung des ERM


## Kontextmaterialien

- kurze Hinweise zu den Nutzungbedingungne BfArm WIDO
- (eventuell kann die beschreibung auch zu den Klassifikationen)

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
