# carbon.py

ELECTRICITY_FACTOR = 0.82
DIESEL_FACTOR = 2.70
FURNACE_OIL_FACTOR = 3.12

def calculate_emissions(
    plant_name,
    electricity_kwh,
    diesel_litres,
    furnace_oil_litres,
    renewable_kwh,
    production_units
):
    electricity_emissions = (
        electricity_kwh * ELECTRICITY_FACTOR
    )

    diesel_emissions = (
        diesel_litres * DIESEL_FACTOR
    )

    furnace_oil_emissions = (
        furnace_oil_litres *
        FURNACE_OIL_FACTOR
    )

    sources = {
    "Electricity": electricity_emissions,
    "Diesel": diesel_emissions,
    "Furnace Oil": furnace_oil_emissions
    }

    largest_emission_source = max(
        sources,
        key=sources.get
    )

    total_emissions = (
        electricity_emissions +
        diesel_emissions +
        furnace_oil_emissions
    )

    electricity_percentage = (
        (electricity_emissions / total_emissions) * 100
        if total_emissions > 0
        else 0
    )

    diesel_percentage = (
        (diesel_emissions / total_emissions) * 100
        if total_emissions > 0
        else 0
    )

    furnace_oil_percentage = (
        (furnace_oil_emissions / total_emissions) * 100
        if total_emissions > 0
        else 0
    )

    renewable_offset = (
        renewable_kwh *
        ELECTRICITY_FACTOR
    )

    net_emissions = max(
        total_emissions -
        renewable_offset,
        0
    )

    percentage_distance = (
        (net_emissions / total_emissions) * 100
        if total_emissions > 0
        else 0
    )

    carbon_intensity = (
        net_emissions / production_units
        if production_units > 0
        else 0
    )

    if percentage_distance == 0:
        status = "Net-Zero"

    elif percentage_distance < 30:
        status = "Close To Net-Zero"

    elif percentage_distance < 60:
        status = "Moderate"

    else:
        status = "Action Needed"

    largest_emission_source = max(
        sources,
        key=sources.get
    )

    return {
        "plant_name": plant_name,
        "electricity_emissions": round(
            electricity_emissions, 2
        ),
        "diesel_emissions": round(
            diesel_emissions, 2
        ),
        "furnace_oil_emissions": round(
            furnace_oil_emissions, 2
        ),
        "total_emissions": round(
            total_emissions, 2
        ),

        "emission_breakdown": {
            "electricity_percentage": round(
                electricity_percentage, 2
            ),
            "diesel_percentage": round(
                diesel_percentage, 2
            ),
            "furnace_oil_percentage": round(
                furnace_oil_percentage, 2
            )
        },

        "renewable_offset": round(
            renewable_offset, 2
        ),
        "net_emissions": round(
            net_emissions, 2
        ),
        "percentage_distance": round(
            percentage_distance, 2
        ),
        "carbon_intensity": round(
            carbon_intensity, 2
        ),
        "largest_emission_source":
        largest_emission_source,
        "status": status
    }
