# Release Notes

Im Folgenden sind die Änderungen im Datensatz für die letzten Versionen aufgeführt.

## Patch 8a (2023-01-06)

- Darstellungen und Ausprägungen sind unverändert, lediglich Typfehler sind korrigiert
- Lieferdatum deklariert den Datumstyp nun nicht mehr per `xs:extension`, was die Implementierung erschwerte
- `Protokollschluessel/Code|Version` waren vorher untypisiert, und sind jetzt vom Typ `Freitext30`
- Versionsangabe ist nun korrekt gefüllt

## Version 8 (2022-10-13)

- Der Typ `Zahl_3_stellig` entfällt, da hier noch die Angabe `U` zulässig ist neben numerischen Werten. Die betroffenen Elemente (Tumorgrösse invasiv/DCIS) werden auf nonNegativeInteger umgestellt
- Diverse Datumselemente werden aus Konfomitätsgründen umbenannt
  - DatumBestrahlung -> `Datum_Beginn_Bestrahlung`
  - DatumSYST -> `Datum_Beginn_SYST`
  - DatumOP -> `Datum_OP`
  - Untersuchungsdatum_Verlauf -> Datum_Folgeereignis
- `Vitalstatus` enthielt fälschlicherweise ein` <choice>` Element aus der Vorversion, dies wird korrigiert
- folgende Modulitems werden hinzugefügt
  - Modul Darm: Rektum: Abstand des Tumorunterrandes zur Anokutanlinie (umgestellt auf nonNegativeInteger)
  - Modul Malignes Melanom: Ulzeration (umgestellt auf `JN_Typ`, ist weiterhin optional)
  - Modul Prostata: Anlass Gleason Score
- das Element `Substanz` in `SYST` ist nun wieder so konstruiert wie in oBDS 3.0.1, die Versionsabgabe zum ATC ist allerdings optional
- `Schema_Version_Development` ist entfallen. Das verpflichtende Element Schema_Version hat nur eine Ausprägung - die jeweils gültige Version von oBDS-RKI (3.0.0.8_RKI)
- target namespace ist nun http://www.basisdatensatz.de/oBDS/XML, in Anlehnung an die oBDS Schemafamilie
- alle Elemente mit `<xs:all>` sind nun ersetzt durch `<xs:sequence>`

## Version 7 (2022-09-08)

- `DCI` wurde umbenannt zu `DCN`. [Details](<https://plattform65c.atlassian.net/wiki/spaces/P6/pages/7372826/Vereinbarungen+zu+Elementen+des+XML-Schemas#DCN-(death-certificate-notified)-%5BinlineCard%5D>)
- die Ausprägungen von `Geschlecht` wurden an oBDS angepasst
- `Grading` 5 wurde entfernt, da dieser Wert im oBDS nicht deklariert ist
- `Diagnosesicherung` ist nun verpflichtend, missings können mit `Unbekannt` kodiert werden. [Details](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/7372826/Vereinbarungen+zu+Elementen+des+XML-Schemas#Diagnosesicherung)
- root node umbenannt von `<ZfKD_Lieferdatensatz>` zu `<oBDS_RKI>` zur Angleichung an die oBDS Schemafamilie
- `Inzidenzort` lässt nun besser erkennen, dass nur Daten von Patienten mit Wohnsitz in Deutschland übermittelt werden
- Elemente mit dem Namen Datum wurden im Kontext umbenannt (z.B. Diagnose_Typ/Datum ->Diagnosedatum)
- Identifikatoren wurden aus Datensparsamkeitsgründen entfernt, bis auf `Patient_ID` und `Tumor_ID`.
- OPS enthält nun wieder die Angabe zur Version
- im Modul_Prostata ist nun das `DatumPSA` verfügbar. [Details](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/7372826/Vereinbarungen+zu+Elementen+des+XML-Schemas#Modul-Prostatakrebs)
- das Element `Vitalstatus` wurde überarbeitet. [Details](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/7372826/Vereinbarungen+zu+Elementen+des+XML-Schemas#Vitalstatus)
- simple types sind zum grossen Teil entfernt. [Details](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/8257538/Technische+Abstimmung#Simple-Types-zur-Beschreibung-von-Textinhalten)
- Abstand in Tagen zwischen Ereignissen ist nun nicht mehr als `JNU-Typ` modelliert. Es wird nun lediglich eine - Abstandsangabe erwartet (ohne Attribute), das Element ist nun optional. [Details](https://plattform65c.atlassian.net/wiki/spaces/P6/pages/7143545/Allgemeine+Vereinbarungen#Angaben-mit-einer-Anzahl-Tagen-zwischen-Ereignissen)
- Tippfehler in Schema Annotationen korrigiert

[zurück](readme.md)
