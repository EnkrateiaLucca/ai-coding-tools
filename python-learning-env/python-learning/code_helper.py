"""
Python Learning Assistant using Claude API

A specialized educational assistant for learning Python programming.
Provides code examples with detailed explanations and comments.
"""

import anthropic
import os
from typing import Optional


class PythonLearningAssistant:
    """
    Educational assistant for learning Python programming.
    
    This class provides a wrapper around Claude's API with specialized prompts
    designed for Python education, offering explanations, code examples, and
    learning guidance.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Python Learning Assistant.
        
        Args:
            api_key: Anthropic API key. If None, will try to get from environment
        """
        # Get API key from parameter or environment
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "Anthropic API key is required. Either pass it as a parameter "
                "or set the ANTHROPIC_API_KEY environment variable."
            )
        
        # Initialize the Anthropic client
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
        # Educational prompt template for Python learning
        self.system_prompt = """
You are an expert Python programming tutor and educational assistant. Your role is to help students learn Python through clear explanations, well-commented code examples, and educational guidance.

Key principles:
1. EDUCATIONAL FOCUS: Always explain concepts, don't just provide code
2. DETAILED COMMENTS: Include comprehensive comments in all code examples
3. STEP-BY-STEP: Break down complex concepts into digestible steps
4. BEST PRACTICES: Demonstrate proper Python conventions and practices
5. MULTIPLE EXAMPLES: Provide various examples when helpful
6. ENCOURAGE LEARNING: Ask follow-up questions to deepen understanding

When responding:
- Start with a brief explanation of the concept
- Provide well-commented code examples
- Explain how the code works line by line when appropriate
- Mention common pitfalls and best practices
- Suggest related concepts to explore
- Encourage experimentation and practice

Format your responses clearly with:
- Brief conceptual explanation
- Code examples with extensive comments
- Step-by-step breakdown
- Tips and best practices
- Suggestions for further learning

Remember: You're not just coding, you're teaching!
"""
    
    def ask(self, question: str, context: str = "") -> str:
        """
        Ask the Python Learning Assistant a question.
        
        Args:
            question: Your Python-related question
            context: Optional context about what you're working on
            
        Returns:
            Educational response with explanations and code examples
        """
        try:
            # Construct the user message
            user_message = f"""
Python Learning Question: {question}

{f"Context: {context}" if context else ""}

Please provide an educational response with:
1. Clear explanation of the concept
2. Well-commented code examples
3. Step-by-step breakdown
4. Best practices and tips
5. Suggestions for further learning
"""
            
            # Make the API call
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                temperature=0.7,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"Error communicating with Claude API: {str(e)}"
    
    def explain_code(self, code: str, specific_question: str = "") -> str:
        """
        Get explanation for existing code.
        
        Args:
            code: The Python code to explain
            specific_question: Optional specific question about the code
            
        Returns:
            Detailed explanation of the code
        """
        question = f"""
Please explain this Python code:

```python
{code}
```

{f"Specific question: {specific_question}" if specific_question else ""}

Please provide:
1. Overview of what the code does
2. Line-by-line explanation
3. Key concepts being used
4. Potential improvements or best practices
5. Related concepts to learn
"""
        return self.ask(question)
    
    def debug_help(self, code: str, error_message: str = "", issue_description: str = "") -> str:
        """
        Get help debugging Python code.
        
        Args:
            code: The problematic Python code
            error_message: Any error message received
            issue_description: Description of the issue
            
        Returns:
            Educational debugging assistance
        """
        question = f"""
I need help debugging this Python code:

```python
{code}
```

{f"Error message: {error_message}" if error_message else ""}
{f"Issue description: {issue_description}" if issue_description else ""}

Please help me understand:
1. What's going wrong and why
2. How to fix it with explained solutions
3. Best practices to avoid similar issues
4. Learning opportunities from this debugging experience
"""
        return self.ask(question)
    
    def concept_tutorial(self, concept: str, level: str = "beginner") -> str:
        """
        Get a tutorial on a specific Python concept.
        
        Args:
            concept: The Python concept to learn about
            level: Learning level (beginner, intermediate, advanced)
            
        Returns:
            Comprehensive tutorial on the concept
        """
        question = f"""
I want to learn about: {concept}

My level: {level}

Please provide a comprehensive tutorial that includes:
1. What this concept is and why it's important
2. Basic syntax and usage
3. Multiple practical examples with detailed comments
4. Common use cases and applications
5. Best practices and common pitfalls
6. Exercises or challenges to practice
7. What to learn next after mastering this concept
"""
        return self.ask(question)
    
    def practice_problems(self, topic: str, difficulty: str = "beginner") -> str:
        """
        Get practice problems for a specific topic.
        
        Args:
            topic: The Python topic to practice
            difficulty: Difficulty level (beginner, intermediate, advanced)
            
        Returns:
            Practice problems with solutions and explanations
        """
        question = f"""
Generate practice problems for: {topic}
Difficulty level: {difficulty}

Please provide:
1. 3-5 practice problems of increasing difficulty
2. Clear problem descriptions
3. Example inputs and expected outputs
4. Hints for solving each problem
5. Complete solutions with detailed explanations
6. Alternative approaches where applicable
"""
        return self.ask(question)


