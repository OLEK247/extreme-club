const fs = require("fs");
const path = require("path");
const html = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");
const start = html.indexOf("const VEHICLES = [");
const bodyStart = start + "const VEHICLES = ".length;
let depth = 0, i = bodyStart, inStr = false, strCh = "", esc = false;
for (; i < html.length; i++) {
  const c = html[i];
  if (inStr) {
    if (esc) { esc = false; }
    else if (c === "\\") { esc = true; }
    else if (c === strCh) { inStr = false; }
    continue;
  }
  if (c === "\"" || c === "'" || c === "`") { inStr = true; strCh = c; continue; }
  if (c === "[") depth++;
  else if (c === "]") { depth--; if (depth === 0) { i++; break; } }
}
const arrText = html.slice(bodyStart, i);
const outPath = path.join(__dirname, "vehicles_tmp.js");
fs.writeFileSync(outPath, "module.exports = " + arrText + ";\n");
const arr = require(outPath);
fs.writeFileSync(path.join(__dirname, "vehicles.json"), JSON.stringify(arr, null, 2));
fs.unlinkSync(outPath);
console.log("Extracted", arr.length, "vehicles ->", path.join(__dirname, "vehicles.json"));
