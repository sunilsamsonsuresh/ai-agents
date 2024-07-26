from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

class Writer:
    def __init__(self, topic, country, verbose=True):
        self.role = "Content Writer"
        self.topic = topic
        self.goal = f"Write an insightful and factually accurate opinion piece on the {self.topic}"
        self.country = country
        self.verbose = verbose
        self.backstory = (
                f"Your task is to write a new opinion piece on the {self.topic} "
                f"based on the Content Planner's outline. "
                f"Provide objective insights supported by the planner's information,"
                f"acknowledging when statements are opinions.")

    def writing(self):
        writer = Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            allow_delegation=False,
            verbose=True
        )

        writing_task = Task(
            description=(
                f"1. Use the content plan to craft a compelling blog post on {self.topic}\n"
                "2. Incorporate SEO keywords naturally.\n"
                "3. Name sections/subtitles engagingly.\n"
                "4. Ensure the post has an engaging introduction, insightful body, "
                "and summarizing conclusion.\n"
                "5. Proofread for grammatical errors"
            ),
            expected_output="A well-written blog post in markdown format, ready for "
                            "publication, with detailed sections.",
            agent=writer
        )

        return writer, writing_task


if __name__ == '__main__':
    topic = 'Work Visa Requirements'
    country = 'Germany'

    writer_agent = Writer(topic, country)

    writer, writing_task = writer_agent.writing()

    crew = Crew(
        agents=[writer],
        tasks=[writing_task],
        verbose=2
    )

    inputs = {
        "topic": topic,
        "country": country
    }

    writer_content = crew.kickoff(inputs=inputs)

    print(writer_content)
