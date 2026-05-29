import configparser

from loguru import logger

from schemas.filters import Filters
from schemas.peq import EqBand, EqPreset


class PeaceParser:
    def __init__(self):
        self.parser = configparser.ConfigParser()

    def parse_peace(self, input_str: str) -> EqPreset:
        try:
            # Parse config
            self.parser.read_string(input_str)

            freq_list = dict(self.parser["Frequencies"])
            gain_list = dict(self.parser["Gains"])
            qualities = dict(self.parser["Qualities"])
            filter_list = dict(self.parser["Filters"])
            disabled_list = dict(self.parser["Disabled"])
            general_config = dict(self.parser["General"])

            # Map list to schema
            result = []
            for i in range(1, len(freq_list) + 1):
                # Parse frequency, gain, and quality
                freq = float(freq_list[f"frequency{i}"])
                gain = float(gain_list[f"gain{i}"])
                quality = float(qualities[f"quality{i}"])

                # Parse enabled state
                disabled_state = disabled_list.get(f"disabled{i}", None)
                enabled = disabled_state is None

                # Parse filter
                try:
                    filter_idx = filter_list.get(f"filter{i}", None)

                    if filter_idx is None:
                        filter = Filters.PEAK
                    else:
                        filter = Filters(int(filter_idx))
                except ValueError:
                    logger.warning(
                        f"Invalid filter index {filter_idx} at band {i}. Using PEAK filter instead."
                    )
                    filter = Filters.PEAK
                    enabled = False

                result.append(
                    EqBand(
                        index=i,
                        frequency=freq,
                        gain=gain,
                        q_factor=quality,
                        filter=filter,
                        enabled=enabled,
                    )
                )

            preamp = float(general_config["preamp"])

            return EqPreset(preamp_gain=preamp, band_list=result)
        except Exception as e:
            logger.error(
                "Looks like this is not a valid PEACE Equalizer file. Check and try again."
            )
            raise e
