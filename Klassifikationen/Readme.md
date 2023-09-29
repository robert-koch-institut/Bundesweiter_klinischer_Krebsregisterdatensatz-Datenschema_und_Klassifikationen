# Klassifikationen

Die für einzelne Variablen erwarteten Ausprägungen und ihre Beschreibung sind in [Referenztabellen](#referenztabellen) hinterlegt. Einzelne Referenzen werden für mehrere Variablen genutzt: Beispielsweise wird für den Östrogen-Rezeptorstatus und den Progesteron-Rezeptorstatus die gleiche Kodierung verwendet. Ebenso werden für die Angaben zur klinischen und pathologischen TNM die gleichen Referenztabellen genutzt.

Größtenteils handelt es sich bei den Referenzen um Vereinbarungen, die bei der Erarbeitung des ZfKD-Lieferdatensatzes getroffen wurden (z. B. Ausprägungen von Variablen im Element Strahlentherapie, Ausprägungen von _Diagnosesicherung_). Teilweise handelt es sich bei den Referenzen um internationale oder nationale Standards (z. B. TNM, ATC-Klassifikation für den deutschen Arzneimittelmarkt). Informationen zu Quelle und Version der jeweiligen Referenzwerte, zu ihrer Interpretation und zu gegebenenfalls bestehenden Nutzungsbedingungen der Herausgeber sind im Abschnitt [Details](#details) zusammengestellt.

## Referenztabellen

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

### Formatierung

Die nachfolgend aufgeführten Referenztabellen sind einheitlich formatiert:

- Zeichensatz: `UTF-8` (dieses Format erleichtert die Bearbeitung in MS Excel, da Umlaute hier korrekt dargestellt werden)
- Datumsformat: `ISO 8601`
- Dateiformat: `.tsv`
- Trennzeichen: Tab `\t`

### Datumsangaben

Die Angabe _Tag_ wird von den Registern grundsätzlich _nicht_ ans ZfKD übermittelt. Das ZfKD legt den Tag auf einen beliebigen Wert fest (i. d. R. 15), so dass immer ein Datum im Format _Jahr-Monat-Tag_ vorliegt.

Für jede Datumsangabe im Datensatz liegen jeweils zwei Variablen vor:

- das `Datum` im internationalen Datumsformat _YYYY-MM-DD_ und
- die `Genauigkeit` des Datums in einer von drei möglichen Ausprägungen (_M_, _T_, _V_):
  _M_ = nur das Jahr ist bekannt (jahrgenau)
  _T_ = Jahr und Monat sind bekannt (monatsgenau)
  _V_ = Jahr und Monat wurden geschätzt

## Details

In diesem Abschnitt stellen wir sukzessive ergänzende Informationen zu den Inhalten der [Referenztabellen](#referenztabellen) zusammen (Hinweise zu Spaltenbezeichnungen, genutzten Quellen usw.).

### [ICD-10-GM Diagnose](/Klassifikationen/icd10.tsv)

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

### [ICD-10 Todesursache](/Klassifikationen/icd10_todesursache.tsv)

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

### [ICD-O Topographie](/Klassifikationen/topographie.tsv)

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

### [Operationen- und Prozedurenschlüssels (OPS)](/Klassifikationen/ops.tsv)

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

### [Protokoll](/Klassifikationen/protokoll.tsv)

Bei der verwendeten Referenztabelle handelt es sich um eine _Vorschlagsliste_ der Plattform § 65c ([externer Link](https://confluence.basisdatensatz.de/display/UMK/Protokolle)). Diese Vorschlagsliste stellt keine verbindliche Festlegung dar. Ein anerkannter Standard für die Kodierung von Systemtherapie-Protokollen ist uns nicht bekannt. Vorschläge für eine standardisierte Nomenklatur (1), Referenzsysteme (2,3) und kommerzielle Produkte für die medizinische Dokumentation (4) wurden von anderen entwickelt. Wir verweisen hier auf eine Auswahl dieser Arbeiten und Systeme.

> Referenzen:
> (1) Rubinstein, S. M., Yang, P. C., Cowan, A. J., & Warner, J. L. (2020). Standardizing Chemotherapy Regimen Nomenclature: A Proposal and Evaluation of the HemOnc and National Cancer Institute Thesaurus Regimen Content. JCO clinical cancer informatics, 4, 60–70. [https://doi.org/10.1200/CCI.19.00122](https://doi.org/10.1200/CCI.19.00122)
> (2) [HemOnc.org - A Free Hematology/Oncology Reference](https://hemonc.org/)
> (3) [National Cancer Institute Thesaurus (NCIT)](https://bioportal.bioontology.org/ontologies/NCIT/?p=classes&conceptid=http%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23C62634)
> (4) [Onkopti® – die Datenbank digitalisierter onkologischer Therapieprotokolle](https://onkopti.de/protokollsuche/)

### [Substanz](/Klassifikationen/substanz.tsv)

Die Erstellung der Referenztabelle erfolgte unter Verwendung der Anatomisch-therapeutisch-chemischen Klassifikation (ATC-Klassifikation) für den deutschen Arzneimittelmarkt (Version 2022), herausgegeben vom Wissenschaftlichen Institut der AOK (WIdO) (1).

Spalten der Referenztabelle:

- `code`: ATC-Kode, Ebene 5
- `name`: Bezeichnung des Arzneimittels

> Referenzen:
> (1) ATC, WIdO: https://www.wido.de/publikationen-produkte/arzneimittel-klassifikation/ -- **[Nutzungsbedingungen](nutzungsbedingungen/wido_atc.pdf)**

### [pTNM N-Kategorie](/Klassifikationen/tnm_n.tsv)

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
