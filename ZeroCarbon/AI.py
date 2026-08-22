from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

#Executive summary prompts
def achieve_executive_summary(report_data):

    return f"""
    
Act as a decarbonization advisor.

Approved actions:
{report_data["recommended_actions"]}

Business data:

{json.dumps(report_data, indent=2)}

IMPORTANT RULES:

- Use ONLY the supplied data.
- Do NOT invent percentages.
- Do NOT invent savings values.
- Do NOT invent emissions reductions.
- If information is UNAVAILABLE, state that more information is needed.
- Do NOT assume anything

Use ONLY the actions listed under recommended_actions.
Do NOT create, modify, merge, or expand actions.

REQUIREMENTS:
Generate an executive summary based solely on the given business data
Header should be ***Executive Summary*** for users to differentiate between executive summary and roadmap
Separate into paragraphs for readability purposes (no section headers)
Short concise 1 to 2 paragraphs

Professional tone
Use executive-level business language
For stakeholders
Specific, not generic

Only for achieving net-zero executive summary
Focus on:
- Largest emission source
- Distance from net-zero
- Current emissions status
- Carbon intensity
- Solar opportunities if relevant

The executive summary must reference all available solar metrics when solar analysis data is provided.

The executive summary must explain why the approved actions are relevant to the plant's largest emission source.

Base recommendations only on recommended_actions in NET_ZERO_ACTIONS

EXAMPLE:
Executive Summary

Mumbai Plant's current carbon footprint stands at 72,720 units of total
emissions, with net emissions of 60,540 after accounting for existing
offsets. This places the facility 83.25% away from achieving net-zero
status, indicating that substantial action is still required to close the
gap. Electricity is the largest contributor to the plant's emissions
profile at 82.4%, followed by diesel at 12.6% and furnace oil at 5.0%,
with a carbon intensity of 6.05 underscoring the scale of reduction
needed, particularly in electricity-related consumption.
To progress toward net-zero, approved actions include reducing
unnecessary electricity consumption, upgrading energy-intensive
equipment, monitoring energy usage regularly, installing solar panels
where feasible, and increasing renewable electricity usage
Solar analysis points to a meaningful opportunity in support of these
efforts: an estimated annual savings of 80,000, a carbon reduction of
12,300, and a payback period of 5.2 years, positioning solar
investment as a key lever for accelerating the plant's path to net-zero.
"""

def sustain_executive_summary(report_data):

    return f"""
    
Act as a decarbonization advisor.

Approved actions:
{report_data["recommended_actions"]}

Business data:

{json.dumps(report_data, indent=2)}

IMPORTANT RULES:

- Use ONLY the supplied data.
- Do NOT invent percentages.
- Do NOT invent savings values.
- Do NOT invent emissions reductions.
- If information is UNAVAILABLE, state that more information is needed.
- Do NOT assume anything

Use ONLY the actions listed under recommended_actions.
Do NOT create, modify, merge, or expand actions.

REQUIREMENTS:
Generate an executive summary based solely on the given business data
Header should be ***Executive Summary*** for users to differentiate between executive summary and roadmap
Separate into paragraphs for readability purposes (no section headers)
Short concise 1 to 2 paragraphs

Professional tone
Use executive-level business language
For stakeholders
Specific, not generic

Only for sustaining net-zero executive summary:
Focus on:
- Net-zero achievement status
- Current sustainability position
- Renewable energy contribution and solar payback period
- Carbon intensity performance
- Key sustainability risks that could impact future net-zero performance
    Key sustainability risks may include:
    - Increased energy consumption
    -Reduced renewable energy generation
    - Solar panels age
    - Increased production
    - Changes in fuel usuage

- Long-term sustainability monitoring
- Approved sustaining actions

- Recommended sustaining actions ONLY from the recommended_actions in SUSTAIN_NET_ZERO_ACTIONS

EXAMPLE:
Executive Summary

Mumbai Plant has achieved net-zero status, with net emissions of 0
against total emissions of 50,000, fully offset through renewable
energy generation. This reflects a percentage distance of 0% from net-
zero and a carbon intensity of 0, demonstrating that renewable energy generation is successfully offsetting operational emissions.
Electricity remains the plant's largest identified
emission source, though renewable generation now fully
offsets this footprint. Solar continues to underpin this performance,
delivering annual savings of 150,000 and a carbon reduction of
50,000, with a payback period of 3.5 years reflecting strong continued
returns on the existing investment.
Sustaining this position requires ongoing attention to risks that could
affect future net-zero performance, including increased energy
consumption, reduced renewable energy generation, aging solar
infrastructure, increased production, and changes in fuel usage. To
support long-term monitoring and resilience, approved sustaining
actions include monitoring emissions on a monthly basis, conducting
annual energy reviews, maintaining renewable energy usage, tracking
sustainability KPIs, continuing employee awareness programs, and
reviewing emissions performance quarterly.
"""

