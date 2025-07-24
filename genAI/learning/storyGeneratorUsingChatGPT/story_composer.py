import os
import sys
import time
from enum import Enum

import openai
from openai import OpenAI

class composer_utils:

    @staticmethod
    def display_text(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Move to the next line after the message is printed

# Initialize OpenAI client (requires `OPENAI_API_KEY` set as environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(messages, temperature=0.8, model="gpt-4.1-nano"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=700,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

class story_composer():

    def __init__(self, writer):
        self.writer = writer

    def get_initial_inputs(self):
        print(f"=== Storyline Generator. Let's write a story together, {self.writer} !! ===")
        genre = input("Enter genre (e.g., sci-fi, romance, thriller): ")
        setting = input("Enter setting (e.g., post-apocalyptic Earth, medieval kingdom): ")
        characters = input("Enter main characters (e.g., a rogue AI, a lonely prince): ")
        theme = input("Enter theme (e.g., redemption, revenge, love conquers all): ")
        return genre, setting, characters, theme

    def compose_story(self, messages):
        print("\n--- Scene 1: Opening Scene ---\n")
        scene = chat_with_gpt(messages)
        print(scene)
        story = list()

        scene_counter = 2
        while True:
            print("\n=== What do you want to do next? ===")
            print("1. Continue with next scene")
            print("2. Write closing scene and end story")
            print("3. Exit without finishing")

            choice = input("Enter your choice (1/2/3): ").strip()
            if choice == "1":
                direction = input("Optional: Enter a direction for the next scene (or press enter to skip): ").strip()
                prompt = f"Write scene {scene_counter} of the story. "
                if direction:
                    prompt += f"Direction: {direction}.\n"
                else:
                    prompt += "Continue the story naturally from the last scene.\n"

                messages.append({"role": "user", "content": prompt})
                scene = chat_with_gpt(messages)
                print(f"\n--- Scene {scene_counter} ---\n")
                print(scene)
                story.append(scene)
                messages.append({"role": "assistant", "content": scene})
                scene_counter += 1

            elif choice == "2":
                messages.append({"role": "user",
                                 "content": "Write the final closing scene that wraps up the story emotionally and logically."})
                closing_scene = chat_with_gpt(messages)
                print("\n--- Final Scene: Closing ---\n")
                print(closing_scene)
                story.append(closing_scene)
                break

            elif choice == "3":
                print("Exiting. Hope you enjoyed your story!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        return story


if __name__ == "__main__":

    # get story type
    name_of_writer = input("Hello There.. ! What's your name : ")
    composer = story_composer(name_of_writer)
    genre, setting, characters, theme = composer.get_initial_inputs()

    # Base prompt to start story
    messages = [
        {"role": "system", "content": "You are a creative storyteller assistant."},
        {"role": "user", "content": f"""Write the opening scene of a {genre} story.
    Setting: {setting}
    Characters: {characters}
    Theme: {theme}

    Include atmosphere, character actions, and a hint of the conflict.
    """}]

    story = composer.compose_story(messages)
    filename = input("Write your story to a file now, give it a name : ")
    file = open(filename, "w")
    for scene in story:
        file.write(scene)
        file.write("\n")
        file.flush()

    print("File saved, verify !")