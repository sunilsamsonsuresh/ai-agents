from crewai import Agent, Task, Crew
from toolbox import scrape_tool, search_tool


class Researcher:
    def __init__(self, topic, country, verbose=True):
        self.topic = topic
        self.country = country
        self.verbose = verbose
        self.role = f'Researcher of {self.topic}'
        self.goal = f"Conduct an in-depth analysis of the {self.topic} to write a blog"
        self.tools = [search_tool, scrape_tool]
        self.backstory = (
            f"As a researcher of the {self.topic}, "
            f"your task is to navigate and extract critical information "
            f"from websites, files, reports, and CSV files. "
            f"Focus particularly on the details of {self.country} for the blog."
        )

    def conduct_research(self):

        researcher = Agent(
            role=self.role,
            goal=self.goal,
            verbose=True,
            tools=[search_tool, scrape_tool],
            backstory=self.backstory
        )

        research_task = Task(
            description=(
                "Analyze the relevant sources to "
                "extract detailed information about the visa requirements "
                "for immigration and relocation to {country}. "
                "Identify the types of visas available, application processes, "
                "required documentation, and key legal regulations."
            ),
            expected_output=(
                "A comprehensive guide detailing the visa types available for {country}, "
                "including eligibility criteria, application procedures, necessary "
                "documents, processing times, and any recent changes in immigration "
                "policy. Provide clear insights into the relocation process."
            ),
            agent=researcher
        )

        return researcher, research_task


if __name__ == '__main__':
    topic = 'Work Visa Requirements'
    country = 'Germany'

    research_agent = Researcher(topic, country)

    researcher, research_task = research_agent.conduct_research()

    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=2
    )

    inputs = {
        "topic": topic,
        "country": country
    }

    research_content = crew.kickoff(inputs=inputs)

    print(research_content)
