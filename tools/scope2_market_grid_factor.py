"""
scope2_market_grid_factor.py - Applies eGRID regional carbon factor to purchased electricity kilowatt-hours
"""
import sys
import json


def calculate_scope2_emissions(electricity_json: str):
    import json
    data = json.loads(electricity_json) if isinstance(electricity_json, str) else electricity_json
    kwh = data.get("kwh_consumed", 50000.0)
    factor = data.get("grid_factor_kg_per_kwh", 0.38)
    mt_co2e = (kwh * factor) / 1000.0
    return {"scope2_mt_co2e": round(mt_co2e, 2), "status": "SCOPE2_CALCULATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "scope2-market-grid-factor"}))
