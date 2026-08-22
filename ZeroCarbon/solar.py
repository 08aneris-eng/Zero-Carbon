# solar.py

from carbon import ELECTRICITY_FACTOR

def calculate_solar_analysis(
    annual_electricity_usage,
    annual_electricity_cost,
    solar_generation,
    solar_installation_cost
):

    average_tariff = (
        annual_electricity_cost /
        annual_electricity_usage
        if annual_electricity_usage > 0
        else 0
    )

    annual_savings = (
        solar_generation *
        average_tariff
    )

    carbon_reduction = (
        solar_generation *
        ELECTRICITY_FACTOR
    )

    solar_percentage = (
    (solar_generation / annual_electricity_usage) * 100
    if annual_electricity_usage > 0
    else 0
    )

    payback_years = (
        solar_installation_cost /
        annual_savings
        if annual_savings > 0
        else 0
    )

    return {
        "average_tariff": round(
            average_tariff, 2
        ),
        "annual_savings": round(
            annual_savings, 2
        ),
        "carbon_reduction": round(
            carbon_reduction, 2
        ),
        "solar_coverage_pct": round(
            solar_percentage, 2    
        ),
        "payback_years": round(
            payback_years, 2
        )
    }
