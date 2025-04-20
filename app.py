import openai

class SWOTAnalysisAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def analyze(self, subject):
        prompt = f"""
        Perform a SWOT analysis for the following subject:
        {subject}

        Provide the analysis in the following format:
        Strengths:
        - ...
        Weaknesses:
        - ...
        Opportunities:
        - ...
        Threats:
        - ...
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'your_openai_api_key' with your actual OpenAI API key
    api_key = "your_openai_api_key"
    agent = SWOTAnalysisAgent(api_key)

    subject = input("Enter the subject for SWOT analysis: ")
    analysis = agent.analyze(subject)
    print("\nSWOT Analysis:")
    print(analysis)