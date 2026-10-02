"""把 src/template.html 和 src/data.json 組成單一檔案 index.html。

用法：在專案根目錄執行  python3 build.py
只需要 Python 3，不用安裝任何套件。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "src" / "data.json").read_text(encoding="utf-8"))
data_str = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8").replace("__DATA__", data_str)

head, rest = tpl.split("</style>", 1)
html = (
    "<!doctype html>\n<html lang=\"zh-Hant-TW\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<title>臺大電信所丙組</title>\n"
    + head + "</style>\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n"
)
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("已輸出 index.html（%d bytes）" % len(html.encode("utf-8")))
