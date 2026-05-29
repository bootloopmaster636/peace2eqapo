from loguru import logger

from schemas.filters import Filters
from schemas.peq import EqBand, EqPreset


class ApoGenerator:
    def __init__(self):
        pass

    def generate_apo(self, eq_preset: EqPreset) -> list[str]:
        try:
            result = []

            preamp_string = f"Preamp: {eq_preset.preamp_gain} db"
            result.append(preamp_string)

            for band in eq_preset.band_list:
                band_result = self.__generate_band_config(band)
                result.append(band_result)

            return result
        except Exception as e:
            logger.error(f"Error generating EQ APO config: {e}")
            raise e

    def __generate_band_config(self, band: EqBand) -> str:
        try:
            band_index = f"Filter {band.index}"
            state = "ON" if band.enabled else "OFF"
            filter = band.filter.to_apo_filter()
            freq = f"Fc {band.frequency} Hz"
            gain = f"Gain {band.gain} dB"
            q_factor = f"Q {band.q_factor}"

            return " ".join([band_index, state, filter, freq, gain, q_factor])
        except Exception as e:
            logger.error(f"Error generating band config: {e}")
            raise e
