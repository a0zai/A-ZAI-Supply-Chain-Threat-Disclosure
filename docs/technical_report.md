# Technisch Rapport – A∞ZAI Supply Chain Threat

## Introductie
Dit rapport beschrijft een potentiële supply chain kwetsbaarheid geïmplementeerd als Proof of Concept (PoC) binnen het A∞ZAI-project. Het toont aan hoe verborgen instructies en gecodeerde informatie kunnen worden verspreid via open source-projectstructuren.

## Doel
Het doel van dit experiment is om:
- Aantonen hoe metadata, bestandsnamen en patronen kunnen worden misbruikt.
- Informatie op een onopgemerkte manier te verzamelen zonder actieve code-executie.
- Te waarschuwen voor structurele blinde vlekken in open source software.

## PoC Beschrijving
Het systeem bestaat uit:
- **Pattern Extractor:** Zoekt verborgen patronen in bestandsnamen.
- **Omgevingsinformatie Verzamelaar:** Haalt gegevens zoals gebruikersnaam, IP en systeemdetails op.
- **Encryptie en Verspreiding:** Data wordt versleuteld en lokaal opgeslagen of verzonden naar een server.

## Impact
Dit mechanisme kan:
- Onopgemerkt data verzamelen.
- Leveringsketens beïnvloeden.
- Worden geïntegreerd zonder actieve payloads, waardoor detectie moeilijker wordt.

---

## Verdedigingsmaatregelen
Zie het bestand: `protection/protector.py`
