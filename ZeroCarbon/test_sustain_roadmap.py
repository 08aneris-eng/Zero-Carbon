#Sustaining roadmap
from AI import generate_roadmap

report_data = {

    "plant_information": {
        "plant_name": "Mumbai Plant"
    },

    "carbon_assessment": {

        "total_emissions": 50000,

        "renewable_offset": 50000,

        "net_emissions": 0,

        "percentage_distance": 0,

        "carbon_intensity": 0,

        "largest_emission_source": "Electricity",

        "status": "Net-Zero"
    },

    "solar_analysis": {

        "annual_savings": 150000,

        "carbon_reduction": 50000,

        "payback_years": 3.5
    },

    "business_insights": {

        "status": "Net-Zero"
    },

    "recommended_actions": [

        "Monitor emissions every month",

        "Conduct annual energy reviews",

        "Maintain renewable energy usage",

        "Track sustainability KPIs"
    ]
}

roadmap = generate_roadmap(
    report_data
)

print(roadmap)