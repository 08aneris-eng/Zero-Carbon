#Achieving roadmap

from AI import generate_roadmap

report_data = {

    "plant_information": {
        "plant_name": "Mumbai Plant"
    },

    "carbon_assessment": {

        "total_emissions": 72720,

        "net_emissions": 60540,

        "percentage_distance": 83.25,

        "carbon_intensity": 6.05,

        "largest_emission_source": "Electricity",

        "status": "Action Needed"
    },

    "solar_analysis": {

        "annual_savings": 80000,

        "carbon_reduction": 12300,

        "payback_years": 5.2
    },

    "business_insights": {

        "status": "Action Needed"
    },

    "recommended_actions": [

        "Reduce unnecessary electricity consumption",

        "Upgrade energy-intensive equipment",

        "Monitor energy usage regularly",

        "Install solar panels where feasible",

        "Increase renewable electricity usage"
    ]
}

roadmap = generate_roadmap(
    report_data
)

print(roadmap)