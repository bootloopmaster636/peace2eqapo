from pydantic import BaseModel, Field

from schemas.filters import Filters


class EqBand(BaseModel):
    index: int = Field(description="Position of this band. Starts from 1.")
    frequency: float = Field(description="This band frequency in Hz")
    q_factor: float = Field(description="This band quality factor")
    gain: float = Field(description="This band gain in dB")
    filter: Filters = Field(description="This band filter type")
    enabled: bool = Field(description="Whether this band is enabled", default=True)


class EqPreset(BaseModel):
    preamp_gain: float = Field(description="Preamp gain in dB")
    band_list: list[EqBand] = Field(description="List of EQ bands")
