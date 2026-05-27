import re
import zipfile
import sys


def extract_lsb_hidden(docx_path: str, marker_color: str = "010000") -> str:
    """Извлечь скрытый текст из DOCX по маркеру цвета (LSB)."""
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")

    runs = re.findall(r"<w:r\b[^>]*>(.*?)</w:r>", xml, flags=re.DOTALL)

    hidden_parts = []
    for run in runs:
        if f'w:val="{marker_color}"' not in run:
            continue
        m = re.search(r"<w:t[^>]*>(.*?)</w:t>", run, flags=re.DOTALL)
        if m:
            hidden_parts.append(m.group(1))

    return "".join(hidden_parts)


path = sys.argv[1] if len(sys.argv) > 1 else "task.docx"
print("Секретное слово:", extract_lsb_hidden(path))
