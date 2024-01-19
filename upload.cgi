#!/bin/bash


##################################################################################
# #
# #                             Autor: Joel Wollny
# #
##################################################################################

WEBDIR="/FileUp/upload"
UPLOADDIR="/var/www/html/$WEBDIR"

# Erstellen des Verzeichnisses für den Datei-Upload mit den entsprechenden Berechtigungen
mkdir -m 777 -p "${UPLOADDIR}"

echo -e "content-type: text/html; charset=utf-8\r\n\r\n"

read querystring
eval "${querystring//&/;}"

# Hochladen der Datei, wenn sowohl "name" als auch "fileupload" vorhanden sind
if [[ -n "$name" && -n "$fileupload" ]] ;then
    {
        echo "$name"
        echo "$fileupload"
        temp_file=$(mktemp)
        UPLOADFILE="${name=\"}"; UPLOADFILE="${UPLOADFILE%%\"*}"
        echo "$fileupload" | tr -d '\n' | base64 --decode > "${UPLOADDIR}/${UPLOADFILE}"
    }
fi

# Generieren der Tabelle mit allen Dateien im UPLOADDIR, wenn "layout" vorhanden ist
if [[ -n $layout  ]]; then
    if [[ "$layout" == "archiv"  ]]; then
        # Tabelle mit allen Dateien im UPLOADDIR generieren
        if [[ -z $(ls -A "${UPLOADDIR}") ]]; then
            echo "<table class='file-list' style='display: flex; justify-content: center; margin-top: 40px; border-collapse: collapse;'>"
            echo "<tr style='background-color: #0d0d0d;'></tr>"
            echo "<tr><td colspan='3'>No files found.</td></tr>"
            echo "</table>"
        else
            count=0
            # Zählvariable für Striping der Tabelle
            echo "<table class='file-list' style='display: flex; justify-content: center; margin-top: 40px; border-collapse: collapse;'>"
            echo "<tr style='background-color: #0d0d0d;'><th>Filename</th><th>Size</th><th>Action</th></tr>"
            for file in "${UPLOADDIR}"/*; do
                filename=$(basename "$file")
                filesize=$(stat -c "%s" "$file") # Dateigröße in Bytes abrufen
                # Hintergrundfarbe für die Zeile festlegen
                if (( count % 2 == 0 )); then
                    bgcolor="#171717"
                else
                    bgcolor="#0d0d0d"
                fi
                echo "<tr style='background-color: ${bgcolor}; text-align: center;'>"
                echo "<td style='font-weight: bold; text-align: left; padding-right: 15px;'>${filename}</td>"
                echo "<td style='padding-left: 20px; padding-right: 20px;'>${filesize} bytes</td>"
                echo "<td><a href='$WEBDIR/$(basename "$file")' download='${filename}'><button name='loadfile' value='${filename}'>Download</button></a>"
                echo "<button name='delete' onclick='deleteFile(\"$filename\")'>Löschen</button>"
                echo "</td>"
                echo "</tr>"
                ((count++))
            done
            echo "</table>"
        fi
        elif [[ "$layout" == "fileupload" ]]; then
        # Formular für den Datei-Upload anzeigen
        cat << EOF
        <h3 class="title">Es werden .txt, .svg, .png, .jpg, .pdf unterstützt</h3>
        <form class="upload" method="post" enctype="multipart/form-data">
          <label>
            <h2>
              Datei zum Hochladen:
              <input id="myFile" class="upload-button" name="datei" type="file" size="50" accept=".txt,.svg,.png,.jpg,.pdf,"">
            </h2>
          </label>
          <br />
        </form>
        <div class="header-buttons">
          <button class="style-command center" onclick="prepareFilesToSend()">Submit</button>
        </div>
EOF
    fi
fi

# Datei löschen, wenn "filedelete" vorhanden ist
if [[ -n $filedelete  ]]; then
    # Überprüfung ob die Datei vorhanden ist
    if [[ -f "$UPLOADDIR/$filedelete" ]]; then
        rm "$UPLOADDIR/$filedelete"
        cat << EOF
             <h3 class="title">Wurde gelöscht</h3>
EOF
    else
       cat << EOF
             <h3 class="title">Konnte nicht gelöscht werden. Datei eventuell schon gelöscht</h3>
EOF
    fi
    # Tabelle mit allen Dateien im UPLOADDIR generieren
    if [[ -z $(ls -A "${UPLOADDIR}") ]]; then
        echo "<table class='file-list' style='display: flex; justify-content: center; margin-top: 40px; border-collapse: collapse;'>"
        echo "<tr style='background-color: #0d0d0d;'></tr>"
        echo "<tr><td colspan='3'>No files found.</td></tr>"
        echo "</table>"
    else
        # Zählvariable für Striping der Tabelle
        count=0
        echo "<table class='file-list' style='display: flex; justify-content: center; margin-top: 40px; border-collapse: collapse;'>"
        echo "<tr style='background-color: #0d0d0d;'><th>Filename</th><th>Size</th><th>Action</th></tr>"
        for file in "${UPLOADDIR}"/*; do
            filename=$(basename "$file")
            filesize=$(stat -c "%s" "$file") # Dateigröße in Bytes abrufen
            
            # Hintergrundfarbe für die Zeile festlegen
            if (( count % 2 == 0 )); then
                bgcolor="#171717"
            else
                bgcolor="#0d0d0d"
            fi
            echo "<tr style='background-color: ${bgcolor}; text-align: center;'>"
            echo "<td style='font-weight: bold; text-align: left; padding-right: 15px;'>${filename}</td>"
            echo "<td style='padding-left: 20px; padding-right: 20px;'>${filesize} bytes</td>"
            echo "<td><a href='/Uploader/upload/$(basename "$file")' download='${filename}'><button name='loadfile' value='${filename}'>Download</button></a>"
            echo "<button name='delete' onclick='deleteFile(\"$filename\")'>Löschen</button>"
            echo "</td>"
            echo "</tr>"
            ((count++))
        done
        echo "</table>"
    fi
fi
