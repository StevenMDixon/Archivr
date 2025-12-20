import re
import unicodedata
from domain.date_normalizer import process_file_name

class FileNameUtils:
    
    @staticmethod
    def normalize_unicode(file_name: str) -> str:
        return unicodedata.normalize("NFKC", file_name)

    @staticmethod
    def normalize_dates(file_name: str) -> str:
        return process_file_name(file_name)

    @staticmethod
    def remove_terms(file_name: str) -> str:
          # Remove commercial / ad phrases
        patterns = [
            r"\bTV\s*Commercial\b",
            r"\bCommercial\s+from\b",
            r"\bCommercial\b",
            r"(^|[\s._-])ad\s*-\s*"
        ]

        for p in patterns:
            file_name = re.sub(p, " ", file_name, flags=re.IGNORECASE)

        return file_name
    
    @staticmethod
    def remove_special_characters(file_name: str) -> str:
        return re.sub(r'[\"\'<>:/\\|?*™]', '', file_name)

    @staticmethod
    def normalize_whitespace_punctuation(file_name: str) -> str:
        file_name = re.sub(r"^[\s\-_.]+", "", file_name)
        file_name = re.sub(r"[\s\-_.]+$", "", file_name)
        file_name = re.sub(r"\s{2,}", " ", file_name)
        return file_name
    
    @staticmethod
    def remove_youtube_tag(file_name: str) -> str:
         file_name = re.sub(r"\[[^\s\]]+\]", "", file_name)
         return file_name