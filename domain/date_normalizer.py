import re
import unicodedata

class DateNormalizer:
    @staticmethod
    def _normalize_two_digit_year(y: int) -> int:
        return 1900 + y if y >= 30 else 2000 + y

    @staticmethod
    def _normalize_decade(value: str) -> int:
        value = value.replace("'", "").strip()
        return DateNormalizer._normalize_two_digit_year(int(value))

    @staticmethod
    def _remove_bracketed_years(text: str):
        years = []

        bracket_pattern = r"[\[\(\{]\s*([0-9,./\-\s]+)\s*[\]\)\}]"

        def repl(m):
            content = m.group(1)
            if re.fullmatch(r"[0-9,./\-\s]+", content):
                # Extract years from content
                nums = [int(n) if len(n) == 4 else DateNormalizer._normalize_two_digit_year(int(n))
                        for n in re.findall(r"\d{2,4}", content)]
                years.extend(nums)
                return " "
            return m.group(0)  # keep bracket if it contains letters

        text = re.sub(bracket_pattern, repl, text)
        return text, years

    @staticmethod
    def _extract_years(text: str):
        text = unicodedata.normalize("NFKC", text)
        all_years = []

        text, years = DateNormalizer._remove_bracketed_years(text)
        all_years.extend(years)

        date_pattern = r"\b\d{1,2}[./-]\d{1,2}[./-](\d{2,4})\b"
        for match in re.finditer(date_pattern, text):
            g = match.group(1)
            y = int(g)
            if len(g) == 2:
                y = DateNormalizer._normalize_two_digit_year(y)
            all_years.append(y)
        text = re.sub(date_pattern, " ", text)

        bare_year_pattern = r"\b(19\d{2}|20\d{2})\b"
        for match in re.finditer(bare_year_pattern, text):
            all_years.append(int(match.group(1)))
        text = re.sub(bare_year_pattern, " ", text)

        decade_pattern = r"\b(\d{2})'?\s*s\b"
        for match in re.finditer(decade_pattern, text, flags=re.IGNORECASE):
            all_years.append(DateNormalizer._normalize_decade(match.group(1)))
        text = re.sub(decade_pattern, " ", text, flags=re.IGNORECASE)

        text = re.sub(r"[\[\(\{]\s*[\]\)\}]", "", text)
        text = re.sub(r"\s{2,}", " ", text).strip()

        return text, all_years

    @staticmethod
    def normalize(text: str) -> str:
        cleaned, years = DateNormalizer._extract_years(text)
        if not years:
            return cleaned
        earliest = min(years)
        return f"{cleaned} {earliest}".strip()
