# Claude Code Best Practices - Practical Exercises

## Exercise 1: Setting Up Your Environment (15 minutes)

### Objective
Configure Claude Code with proper context and permissions for a sample project.

### Tasks

#### Task 1.1: Create a CLAUDE.md File
Create a CLAUDE.md file for a hypothetical Node.js project with the following requirements:
- The project uses TypeScript
- Testing is done with Jest
- The project has a PostgreSQL database
- Deployment is via Docker

**Your Task:** Write a comprehensive CLAUDE.md file including:
- [ ] Build and test commands
- [ ] Project structure
- [ ] Coding standards
- [ ] Environment requirements
- [ ] Common troubleshooting tips

#### Task 1.2: Configure Permissions
Create a `.claude/settings.json` file that:
- [ ] Allows npm install and npm test
- [ ] Allows reading all files
- [ ] Allows writing only to src/ and tests/ directories
- [ ] Blocks dangerous commands like rm -rf

#### Task 1.3: Create a Custom Command
Create a slash command called `/lint-fix` that:
- [ ] Runs ESLint with auto-fix
- [ ] Shows which files were modified
- [ ] Runs tests after fixing

**Verification:** 
- Show your CLAUDE.md to a partner
- Explain your permission choices
- Demonstrate your custom command

---

## Exercise 2: Test-Driven Development Workflow (25 minutes)

### Objective
Practice the TDD workflow with Claude Code by building a simple utility function.

### Scenario
You need to create a function that validates email addresses according to your company's specific rules:
- Must contain @ symbol
- Domain must be from approved list: gmail.com, company.com, outlook.com
- No special characters except . and _ before @
- Minimum 3 characters before @

### Tasks

#### Task 2.1: Write the Tests First
Ask Claude to:
```
"Write comprehensive tests for an email validation function with these requirements: [paste requirements above]"
```

#### Task 2.2: Run Tests (Should Fail)
```
"Run the tests to confirm they fail since we haven't implemented the function yet"
```

#### Task 2.3: Implement the Function
```
"Now implement the validateEmail function to pass all tests"
```

#### Task 2.4: Verify Tests Pass
```
"Run the tests again to ensure they all pass"
```

#### Task 2.5: Refactor and Optimize
```
"Review the implementation and suggest improvements for performance or readability"
```

#### Task 2.6: Add Edge Cases
```
"What edge cases are we missing? Add tests for them"
```

**Deliverables:**
- [ ] Test file with comprehensive test cases
- [ ] Implementation that passes all tests
- [ ] Documentation for the function
- [ ] Git commit with appropriate message

---

## Exercise 3: Debugging Challenge (20 minutes)

### Objective
Practice effective debugging communication with Claude Code.

### Scenario
You have a React component that's throwing an error. The component should display user profiles but crashes when certain users are selected.

### The Broken Code
```javascript
// UserProfile.jsx
import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });
  }, [userId]);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="profile">
      <h1>{user.name.first} {user.name.last}</h1>
      <p>Email: {user.email}</p>
      <p>Role: {user.role.title}</p>
      <p>Department: {user.role.department}</p>
      <p>Manager: {user.manager.name}</p>
      <div>
        <h2>Recent Activity</h2>
        {user.activities.map(activity => (
          <div key={activity.id}>
            {activity.description} - {activity.date}
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserProfile;
```

### Error Message
```
TypeError: Cannot read properties of undefined (reading 'first')
  at UserProfile (UserProfile.jsx:18)
```

### Tasks

#### Task 3.1: Identify the Issues
Without running the code, ask Claude:
```
"Review this React component and identify all potential runtime errors"
```

#### Task 3.2: Create Defensive Code
Ask Claude to:
```
"Rewrite this component with proper error handling and defensive programming"
```

#### Task 3.3: Add PropTypes or TypeScript
```
"Add proper type checking to prevent these errors in the future"
```

