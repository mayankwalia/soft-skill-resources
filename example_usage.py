#!/usr/bin/env python3
"""
Example script demonstrating how to work with the soft skills guide CSV.
This script shows how to:
1. Load and parse the CSV
2. Display skills by category
3. Generate a personalized learning plan
4. Export specific skills or activities
"""

import csv
import random
from typing import List, Dict

def load_skills_guide(filepath: str = 'soft-skills-guide-30-60-days.csv') -> List[Dict[str, str]]:
    """Load the soft skills guide from CSV file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def display_all_skills(skills: List[Dict[str, str]]) -> None:
    """Display all available skills with descriptions."""
    print("=" * 80)
    print("AVAILABLE SOFT SKILLS")
    print("=" * 80)
    for i, skill in enumerate(skills, 1):
        print(f"\n{i}. {skill['Skill'].upper()}")
        print(f"   {skill['Description']}")
    print("\n" + "=" * 80)

def display_skill_detail(skill: Dict[str, str]) -> None:
    """Display detailed information about a specific skill."""
    print("\n" + "=" * 80)
    print(f"SKILL: {skill['Skill'].upper()}")
    print("=" * 80)
    print(f"\nDescription:\n{skill['Description']}\n")
    print(f"Activities:\n{skill['Activities']}\n")
    print(f"Reflection:\n{skill['Reflection']}\n")
    print("Resources:")
    print(f"  📚 Book: {skill['Book']}")
    print(f"  🎥 Video: {skill['Video']}")
    print(f"  🎙️  Podcast: {skill['Podcast']}")
    print(f"  🎓 Course: {skill['Course']}")
    print("=" * 80)

def generate_30_day_plan(skills: List[Dict[str, str]], focus_areas: List[str] = None) -> None:
    """Generate a 30-day learning plan."""
    print("\n" + "=" * 80)
    print("30-DAY SOFT SKILLS DEVELOPMENT PLAN")
    print("=" * 80)
    
    if focus_areas:
        selected_skills = [s for s in skills if s['Skill'] in focus_areas]
    else:
        # Select 5 random skills for 30-day plan
        selected_skills = random.sample(skills, min(5, len(skills)))
    
    weeks_per_skill = 30 // len(selected_skills)
    
    for i, skill in enumerate(selected_skills, 1):
        start_day = (i - 1) * weeks_per_skill + 1
        end_day = start_day + weeks_per_skill - 1
        print(f"\nWeek {i} (Days {start_day}-{end_day}): {skill['Skill']}")
        print(f"   Focus: {skill['Description'][:80]}...")
        print(f"   Activities: Complete 2-3 activities from the list")
        print(f"   Resources: Read/watch 1-2 resources")
        print(f"   Reflection: Answer the reflection question at week end")
    
    print("\n" + "=" * 80)

def export_skill_summary(skills: List[Dict[str, str]], output_file: str = 'skills_summary.txt') -> None:
    """Export a summary of all skills to a text file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("SOFT SKILLS GUIDE - SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        
        for skill in skills:
            f.write(f"SKILL: {skill['Skill']}\n")
            f.write(f"{'-' * 80}\n")
            f.write(f"{skill['Description']}\n\n")
            f.write(f"Key Resources:\n")
            f.write(f"  Book: {skill['Book'].split(' - ')[0] if ' - ' in skill['Book'] else skill['Book']}\n")
            f.write(f"  Video: {skill['Video'].split(' - ')[0] if ' - ' in skill['Video'] else skill['Video']}\n\n")
    
    print(f"\n✓ Summary exported to {output_file}")

def main():
    """Main function demonstrating usage examples."""
    # Load the skills guide
    skills = load_skills_guide()
    
    print("\n🎯 SOFT SKILLS GUIDE - INTERACTIVE EXAMPLES")
    
    # Example 1: Display all skills
    display_all_skills(skills)
    
    # Example 2: Display detail for first skill
    print("\n\nExample: Detailed view of first skill")
    display_skill_detail(skills[0])
    
    # Example 3: Generate a 30-day plan
    print("\n\nExample: Generated 30-day plan")
    generate_30_day_plan(skills)
    
    # Example 4: Generate plan focused on specific areas
    print("\n\nExample: Focused plan on leadership and communication")
    focus = ['Strategic Communication', 'Adaptive Leadership', 'Emotional Intelligence']
    generate_30_day_plan(skills, focus)
    
    # Example 5: Export summary
    export_skill_summary(skills)
    
    print("\n\n✅ All examples completed successfully!")

if __name__ == '__main__':
    main()
