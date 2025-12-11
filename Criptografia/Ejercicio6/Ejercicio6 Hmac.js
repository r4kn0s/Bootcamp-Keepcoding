const crypto = require("crypto");

var algoritmo = "sha256";

// Texto del ejercicio
var mensaje = "Siempre existe más de una forma de hacerlo, y más de una solución válida.";
// Clave del keystore en HEX
var keyHex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72";

// Convertimos la clave HEX a Buffer
var key = Buffer.from(keyHex, "hex");

// Creamos el HMAC
var hash = crypto.createHmac(algoritmo, key);

hash.update(mensaje);

console.log("Clave HEX:", keyHex);
console.log("Método:", algoritmo);

var miHash = hash.digest("hex");

console.log("HMAC es:", miHash);
console.log("Longitud del HMAC:", miHash.length * 4, "bits");

