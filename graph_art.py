#!/usr/bin/env python3
"""
GitHub Contribution Graph ASCII Art Generator

This script creates commits on specific dates to spell out text on your GitHub contribution graph.
For 2025, this will spell out "WASSSUP!" in beautiful green squares!
"""

import datetime
import subprocess
import json
import random
import os
from pathlib import Path


class GitHubGraphArt:
    def __init__(self):
        self.repo_path = Path(".")
        self.data_dir = self.repo_path / "data"
        self.data_dir.mkdir(exist_ok=True)
        
        # GitHub contribution graph is 53 weeks × 7 days
        # Week 0 = leftmost column, Week 52 = rightmost column  
        # Day 0 = Sunday, Day 6 = Saturday
        
        # Define letter patterns (7 rows × variable width)
        # 1 = commit, 0 = no commit
        self.letters = {
            'W': [
                [1,0,0,0,1],
                [1,0,0,0,1], 
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,1,0,1],
                [1,1,0,1,1],
                [1,0,0,0,1]
            ],
            'A': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,1,1,1,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1]
            ],
            'S': [
                [0,1,1,1,1],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [0,1,1,1,0],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [1,1,1,1,0]
            ],
            'U': [
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            'P': [
                [1,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,1,1,1,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0]
            ],
            'H': [
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,1,1,1,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1]
            ],
            'I': [
                [1,1,1,1,1],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0],
                [1,1,1,1,1]
            ],
            'E': [
                [1,1,1,1,1],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,1,1,1,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,1,1,1,1]
            ],
            'L': [
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,1,1,1,1]
            ],
            'O': [
                [0,1,1,1,0],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [1,0,0,0,1],
                [0,1,1,1,0]
            ],
            '!': [
                [1],
                [1],
                [1],
                [1],
                [1],
                [0],
                [1]
            ]
        }
    
    def get_contribution_graph_start_date(self):
        """Get the start date of the GitHub contribution graph (53 weeks ago from today)"""
        # GitHub contribution graph shows the last 53 weeks (371 days)
        today = datetime.date.today()
        
        # Find the Sunday that started 52 weeks ago (GitHub's contribution graph starts on Sunday)
        # Go back 52 weeks (364 days) and find the Sunday of that week
        weeks_ago_52 = today - datetime.timedelta(weeks=52)
        
        # Find the Sunday of that week
        days_since_sunday = weeks_ago_52.weekday() + 1  # Monday = 0, so Sunday = 6, but we want Sunday = 0
        if days_since_sunday == 7:
            days_since_sunday = 0
        
        start_sunday = weeks_ago_52 - datetime.timedelta(days=days_since_sunday)
        return start_sunday
    
    def calculate_commit_dates(self, text, start_week=5):
        """Calculate which dates need commits to spell out the text on current contribution graph"""
        commit_dates = []
        current_week = start_week
        
        for char in text.upper():
            if char == ' ':
                current_week += 2  # Space between words
                continue
            
            if char in self.letters:
                pattern = self.letters[char]
                letter_width = len(pattern[0])
                
                # For each column of the letter
                for col in range(letter_width):
                    # For each row of the letter  
                    for row in range(7):
                        if row < len(pattern) and col < len(pattern[row]) and pattern[row][col] == 1:
                            # Calculate the actual date based on current contribution graph
                            graph_start_date = self.get_contribution_graph_start_date()
                            target_date = graph_start_date + datetime.timedelta(weeks=current_week, days=row)
                            
                            # Only add dates that are in the past (can't commit to future)
                            if target_date <= datetime.date.today():
                                commit_dates.append(target_date)
                    
                    current_week += 1  # Move to next column
                
                current_week += 1  # Space between letters
        
        return sorted(commit_dates)
    
    def create_data_file_for_date(self, date):
        """Create a single lightweight data file (reused and updated)"""
        filename = "contribution_data.json"
        file_path = self.data_dir / filename
        
        # Simple, lightweight data structure
        data = {
            "last_updated": date.isoformat(),
            "contribution_count": random.randint(1, 5),
            "status": "active"
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return str(file_path)
    
    def make_commit_for_date(self, date, custom_message=None):
        """Create a commit for a specific date"""
        # Create/update the single data file
        file_path = self.create_data_file_for_date(date)
        
        # Stage the file
        subprocess.run(["git", "add", file_path], cwd=self.repo_path, check=True)
        
        # Create commit message
        if custom_message:
            commit_msg = custom_message
        else:
            messages = [
                f"Update processing {date.strftime('%m/%d')}",
                f"Data checkpoint {date.strftime('%Y%m%d')}",
                f"System update {date.strftime('%B %d')}",
                "Performance improvements",
                "Code optimization",
                "Bug fixes and updates",
                "Enhancement updates",
                "Maintenance update"
            ]
            commit_msg = random.choice(messages)
        
        # Set the commit date using git's date format
        commit_datetime = datetime.datetime.combine(date, datetime.time(
            hour=random.randint(9, 17),  # Business hours
            minute=random.randint(0, 59)
        ))
        date_str = commit_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        # Create the commit with the specific date
        # GitHub contribution graph uses AUTHOR date, so we need to set both author and commit date
        env = {
            "GIT_AUTHOR_DATE": date_str,
            "GIT_COMMITTER_DATE": date_str
        }
        # Merge environment variables
        full_env = os.environ.copy()
        full_env.update(env)
        
        subprocess.run([
            "git", "commit", "-m", commit_msg
        ], cwd=self.repo_path, check=True, env=full_env)
        
        return True
    
    def create_graph_art(self, text="WASSSUP!", start_week=8, preview_only=False):
        """Create the GitHub graph art"""
        print(f"🎨 Creating GitHub graph art: '{text}' on current contribution graph")
        
        # Calculate all the dates we need
        commit_dates = self.calculate_commit_dates(text, start_week)
        
        if not commit_dates:
            print("❌ No commit dates calculated!")
            return False
        
        print(f"📅 Need to create {len(commit_dates)} commits between {commit_dates[0]} and {commit_dates[-1]}")
        
        if preview_only:
            print("\n📋 Preview of commit dates:")
            for i, date in enumerate(commit_dates):
                print(f"  {i+1:2d}. {date.strftime('%Y-%m-%d (%A)')}")
            return True
        
        # Create commits for each date
        success_count = 0
        for i, date in enumerate(commit_dates):
            try:
                print(f"📝 Creating commit {i+1}/{len(commit_dates)} for {date.strftime('%Y-%m-%d')}...")
                self.make_commit_for_date(date)
                success_count += 1
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to create commit for {date}: {e}")
        
        print(f"\n✅ Successfully created {success_count}/{len(commit_dates)} commits!")
        print(f"🚀 Your '{text}' should appear on your GitHub contribution graph!")
        
        return success_count == len(commit_dates)
    
    def preview_layout(self, text="WASSSUP!", start_week=8):
        """Show a visual preview of how the text will look on the current contribution graph"""
        print(f"🎨 Preview of '{text}' on current GitHub contribution graph:")
        print("   (Each █ represents a day with commits)\n")
        
        # Create a 53x7 grid to simulate the contribution graph
        grid = [['·' for _ in range(53)] for _ in range(7)]
        
        # Fill in the pattern
        commit_dates = self.calculate_commit_dates(text, start_week)
        graph_start_date = self.get_contribution_graph_start_date()
        
        for date in commit_dates:
            days_diff = (date - graph_start_date).days
            week = days_diff // 7
            day_of_week = days_diff % 7
            
            if 0 <= week < 53 and 0 <= day_of_week < 7:
                grid[day_of_week][week] = '█'
        
        # Print the grid
        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i, day in enumerate(days):
            print(f"{day} │{''.join(grid[i])}")
        
        print("    └" + "─" * 53)
        print(f"     Last Year{' ' * 40}Today")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Create GitHub contribution graph ASCII art")
    parser.add_argument("--text", default="WASSSUP!", help="Text to display on graph")
    parser.add_argument("--start-week", type=int, default=8, help="Week to start the text (0-52)")
    parser.add_argument("--preview", action="store_true", help="Preview the layout without creating commits")
    parser.add_argument("--preview-dates", action="store_true", help="Show all commit dates")
    
    args = parser.parse_args()
    
    # Initialize git if needed
    if not Path(".git").exists():
        print("Initializing git repository...")
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "config", "user.name", "Graph Artist"], check=True)
        subprocess.run(["git", "config", "user.email", "artist@github.com"], check=True)
    
    artist = GitHubGraphArt()
    
    if args.preview:
        artist.preview_layout(args.text, args.start_week)
    elif args.preview_dates:
        artist.create_graph_art(args.text, args.start_week, preview_only=True)
    else:
        # Create the actual commits
        success = artist.create_graph_art(args.text, args.start_week)
        
        if success:
            print("\n🎉 Graph art created successfully!")
            print("💡 Don't forget to push to GitHub:")
            print("   git push origin main")
            print(f"\n📊 Your '{args.text}' should be visible on your GitHub profile now!")
        else:
            print("\n❌ Some commits failed. Check the output above for details.")


if __name__ == "__main__":
    main()
