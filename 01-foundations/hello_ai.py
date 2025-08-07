#!/usr/bin/env python3
"""
My First AI Learning Program
Week 1 - Day 1: Hello AI World!
"""

import datetime
import sys

def main():
    """
    My first program in the AI learning journey!
    """
    print("🤖 Hello AI World! 🤖")
    print("=" * 50)
    print(f"📅 Started learning on: {datetime.date.today()}")
    print(f"🐍 Python version: {sys.version}")
    print("=" * 50)
    
    # Simple AI-related calculation
    print("\n🧠 Let's do some 'AI' math:")
    numbers = [1, 2, 3, 4, 5]
    mean = sum(numbers) / len(numbers)
    print(f"📊 Average of {numbers} = {mean}")
    
    # Goal setting
    print("\n🎯 My AI Learning Goals:")
    goals = [
        "Build my first chatbot",
        "Create an AI agent",
        "Deploy a project to the cloud",
        "Understand machine learning basics",
        "Complete 8-week learning plan"
    ]
    
    for i, goal in enumerate(goals, 1):
        print(f"   {i}. {goal}")
    
    print("\n🚀 Let's start this AI journey!")
    print("💪 Week 1: Environment Setup - COMPLETE!")

if __name__ == "__main__":
    main()
