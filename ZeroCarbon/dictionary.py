#dictionary.py

from actions import (
    NET_ZERO_ACTIONS,
    SUSTAIN_NET_ZERO_ACTIONS
)

def context_package(
    carbon_data,
    solar_data,
    timeline_months
):
    
    status = carbon_data["status"]

    if status == "Net-Zero":
        selected_actions = (
            SUSTAIN_NET_ZERO_ACTIONS
        )
    else:
        largest_source = (
            carbon_data[
                "largest_emission_source"
            ]
        )
        selected_actions = (
            NET_ZERO_ACTIONS[
                largest_source
            ]
        )

    return {

        "plant_information": {
            "plant_name":
            carbon_data["plant_name"]
        },

        "carbon_assessment":
        carbon_data,

        "solar_analysis":
        solar_data,

        "net_zero_goal": {
            "target_months":
            timeline_months
        },

        "business_insights": {

            "largest_emission_source":
            carbon_data["largest_emission_source"],

            "status":
            carbon_data["status"],

            "distance_from_net_zero":
            carbon_data["percentage_distance"],

            "carbon_intensity":
            carbon_data["carbon_intensity"],

            "solar_payback_years":
            solar_data["payback_years"]

        },

        "recommended_actions":
        selected_actions

    }