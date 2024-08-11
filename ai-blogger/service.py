from content_researcher import Researcher
from content_planner import Planner
from content_writer import Writer
from crewai import Crew

if __name__ == '__main__':
    topic = 'New Updated Policies'
    country = 'Germany'

    research_agent = Researcher(topic, country)
    planner_agent = Planner(topic, country)
    writer_agent = Writer(topic, country)

    researcher, research_task = research_agent.conduct_research()
    planner, planning_task = planner_agent.conduct_planning()
    writer, writing_task = writer_agent.writing()

    crew = Crew(
        agents=[researcher, planner, writer],
        tasks=[research_task, planning_task, writing_task],
        verbose=2
    )

    inputs = {
        "topic": topic,
        "country": country
    }

    seo_content = crew.kickoff(inputs=inputs)

    print(seo_content)
