import requests
from dataclasses import dataclass


@dataclass(slots=True)
class Element:
    atomic_number: int
    symbol: str
    name: str
    atomic_mass: str
    cpk_hex_color: str
    electronic_configuration: str
    electronegativity: float
    atomic_radius: int
    ion_radius: str
    vanDerWaals_radius: str
    ionization_energy: int
    electron_affinity: int
    oxidation_states: int
    standard_state: str
    bonding_type: str
    melting_point: int
    boiling_point: int
    density: float
    group_block: str
    year_of_discovery: int



