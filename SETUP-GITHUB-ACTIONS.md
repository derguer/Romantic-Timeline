# 🔧 GitHub Auto-Sync Setup Guide

## Schritt 1: Personal Access Token erstellen

1. Gehe zu **GitHub.com** → Klicke auf dein Profilbild → **Settings**
2. Scrolle runter zu **Developer settings** (links unten)
3. Klicke **Personal access tokens** → **Tokens (classic)**
4. Klicke **Generate new token** → **Generate new token (classic)**
5. **Note**: Gib ein: "Romantic Timeline Sync"
6. **Expiration**: Wähle "No expiration" (oder 1 Jahr)
7. **Scopes**: Setze Häkchen bei **"repo"** (das reicht!)
8. Klicke **Generate token**
9. **WICHTIG**: Kopiere den Token sofort! (Du siehst ihn nur einmal)

## Schritt 2: Token beim ersten Speichern eingeben

1. Gehe auf deine Website
2. Erstelle ein neues Date oder bearbeite ein vorhandenes
3. Klicke **Speichern**
4. Es erscheint automatisch ein Dialog: "GitHub Personal Access Token eingeben"
5. Füge deinen kopierten Token ein
6. Der Token wird sicher in deinem Browser gespeichert

## Schritt 3: Fertig! 🎉

- **Automatisches Sync**: Alle 30 Sekunden werden Daten synchronisiert
- **Sofortige Speicherung**: Neue Dates werden sofort zu GitHub hochgeladen
- **Multi-Device**: Dates erscheinen automatisch auf allen Geräten

## ✅ So erkennst du, dass es funktioniert:

- Sync-Status zeigt "✅ Synchronisiert" (oben rechts)
- In der Browser-Konsole: "✅ Successfully saved to GitHub"
- Die `data/dates.json` Datei wird automatisch auf GitHub aktualisiert
- Neue Dates erscheinen binnen 30 Sekunden auf anderen Geräten

## 🔒 Sicherheit:

- Token wird nur lokal in deinem Browser gespeichert
- Kein Token im öffentlichen Code sichtbar
- Du kannst den Token jederzeit in GitHub deaktivieren

## 🚨 Falls Probleme auftreten:

1. Überprüfe ob der Token "repo" Berechtigung hat
2. Schaue in die Browser-Konsole (F12) nach Fehlermeldungen
3. Bei "Token invalid": Lösche den Token im Browser und erstelle einen neuen

**Das war's! Vollautomatisches Sync ohne manuelle Schritte! 🚀**