# Convenience functions for quick access
def quick_ask(question: str, context: str = "") -> str:
    """
    Quick function to ask a Python question without creating an instance.
    
    Args:
        question: Your Python question
        context: Optional context
        
    Returns:
        Educational response
    """
    assistant = PythonLearningAssistant()
    return assistant.ask(question, context)


def explain(code: str, question: str = "") -> str:
    """
    Quick function to explain Python code.
    
    Args:
        code: Python code to explain
        question: Optional specific question
        
    Returns:
        Code explanation
    """
    assistant = PythonLearningAssistant()
    return assistant.explain_code(code, question)


def debug(code: str, error: str = "", issue: str = "") -> str:
    """
    Quick function to get debugging help.
    
    Args:
        code: Problematic code
        error: Error message
        issue: Issue description
        
    Returns:
        Debugging assistance
    """
    assistant = PythonLearningAssistant()
    return assistant.debug_help(code, error, issue)


def learn(concept: str, level: str = "beginner") -> str:
    """
    Quick function to learn a Python concept.
    
    Args:
        concept: Concept to learn
        level: Learning level
        
    Returns:
        Concept tutorial
    """
    assistant = PythonLearningAssistant()
    return assistant.concept_tutorial(concept, level)


def practice(topic: str, difficulty: str = "beginner") -> str:
    """
    Quick function to get practice problems.
    
    Args:
        topic: Topic to practice
        difficulty: Difficulty level
        
    Returns:
        Practice problems with solutions
    """
    assistant = PythonLearningAssistant()
    return assistant.practice_problems(topic, difficulty)


# Example usage and setup instructions
if __name__ == "__main__":
    print("""
Python Learning Assistant - Setup Instructions:

1. Install the anthropic package:
   pip install anthropic

2. Set your API key as an environment variable:
   export ANTHROPIC_API_KEY="your_api_key_here"
   
   Or in a Jupyter notebook:
   import os
   os.environ['ANTHROPIC_API_KEY'] = 'your_api_key_here'

3. Import and use in your Jupyter notebook:
   from code_helper import PythonLearningAssistant, quick_ask, explain, learn
   
   # Create an assistant
   assistant = PythonLearningAssistant()
   
   # Ask questions
   response = assistant.ask("How do list comprehensions work?")
   print(response)
   
   # Or use convenience functions
   explanation = explain("numbers = [x**2 for x in range(10)]")
   print(explanation)
   
   tutorial = learn("decorators", "intermediate")
   print(tutorial)

Example usage:
- assistant.ask("How do I iterate through a dictionary?")
- assistant.explain_code("def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)")
- assistant.debug_help("my_list = [1,2,3]; print(my_list[5])", "IndexError: list index out of range")
- assistant.concept_tutorial("lambda functions", "beginner")
- assistant.practice_problems("loops", "intermediate")
""")