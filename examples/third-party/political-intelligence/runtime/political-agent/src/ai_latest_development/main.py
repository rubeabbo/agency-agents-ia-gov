#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

# IA-Gov modification 2026-10-17: package import and explicit CLI entrypoint.
from .crew import AiLatestPoliticalNews
import argparse

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', default='political news')
    args = parser.parse_args()
    inputs = {
        'topic': args.topic,
        'date': str(datetime.now().date()),
        'current_year': str(datetime.now().year)
       
    }
    
    try:
        AiLatestPoliticalNews().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
