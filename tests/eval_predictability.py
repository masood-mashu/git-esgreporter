"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitEsgReporter.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.scope1_emission_calculator import *
from tools.scope2_market_grid_factor import *
from tools.ghg_protocol_certifier import *

class TestGitEsgReporterPredictability(unittest.TestCase):
    def test_scope1_emission_calculator(self):
        res = calculate_scope1_emissions('{"natural_gas_therms": 2000.0, "diesel_gallons": 500.0}')
        self.assertGreater(res["scope1_mt_co2e"], 10.0)
        self.assertEqual(res["status"], "SCOPE1_CALCULATED")

    def test_scope2_market_grid_factor(self):
        res = calculate_scope2_emissions('{"kwh_consumed": 100000.0, "grid_factor_kg_per_kwh": 0.4}')
        self.assertEqual(res["scope2_mt_co2e"], 40.0)
        self.assertEqual(res["status"], "SCOPE2_CALCULATED")

    def test_ghg_protocol_certifier(self):
        res = certify_ghg_report('{"total_mt_co2e": 55.7, "reporting_year": 2026}')
        self.assertTrue(res["certified"])
        self.assertEqual(res["status"], "AUDIT_CERTIFIED")


if __name__ == "__main__":
    unittest.main()
