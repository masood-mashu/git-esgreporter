"""
scope1_emission_calculator.py - Computes metric tonnes CO2e from natural gas and diesel fuel consumption
"""
import sys
import json


def calculate_scope1_emissions(fuel_data_json: str):
    import json
    data = json.loads(fuel_data_json) if isinstance(fuel_data_json, str) else fuel_data_json
    therms = data.get("natural_gas_therms", 1000.0)
    gallons = data.get("diesel_gallons", 200.0)
    mt_co2e = (therms * 0.0053) + (gallons * 0.01021)
    return {"scope1_mt_co2e": round(mt_co2e, 2), "status": "SCOPE1_CALCULATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "scope1-emission-calculator"}))
