import unittest
from converter import CONVERSION_FACTORS

class TestConversionFactors(unittest.TestCase):

    def test_length_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['length']['m'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['length']['ft'], 0.3048)
        self.assertAlmostEqual(CONVERSION_FACTORS['length']['in'], 0.0254)

    def test_mass_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['mass']['kg'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['mass']['lb'], 0.453592)
        self.assertAlmostEqual(CONVERSION_FACTORS['mass']['oz'], 0.0283495)

    def test_time_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['time']['s'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['time']['min'], 60.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['time']['h'], 3600.0)

    def test_temperature_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['temperature']['K'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['temperature']['C'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['temperature']['F'], 0.555556)

    def test_electric_current_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['electric_current']['A'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['electric_current']['mA'], 0.001)
        self.assertAlmostEqual(CONVERSION_FACTORS['electric_current']['kA'], 1000.0)

    def test_amount_of_substance_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['amount_of_substance']['mol'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['amount_of_substance']['mmol'], 0.001)
        self.assertAlmostEqual(CONVERSION_FACTORS['amount_of_substance']['kmol'], 1000.0)

    def test_luminous_intensity_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['luminous_intensity']['cd'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['luminous_intensity']['lm'], 1.0)

    def test_speed_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['speed']['m/s'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['speed']['km/h'], 0.277778)
        self.assertAlmostEqual(CONVERSION_FACTORS['speed']['mph'], 0.44704)

    def test_area_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['area']['m^2'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['area']['ft^2'], 0.092903)
        self.assertAlmostEqual(CONVERSION_FACTORS['area']['ac'], 4046.86)

    def test_volume_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['volume']['m^3'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['volume']['L'], 0.001)
        self.assertAlmostEqual(CONVERSION_FACTORS['volume']['gal'], 0.003785)

    def test_pressure_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['pressure']['Pa'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['pressure']['bar'], 100000.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['pressure']['psi'], 6894.76)

    def test_energy_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['energy']['J'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['energy']['cal'], 0.239006)
        self.assertAlmostEqual(CONVERSION_FACTORS['energy']['kWh'], 3600000.0)

    def test_power_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['power']['W'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['power']['hp'], 745.7)
        self.assertAlmostEqual(CONVERSION_FACTORS['power']['BTU/h'], 0.293071)

    def test_frequency_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['frequency']['Hz'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['frequency']['kHz'], 1000.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['frequency']['MHz'], 1000000.0)

    def test_digital_storage_conversion(self):
        self.assertAlmostEqual(CONVERSION_FACTORS['digital_storage']['B'], 1.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['digital_storage']['KB'], 1024.0)
        self.assertAlmostEqual(CONVERSION_FACTORS['digital_storage']['MB'], 1048576.0)
"""
Converts a temperature value from one unit to another.

Args:
    value (float): The temperature value to convert.
    from_unit (str): The unit of the input temperature value. Can be 'C', 'F', or 'K'.
    to_unit (str): The unit to convert the temperature to. Can be 'C', 'F', or 'K'.

Returns:
    float: The converted temperature value.
"""
