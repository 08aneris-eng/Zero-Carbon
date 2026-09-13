# ZeroCarbon 
> AI-driven sustainability tool for manufacturing plants
> 
> Tool developed during Deloitte India internship

## Tool Overview
An AI-driven decision support system that helps manufacturing plants assess their carbon footprint, identify opportunities 
for emissions reduction, and support the achievement or sustainment of net-zero operations. Based on the plant’s current 
emissions profile, the tool provides guidance tailored to either achieving zero carbon or sustaining the net-zero status.

## Problem statement

Manufacturing plants are significant contributors to carbon and are under increasing pressure to meet net-zero targets. While many sustainability tools exist, businesses often struggle to understand their emissions profile, evaluate renewable energy opportunities, and determine the actions required to achieve or sustain zero carbon.  
  
As a result, businesses require a solution that can transform emission data into clear, actionable recommendations that support decision-making and long-term sustainability efforts.

## Solution

ZeroCarbon helps manufacturing plants measure, reduce, and sustain their journey to being net-zero. It combines:  
  
• Measure carbon emissions  
• Identify net-zero gap  
• Evaluate solar opportunities  
• Calculate solar savings and payback time  
• Generate AI-powered executive summary  
• Generate AI-powered personalized sustainability roadmap
  
The tool acts as a decision support system that assists in making informed sustainability decisions rather than automatically  
implementing them.

Note: The carbon emissions and solar calculations are Python based.

## Example
**Achieving net-zero executive summary**
<img width="598" height="157" alt="Screenshot 2026-07-23 064702" src="https://github.com/user-attachments/assets/1964f530-81ce-4c23-a0a9-5e8f71c38707" />


**Snippet of achieving net-zero roadmap**
> ***Roadmap***
> 
> **Stage 1: Establish electricity visibility**
> **Objective:** Address the electricity-related emissions profile in a progressive, data-grounded sequence.
> 
> **Action:** Monitor energy usage regularly
> 
> **Reason:** Electricity is Mumbai Plant’s largest emission source, and its current status is Action Needed.
> 
> **Contribution to net-zero:** Creates visibility into electricity usage while the plant is 83.25% from net-zero and has a carbon
> intensity of 6.05.
> 
> **Milestone:** A regular energy-use monitoring process is in place and records are available for review.
> 
> **Expected outcomes:** Better visibility of electricity use and a foundation for the remaining approved actions.

**Sustaining net-zero executive summary**
<img width="595" height="134" alt="Screenshot 2026-07-23 064549" src="https://github.com/user-attachments/assets/66c36b63-60e2-4011-b5af-c33b7c50f291" />


**Sustaining net-zero roadmap**

> ***Roadmap***
> 
> **Stage 1: Monitor and Review Net-Zero Performance**
> 
> **Objective:** Maintain Mumbai Plant’s Net-Zero status by monitoring
> emissions performance, carbon intensity, and sustainability
> indicators.
>
> **Action:** Monitor emissions every month
> 
> **Reason:** Mumbai Plant has achieved Net-Zero status with total emissions of 50,000, renewable offset of 50,000, net emissions of 0, and a percentage distance of 0% from net-zero. Monthly monitoring is needed to confirm this position is sustained.
>
> **Contribution to sustaining net-zero:** Monitoring helps identify changes in emissions that could affect the current net-zero position, including increased energy consumption, increased production, or changes in fuel usage.
>
> **Milestone:** Monthly emissions records are maintained and available for review.
>
> **Expected outcomes:** Ongoing visibility of emissions performance and earlier identification of risks that could affect net-zero status.

## Tech Stack
**Coding language**:
 Python
 
**API**:
 Hugging Face Inference API (meta-llama/Llama-3.1-8B-Instruct)
	
**Development environment**:
Visual Studio Code

## Installation / Setup
Clone this repository in Visual Studio Code

Install the latest Python version from [https://www.python.org/downloads/](https://www.python.org/downloads/)

Verify Python in Visual Studio Code
Open a new terminal
Run the follow command

      python --version
      
Install the Python extension in Visual Studio Code  
1. Click the Extensions icon in Visual Studio Code  
2. Search for Python  
3. Install Python published by Microsoft  
  
Select your Python interpreter  
  
Create a virtual environment


## Known Limitations  
- Manual inputs
- Generic AI-generated roadmaps
- Limited scope (May not cover all the emission sources or solar sources used by a manufacturing plant)
- Simplified solar payback calculations (Doesn't take into account factors like inflation)
