from crewai import Agent, Task, Crew
from toolbox import scrape_tool, search_tool


class Planner:
    def __init__(self, topic, country, verbose=True):
        # super().__init__(topic, country, verbose)
        self.role = "Content Planner"
        self.topic = topic
        self.goal = f"Plan engaging a more relevant content on {self.topic} from official sources"
        self.country = country
        self.verbose = verbose
        self.tools = [search_tool, scrape_tool],
        self.backstory = (f"As a content planner, your task is to plan a article \n"
                          f"about immigration, relocation & visa. Gather \n"
                          f"accurate and recent info to help the audience \n"
                          f"understand about the steps and process involved. \n"
                          f"Provide a details analysis about the {self.country}'s \n"
                          f"visa process")

    def conduct_planning(self):

        planner = Agent(
            role=self.role,
            goal=self.goal,
            verbose=True,
            tools=[search_tool, scrape_tool],
            backstory=self.backstory
        )

        planning_task = Task(
            description=(
                "1. **Research and Define the Topic**: \n"
                "   - Gather information on immigration, relocation, and visa processes. \n"
                "   - Identify recent trends and challenges in {country}'s immigration policies.\n\n"

                "2. **Analyze Official Sources**: \n"
                "   - Collect data from government websites, legal documents, and trusted news sources.\n"
                "   - Highlight changes in policies and their implications.\n\n"

                "3. **Write the Introduction**: \n"
                "   - Provide a brief overview of the current immigration landscape in {country}.\n"
                "   - Explain the significance of understanding immigration processes.\n\n"

                "4. **Detailed Process Analysis**: \n"
                "   - Break down the visa application process step-by-step for {country}.\n"
                "   - Include key documents required, fees, and timelines.\n\n"

                "5. **Compare with Other Countries**: \n"
                "   - Analyze how {country}'s immigration policies compare with those of neighboring countries.\n"
                "   - Use data and reports to support your analysis.\n\n"

                "6. **Identify the Target Audience**: \n"
                "   - Determine who will benefit most from this article (e.g., potential immigrants, legal advisors).\n"
                "   - Tailor the content to meet their needs and interests.\n\n"

                "7. **Develop Content Outline**: \n"
                "   - Create a structured outline with key sections and points to cover.\n"
                "   - Include a clear call to action for readers.\n\n"

                "8. **Incorporate SEO Keywords**: \n"
                "   - Identify relevant keywords related to immigration and visas.\n"
                "   - Ensure these keywords are strategically placed throughout the content.\n\n"

                "9. **Conclusion and Recommendations**: \n"
                "   - Summarize the findings and provide actionable insights.\n"
                "   - Suggest improvements or future considerations for {country}'s immigration policies.\n"
            ),
            expected_output=(
                "A comprehensive content plan that includes:\n"
                "- An outline with key sections and points.\n"
                "- Audience analysis and tailored content strategy.\n"
                "- SEO keywords and placement strategy.\n"
                "- Data sources and references.\n"
            ),
            agent=planner
        )

        return planner, planning_task


if __name__ == '__main__':
    topic = 'Work Visa Requirements'
    country = 'Germany'

    planner_agent = Planner(topic, country)

    planner, planning_task = planner_agent.conduct_planning()

    crew = Crew(
        agents=[planner],
        tasks=[planning_task],
        verbose=2
    )

    inputs = {
        "topic": topic,
        "country": country
    }

    planner_content = crew.kickoff(inputs=inputs)

    print(planner_content)