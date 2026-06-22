import re
from pathlib import Path


CATALOG_PATH = Path(__file__).with_name("products.txt")
PRODUCT_CODE_RE = re.compile(r"^[A-Z]{2,}\d{3}$")

BRAND_ALIASES = {
    "Artcaffe": "Artcaffe",
    "ChocoMania": "ChocoMania",
    "ChocoTella": "ChocoTella",
    "Enigma": "Enigma",
    "Frusion": "Frusion",
    "Galitos": "Galitos",
    "Groupaco": "Groupaco",
    "Heavenly": "Heavenly",
    "KFC": "KFC",
    "Lyons": "Lyons",
    "MaxChoco": "MaxChoco",
    "Ooh": "Ooh!",
    "Presto": "Presto",
    "Raka": "Raka",
    "Simbisa": "Simbisa",
    "SUBZ": "SUBZ",
    "TANA": "TANA",
    "Twister": "Twister",
}

UNIT_RE = re.compile(
    r"(?i)(\d+(?:\.\d+)?\s*(?:kg|kgs|gms|gm|g|ml|ltr|l|pc|pcs|cups|tub|box)"
    r"(?:\s*x\s*\d+\s*(?:pc|pcs|g|gm|ml)?)?|"
    r"\d+\s*x\s*\d+(?:ml|g|gm|pc|pcs)?|"
    r"\d+L\s*Plus\s*\d+L|"
    r"\d+ml\s*Plus\s*\d+ml)"
)


def infer_brand(product_name):
    normalized = product_name.replace("I/C", "IC").replace("-", " ")
    first_word = normalized.split()[0] if normalized.split() else ""
    if first_word.upper() == "GALITOS":
        return "Galitos"
    if first_word in BRAND_ALIASES:
        return BRAND_ALIASES[first_word]
    return "Razco"


def infer_unit(product_name):
    matches = UNIT_RE.findall(product_name)
    return matches[-1].strip() if matches else ""


def load_products():
    products = []
    category = None
    for raw_line in CATALOG_PATH.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        parts = [part.strip() for part in re.split(r"\t+", line) if part.strip()]
        if len(parts) >= 2 and PRODUCT_CODE_RE.match(parts[0]):
            product_name = " ".join(parts[1:])
            products.append(
                {
                    "product_code": parts[0],
                    "product_name": product_name,
                    "category": category or "Other",
                    "brand": infer_brand(product_name),
                    "unit_size": infer_unit(product_name),
                }
            )
            continue

        if len(parts) == 1 and not PRODUCT_CODE_RE.match(parts[0]):
            category = parts[0]

    return products


REAL_PRODUCTS = load_products()
PRODUCT_CATEGORIES = sorted({product["category"] for product in REAL_PRODUCTS})