#### Task 3.4: Write Tests
```
"Write tests that would have caught these bugs"
```

**Expected Learnings:**
- [ ] Identify multiple potential error points
- [ ] Implement proper null checking
- [ ] Add loading and error states
- [ ] Use optional chaining
- [ ] Handle API errors

---

## Exercise 4: Code Review Process (15 minutes)

### Objective
Learn to leverage Claude for comprehensive code reviews.

### The Code to Review
```python
# payment_processor.py
import requests
import json

class PaymentProcessor:
    def __init__(self):
        self.api_key = "sk_live_abc123xyz789"
        self.endpoint = "https://api.payment.com/v1/"
    
    def process_payment(self, amount, card_number, cvv, exp_date):
        # Process the payment
        data = {
            "amount": amount,
            "card": card_number,
            "cvv": cvv,
            "expiry": exp_date
        }
        
        response = requests.post(
            self.endpoint + "charge",
            json=data,
            headers={"Authorization": self.api_key}
        )
        
        if response.status_code == 200:
            return True
        else:
            return False
    
    def refund(self, transaction_id, amount):
        response = requests.post(
            self.endpoint + "refund",
            json={"id": transaction_id, "amount": amount},
            headers={"Authorization": self.api_key}
        )
        return response.json()
    
    def get_balance(self):
        balance = requests.get(self.endpoint + "balance")
        return float(balance.text)
```

### Tasks

#### Task 4.1: Security Review
```
"Review this payment processor code for security vulnerabilities"
```

#### Task 4.2: Best Practices Review
```
"Review this code for Python best practices and PEP 8 compliance"
```

#### Task 4.3: Error Handling Review
```
"Identify missing error handling and suggest improvements"
```

#### Task 4.4: Testing Strategy
```
"Suggest a testing strategy for this payment processor"
```

#### Task 4.5: Refactor
```
"Refactor this code addressing all the issues identified"
```

**Key Issues to Find:**
- [ ] Hardcoded API key (security)
- [ ] No input validation
- [ ] Poor error handling
- [ ] No logging
- [ ] Missing timeout handling
- [ ] No retry logic
- [ ] Type hints missing

---

## Exercise 5: Building with MCP (20 minutes)

### Objective
Create and integrate a simple MCP server with Claude Code.

### Tasks

#### Task 5.1: Design an MCP Server
Design an MCP server that provides these tools:
- `format_date`: Formats dates in various formats
- `calculate_age`: Calculates age from birthdate
- `generate_username`: Creates username from first/last name

#### Task 5.2: Implement the Server
Ask Claude:
```
"Create an MCP server with these three tools: [list tools and requirements]"
```

#### Task 5.3: Configure Integration
Create the `.mcp.json` configuration file

#### Task 5.4: Test the Integration
Use the new tools in a practical scenario

#### Task 5.5: Document Usage
Create documentation for team members on how to use your MCP server

**Deliverables:**
- [ ] Working MCP server code
- [ ] Configuration file
- [ ] Test examples
- [ ] Documentation

---

## Exercise 6: Workflow Automation (15 minutes)

### Objective
Create an automated workflow for a common development task.

### Scenario
Your team frequently needs to:
1. Create a new feature branch
2. Set up boilerplate for a new component
3. Create associated test file
4. Update the index file
5. Create a story file for Storybook

### Tasks

#### Task 6.1: Document the Workflow
Create a CLAUDE.md section documenting this workflow

#### Task 6.2: Create a Slash Command
Create a custom slash command `/new-component` that takes a component name

#### Task 6.3: Implement Automation
Ask Claude to:
```
"Create a script that automates creating a new React component with tests and stories"
```

#### Task 6.4: Test the Workflow
Run through the entire workflow with a sample component

#### Task 6.5: Optimize
Identify and implement improvements to the workflow

**Success Criteria:**
- [ ] Single command creates all necessary files
- [ ] Files follow team conventions
- [ ] Includes proper boilerplate
- [ ] Updates index exports
- [ ] Creates git branch