def achieve_roadmap(report_data):
    return f"""

Act as a decarbonization advisor.

Approved actions:
{report_data["recommended_actions"]}

Business data:

{json.dumps(report_data, indent=2)}

IMPORTANT RULES:

- Use ONLY the supplied data.
- Use ONLY the approved actions.
- Do NOT create new actions.
- Do NOT modify actions.
- Do NOT invent percentages.
- Do NOT invent savings values.
- Do NOT invent emissions reductions.
- If information is UNAVAILABLE, state that more information is needed.
- Do NOT assume anything

Avoid repeating identical explanations across actions.
Each action should have a unique rationale tied to the supplied business data.

Ensure all actions, rationales, milestones, and expected outcomes are consistent with the current emissions profile and approved actions.

Use ONLY the actions listed under recommended_actions.
Do NOT create, modify, merge, or expand actions.

REQUIREMENTS:
Generate an achieve net-zero roadmap based solely on the given business data
Header should be ***Roadmap*** for users to differentiate between executive summary and roadmap

Group related actions under logical roadmap stages.
Each stage should include:
- Objective
- Actions
- Reasons
- Contribution to achieve Net-Zero
- Milestones
- Expected Outcomes
Stages should build progressively toward achieving net-zero.

Actions focused on assessment, monitoring, and planning should typically appear before actions focused on implementation.
Prioritize actions that address the largest emission source before actions that provide secondary benefits.
Actions should be presented in the order they would realistically be implemented.
Earlier actions should establish the foundation for later actions.
Do not assign actions to arbitrary quarters unless supported by the business data.

For each approved action:
1. Explain why the action was selected based on the supplied business data
2. Explain how the action address:
    - Largest emission source
    - Current emissions status
    - Distance from net-zero
    - Carbon intensity
    - Solar analysis (if relevant)

3. Explain how the action contributes to achieving net-zero and how it addresses the facility's current emissions profile.

Use information from:
- Largest emission source
- Distance from net-zero
- Current emissions status
- Solar analysis (if relevant)

Format:
Objective (What are we addressing and solving in this roadmap stage?)
Action
Reason (Why was this action selected?)
Contribution to net-zero (How does it support net-zero?)
Milestone (What indicates that the action has been completed?)
Use measurable completion events where possible, but do not invent percentages, savings, emissions reductions, or unsupported numerical targets.

Expected outcomes (Should describe anticipated operational or sustainability benefits from completing the action?)
Do not invent numerical improvements, savings, or emissions reductions.

Specific, not generic


EXAMPLE:
Achieving Roadmap



"""

def sustain_roadmap(report_data):
    return f"""

Act as a decarbonization advisor.

Approved actions:
{report_data["recommended_actions"]}

Business data:

{json.dumps(report_data, indent=2)}

IMPORTANT RULES:

- Use ONLY the supplied data.
- Use ONLY the approved actions.
- Do NOT create new actions.
- Do NOT modify actions.
- Do NOT invent percentages.
- Do NOT invent savings values.
- Do NOT invent emissions reductions.
- If information is UNAVAILABLE, state that more information is needed.
- Do NOT assume anything

Avoid repeating identical explanations across actions.
Each action should have a unique rationale tied to the supplied business data.

Ensure all actions, rationales, milestones, and expected outcomes are consistent with the current emissions profile and approved actions.

Use ONLY the actions listed under recommended_actions.
Do NOT create, modify, merge, or expand actions.

REQUIREMENTS:
Generate a maintain net-zero roadmap based solely on the given business data
Label ***Roadmap*** for users to differentiate between executive summary and roadmap

Group related actions under logical roadmap stages.
Each stage should include:
- Objective
- Actions
- Reasons
- Contribution to sustaining net-zero
- Milestons
- Expected Outcomes
Stages should build progressively toward maintaining net-zero performance rather than reducing emissions.

Examples of stages may include:
- Monitoring and visibility
- Renewable energy management
- Performance reviews
- Continuous improvements

Actions should be presented in the order they would realistically be implemented.
Earlier actions should establish the foundation for later actions.
Do not assign actions to arbitrary quarters unless supported by the business data.

For each approved action:
1. Explain why the action was selected based on the supplied business data
2. Explain how the action address:
    - Current sustainability performance
    - Carbon intensity
    - Solar analysis (if relevant)

3. Explain how the action contributes to maintaining net-zero and how it addresses the facility's current emissions profile.

Use information from:
- Current sustainability performace
- Carbon intensity
- Renewable energy contribution
- Solar analysis (if relevant)

Where relevant, explain any risks that the action helps mitigate, such as:
- Increased energy consumption
- Reduced renewable energy generation
- Aging solar infrastructure
- Increased production demand
- Changes in fuel usage

Format:
Objective (What are we addressing and solving in this roadmap stage?)
Action
Reason (Why was this action selected?)
Contribution to maintaining net-zero (How does it support net-zero?)
Milestone (What indicates that the action has been completed?)
Use measurable completion events where possible, but do not invent percentages, savings, emissions reductions, or unsupported numerical targets.

Expected outcomes (Should describe anticipated operational or sustainability benefits from completing the action?)
Do not invent numerical improvements, savings, or emissions reductions.

Specific, not generic

EXAMPLE:
Sustain Roadmap



"""

#Call API for generating executive summary
def generate_executive_summary(
    report_data
):

    status = report_data[
        "business_insights"
    ][
        "status"
    ]

    if status == "Net-Zero":

        prompt = sustain_executive_summary(
            report_data
        )

    else:

        prompt = achieve_executive_summary(
            report_data
        )

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

#Call API for generating roadmap
def generate_roadmap(
    report_data
):

    status = report_data[
        "business_insights"
    ][
        "status"
    ]

    if status == "Net-Zero":

        prompt = sustain_roadmap(
            report_data
        )

    else:

        prompt = achieve_roadmap(
            report_data
        )

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content