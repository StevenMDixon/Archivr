from dataclasses import dataclass

@dataclass
class MediaItem():
    file_name: str
    normalized_name: str
    extension: str
    path: str
    year: str = ''
    rating: str = ''
    season: str = ''
    runtime: str = ''
    resolution: str = ''
    network: str = ''
    watermark: bool = False
    formmated: bool = False
    index: int = -1