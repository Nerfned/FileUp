README
Projekt: CGI-AJAX-Webanwendung - File Up Datei Uploader mit Archivierung


Kurzbeschreibung
Die CGI-AJAX-Webanwendung ermöglicht es Nutzern, PDF-, JPG-, SVG-, PNG- und TXT-Dateien hochzuladen, zu archivieren und bei Bedarf herunterzuladen. 
Die Anwendung besteht aus einem CGI-Skript und einer HTML-Datei mit JavaScript und AJAX.


Funktionsweise
    Datei Uploader:
        Nutzer können Dateien hochladen (PDF, JPG, SVG, PNG, TXT).
        Die Datei wird über ein Formular ausgewählt und mit JavaScript verarbeitet.
        Das CGI-Skript speichert die Datei nach Entschlüsselung auf dem Server.
        Statusmeldungen informieren über den Speicherprozess.

    Archiv:
        Zeigt archivierte Dateien an.
        Dateien können heruntergeladen oder gelöscht werden.
        Das Archiv wird in einer Tabelle dargestellt.


Wie es funktioniert
    Datei Uploader:
        Der Nutzer wählt eine Datei aus und lädt sie hoch.
        Das CGI-Skript entschlüsselt die Datei und speichert sie.
        Statusmeldungen informieren den Nutzer über den Speicherfortschritt.

    Archiv:
        Gespeicherte Dateien werden im Archiv angezeigt.
        Nutzer können Dateien löschen oder herunterladen.
