from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


from crewai_tools import(
    SerperDevTool,
    FileWriterTool,
    ScrapeWebsiteTool,
    
)

#set up API
# IA-Gov modification 2026-10-17: preserve operator credential; never overwrite it.
if not os.environ.get("SERPER_API_KEY"):
    raise RuntimeError("SERPER_API_KEY required by SerperDevTool; Serper is not an unlimited free service")


#instantiate tools
search_tool = SerperDevTool()
scrape_website = ScrapeWebsiteTool()
file_writer = FileWriterTool()


@CrewBase
class AiLatestPoliticalNews():
    """AiLatestPoliticalNews  crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    mistral_llm = LLM(
        model = "ollama/mistral",
        base_url = "http://localhost:11434", 
        
    )
    
    @agent
    def retrive_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrive_news'], # type: ignore[index]'
            tools= [SerperDevTool()],
            verbose=True,
            llm = self.mistral_llm
        )

    @agent
    def website_scrapper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scrapper'],  
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            llm = self.mistral_llm
        )
        
    @agent
    def news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['news_writer'], # type: ignore[index]
            verbose=True,
            llm = self.mistral_llm
        )
        
        
    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'], # type: ignore[index]
            tools=[FileWriterTool()],
            verbose=True,
            llm = self.mistral_llm
        )        

    @task
    def retrive_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrive_news_task'], # type: ignore[index]
        )

    @task
    def website_scrapper_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_scrapper_task'], # type: ignore[index]
            output_file='report.md'
        )
        
    @task
    def news_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_writer_task'], # type: ignore[index]
            output_file='report.md'
        )  
                
    @task
    def file_write_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_write_task'], # type: ignore[index]
            output_file='report.md'
        )      


    @crew
    def crew(self) -> Crew:
        """Creates the AiLatestPoliticalNews crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
