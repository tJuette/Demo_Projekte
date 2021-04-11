"use strict"
let sekunde = 0
let zeit
let dauer = parseInt(prompt("Wieviele Minuten möchten Sie meditieren?"))
if(dauer) {
    zeit = setInterval(farben, 1000)
}


function farben() {
	let hexFarben = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
	function hex00BisFF() {
		return `${hexFarben[Math.floor(Math.random() * 16)]}${hexFarben[Math.floor(Math.random() * 16)]}`
	}
	let farbe1 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
	let farbe2 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
	let farbe3 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
	let farbe4 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
	let farbe5 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
    let farbe6 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
    let farbe7 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
    let farbe8 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
    let farbe9 = `#${hex00BisFF()}${hex00BisFF()}${hex00BisFF()}`
    for(let reihe = 1; reihe < 114; reihe++) {
        for(let feld = 1; feld < 201; feld++) {
            if(reihe % 2 == 0 && reihe % 3 != 0 && reihe % 4 != 0) {
                if(feld % 2 == 0 && feld % 3 != 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe1
                }
                else if(feld % 3 == 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe2
                }
                else if(feld % 4 == 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe3
                }
                else {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe4
                }
            }
            else if(reihe % 3 == 0 && reihe % 4 != 0) {
                if(feld % 2 == 0 && feld % 3 != 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe4
                }
                else if(feld % 3 == 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe1
                }
                else if(feld % 4 == 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe2
                }
                else {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe3
                }
            }
            else if(reihe % 4 == 0) {
                if(feld % 2 == 0 && feld % 3 != 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe3
                }
                else if(feld % 3 == 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe4
                }
                else if(feld % 4 == 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe1
                }
                else {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe2
                }
            }
            else {
                if(feld % 2 == 0 && feld % 3 != 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe2
                }
                else if(feld % 3 == 0 && feld % 4 != 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe3
                }
                else if(feld % 4 == 0) {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe4
                }
                else {
                    $(`#r${reihe}f${feld}`)[0].style.backgroundColor = farbe1
                }
            }
        }
    }
    sekunde += 1
    if(dauer == sekunde/60) {
        clearInterval(zeit)
        $('td').css("background-color", "black")
        alert("Die Zeit ist um!")
        if(confirm("Nochmal?")) {
            location.reload()
        }
    }
}

    