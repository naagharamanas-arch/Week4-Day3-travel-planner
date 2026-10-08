from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

load_dotenv()

city = input("Which city? ")

planner = Agent(
    role="Travel Planner",
    goal="Suggest three interesting places to visit in the given city.",
    backstory="You are a helpful travel planner who gives clear and practical suggestions to travelers.",
    verbose=True
)

task = Task(
    description="Suggest exactly 3 places to visit in {city}.",
    expected_output="A numbered list containing exactly 3 places to visit in {city}, with a short reason for each place.",
    agent=planner
)

crew = Crew(
    agents=[planner],
    tasks=[task]
)

print(crew.kickoff(inputs={"city": city}))