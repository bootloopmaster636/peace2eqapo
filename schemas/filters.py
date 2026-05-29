from enum import Enum


class Filters(Enum):
    PEAK = 0
    LOW_PASS = 1
    HIGH_PASS = 2
    BAND_PASS = 3
    LOW_SHELF = 4
    HIGH_SHELF = 5
    NOTCH = 6
    ALL_PASS = 7
    LOW_SHELF_Q_SLOPE = 14
    HIGH_SHELF_Q_SLOPE = 15

    def to_apo_filter(self) -> str:
        match self:
            case Filters.PEAK:
                return "PK"
            case Filters.LOW_PASS:
                return "LP"
            case Filters.HIGH_PASS:
                return "HP"
            case Filters.BAND_PASS:
                return "BP"
            case Filters.LOW_SHELF:
                return "LS"
            case Filters.HIGH_SHELF:
                return "HS"
            case Filters.NOTCH:
                return "NO"
            case Filters.ALL_PASS:
                return "AP"
            case Filters.LOW_SHELF_Q_SLOPE:
                return "LSC"
            case Filters.HIGH_SHELF_Q_SLOPE:
                return "HSC"