---

## Exercise 7: Real-World Integration (30 minutes)

### Objective
Integrate Claude Code into an existing project workflow.

### Choose Your Project
Select one of:
1. A personal project
2. An open-source contribution
3. The provided sample project

### Tasks

#### Task 7.1: Project Analysis
```
"Analyze this project structure and suggest Claude Code optimizations"
```

#### Task 7.2: Create Comprehensive CLAUDE.md
Based on the analysis, create a complete CLAUDE.md

#### Task 7.3: Set Up Permissions
Configure appropriate permissions for the project

#### Task 7.4: Implement a Feature
Choose a small feature and implement it using:
- The explore-plan-code-commit workflow
- Proper testing
- Documentation

#### Task 7.5: Create a Pull Request
```
"Create a pull request for this feature with a comprehensive description"
```

**Evaluation Criteria:**
- [ ] CLAUDE.md is comprehensive and accurate
- [ ] Permissions are security-conscious
- [ ] Feature is properly tested
- [ ] Code follows project conventions
- [ ] PR description is complete

---

## Bonus Challenges

### Challenge 1: Performance Optimization
Take a slow function and work with Claude to:
1. Profile the performance issue
2. Identify bottlenecks
3. Implement optimizations
4. Verify improvements

### Challenge 2: Legacy Code Refactoring
Find a piece of legacy code and:
1. Add tests to ensure behavior is preserved
2. Refactor for modern standards
3. Improve documentation
4. Ensure backward compatibility

### Challenge 3: CI/CD Integration
Set up Claude Code friendly CI/CD:
1. Create GitHub Actions workflow
2. Include Claude Code compatible testing
3. Add automation for common tasks
4. Document for team usage

---

## Reflection Questions

After completing the exercises, consider:

1. **Which workflow felt most natural to you? Why?**
   _________________________________________________

2. **What aspects of Claude Code surprised you?**
   _________________________________________________

3. **How would you integrate Claude Code into your daily workflow?**
   _________________________________________________

4. **What custom commands would be useful for your projects?**
   _________________________________________________

5. **What safety concerns do you have and how would you address them?**
   _________________________________________________

---

## Exercise Solutions Checklist

Use this checklist to verify you've completed all exercises:

- [ ] Exercise 1: Environment Setup
  - [ ] CLAUDE.md created
  - [ ] Permissions configured
  - [ ] Custom command working

- [ ] Exercise 2: TDD Workflow
  - [ ] Tests written first
  - [ ] Implementation passes tests
  - [ ] Edge cases covered

- [ ] Exercise 3: Debugging
  - [ ] Issues identified
  - [ ] Defensive code implemented
  - [ ] Tests added

- [ ] Exercise 4: Code Review
  - [ ] Security issues found
  - [ ] Best practices applied
  - [ ] Refactored version complete

- [ ] Exercise 5: MCP Integration
  - [ ] Server implemented
  - [ ] Configuration complete
  - [ ] Documentation written

- [ ] Exercise 6: Workflow Automation
  - [ ] Workflow documented
  - [ ] Automation working
  - [ ] Optimizations applied

- [ ] Exercise 7: Real-World Integration
  - [ ] Project analyzed
  - [ ] Feature implemented
  - [ ] PR created

---

## Additional Resources

### Sample Files
Check the `/examples` folder for:
- Sample CLAUDE.md files
- Example MCP servers
- Custom command templates
- Permission configurations

### Troubleshooting
If you get stuck:
1. Check the error message carefully
2. Verify your configuration files
3. Ask Claude to explain the issue
4. Consult the documentation
5. Ask your instructor

### Next Steps
After completing these exercises:
1. Apply these practices to your own projects
2. Share your custom commands with the team
3. Contribute to the Claude Code community
4. Explore advanced MCP capabilities
5. Create your own exercise scenarios