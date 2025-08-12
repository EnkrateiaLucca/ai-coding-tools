# Claude Code Best Practices - Instructor Guide

## Course Overview

**Duration:** 2 hours (with optional 30-minute extension for advanced topics)
**Target Audience:** Developers with basic CLI experience
**Prerequisites:** Node.js installed, basic Git knowledge, text editor

### Learning Objectives
By the end of this workshop, students will be able to:
1. Configure Claude Code for optimal productivity
2. Create and maintain CLAUDE.md files
3. Implement secure permission strategies
4. Apply effective development workflows
5. Extend Claude's capabilities with MCP and custom commands
6. Debug and review code effectively with Claude

---

## Pre-Workshop Setup (Send 24 hours before)

### Email Template
```
Subject: Claude Code Workshop - Setup Instructions

Please complete these steps before the workshop:

1. Install Claude Code:
   npm install -g @anthropic/claude-code

2. Install GitHub CLI (optional but recommended):
   - Mac: brew install gh
   - Linux: sudo apt install gh
   - Windows: winget install GitHub.cli

3. Create a test project directory:
   mkdir claude-workshop
   cd claude-workshop
   npm init -y

4. Verify installation:
   claude code --version

If you encounter issues, we'll address them in the first 10 minutes of the workshop.

See you tomorrow!
```

---

## Session Timeline

### Introduction (10 minutes)
- **5 min:** Welcome, introductions, agenda
- **3 min:** Verify installations, troubleshoot issues
- **2 min:** Set expectations and learning goals

### Module 1: Customizing Your Setup (20 minutes)
- **8 min:** CLAUDE.md concept and importance
- **7 min:** Live demo - creating effective CLAUDE.md
- **5 min:** Permissions and security discussion

### Module 2: Extending Capabilities (20 minutes)
- **7 min:** MCP servers explanation
- **8 min:** Custom commands demonstration
- **5 min:** Integration with existing tools

### Module 3: Effective Workflows (30 minutes)
- **10 min:** Explore-Plan-Code-Commit workflow
- **10 min:** TDD with Claude demonstration
- **5 min:** Visual implementation workflow
- **5 min:** Debugging strategies

### Module 4: Hands-On Practice (30 minutes)
- **5 min:** Exercise introduction and pairing
- **20 min:** Guided exercises (rotate between groups)
- **5 min:** Share discoveries and challenges

### Wrap-Up (10 minutes)
- **5 min:** Key takeaways recap
- **3 min:** Resources and next steps
- **2 min:** Q&A and feedback

---

## Teaching Notes by Module

### Module 1: Customizing Your Setup

#### Key Points to Emphasize
- CLAUDE.md is like a team member's onboarding document
- Global vs. project-specific configuration
- Security is paramount - demonstrate bad permission examples

#### Live Demo Script
```bash
# Create a sample project
mkdir demo-project && cd demo-project
npm init -y

# Create CLAUDE.md
cat > CLAUDE.md << 'EOF'
# Demo Project

## Commands
- Build: npm run build
- Test: npm test

## Code Style
- Use 2 spaces for indentation
- Prefer const over let
EOF

# Show how Claude uses this context
claude code
# "What commands are available in this project?"
# Claude should reference the CLAUDE.md content
```

#### Common Student Questions
- **Q: "Can CLAUDE.md contain secrets?"**
  A: Never put secrets directly. Reference where they're stored instead.

- **Q: "How detailed should CLAUDE.md be?"**
  A: Enough detail to work independently, but concise enough to be maintainable.

### Module 2: Extending Capabilities

#### MCP Demo Setup
Have a simple MCP server ready:
```javascript
// simple-mcp-server.js
const { Server } = require('@modelcontextprotocol/sdk');

// ... minimal working example
```

#### Custom Commands Examples
Show progression from simple to complex:
1. Simple: `/greeting` - just returns text
2. Medium: `/review` - takes arguments
3. Complex: `/deploy` - multi-step process

#### Troubleshooting Tips
- MCP connection issues: Check Node.js version
- Command not found: Verify file permissions
- Path issues: Use absolute paths initially

### Module 3: Effective Workflows

#### Workflow Demonstrations

##### Demo 1: TDD Workflow
```
Step 1: "Write tests for a function that calculates fibonacci numbers"
Step 2: "Run the tests" (show them fail)
Step 3: "Implement the fibonacci function"
Step 4: "Run tests again" (show them pass)
Step 5: "Optimize the implementation"
```

##### Demo 2: Debugging Session
Prepare a buggy code sample:
```javascript
// Intentionally buggy code
function processUsers(users) {
  return users.map(u => {
    return {
      name: u.firstName + ' ' + u.lastName,
      age: calculateAge(u.birthdate),
      email: u.contact.email // This will fail if contact is undefined
    }
  });
}
```

Show how to communicate the error effectively to Claude.

#### Workflow Comparison Table
| Workflow | Best For | Time Investment | Learning Curve |
|----------|----------|-----------------|----------------|
| Explore-Plan-Code | New features | Medium | Low |
| TDD | Critical logic | High | Medium |
| Visual Implementation | UI work | Low | Low |
| Debug-Fix-Test | Bug fixes | Low | Low |

### Module 4: Hands-On Practice

#### Exercise Facilitation Tips

##### For Exercise 1 (Environment Setup)
- Walk around and check CLAUDE.md files
- Share good examples on screen
- Point out security issues privately

##### For Exercise 2 (TDD)
- Pair students if possible
- Have solution ready but don't show immediately
- Encourage test creativity

##### For Exercise 3 (Debugging)
- Let students struggle briefly (productive struggle)
- Give hints about defensive programming
- Discuss real-world implications

#### Group Management
- Create diverse pairs (experience levels)
- Rotate between groups every 5 minutes
- Have advanced exercises ready for fast finishers

---

## Common Issues and Solutions

### Technical Issues

| Issue | Solution | Prevention |
|-------|----------|------------|
| Claude Code won't start | Check Node.js version, reinstall | Verify in pre-workshop email |
| Permission denied errors | Check file permissions, use sudo carefully | Demo proper permission setup |
| MCP server connection fails | Verify path, check server logs | Test MCP setup before workshop |
| Git integration issues | Ensure git is configured, check credentials | Include git setup in prerequisites |

### Conceptual Misunderstandings

| Misunderstanding | Clarification | Example |
|------------------|---------------|---------|
| "Claude Code replaces developers" | It's a tool, not a replacement | Show complex decision-making scenarios |
| "More permissions = better" | Security first, convenience second | Demo security breach scenario |
| "CLAUDE.md needs everything" | Focus on what's unique/important | Show minimal vs. bloated examples |
| "Claude knows my codebase" | It only knows what you show it | Demonstrate context limitations |

---

## Assessment Strategies

### Formative Assessment (During Workshop)
- **Observation Checklist:**
  - [ ] Student creates functional CLAUDE.md
  - [ ] Appropriate permissions configured
  - [ ] Successfully completes one workflow
  - [ ] Asks clarifying questions

### Summative Assessment (End of Workshop)
- **Quick Quiz (Optional):**
  1. When should you use YOLO mode? (Never in production)
  2. Where can CLAUDE.md files be placed? (Project root, ~/.claude/)
  3. Name two ways to extend Claude's capabilities (MCP, custom commands)

### Success Indicators
- Students actively experimenting during exercises
- Questions shift from "how" to "what if"
- Students help each other troubleshoot
- Excitement about applying to their projects

---

## Advanced Topics (Optional Extension)

### If Time Permits or for Advanced Groups

#### Topic 1: CI/CD Integration (10 min)
- GitHub Actions with Claude Code
- Automated testing workflows
- Security considerations

#### Topic 2: Team Collaboration (10 min)
- Shared CLAUDE.md best practices
- Version controlling configurations
- Code review workflows

#### Topic 3: Performance Optimization (10 min)
- Large codebase strategies
- Context management
- Efficient prompting

---

## Resources for Instructors

### Preparation Checklist
- [ ] Test all demos on workshop machine
- [ ] Prepare backup slides for technical issues
- [ ] Have offline documentation ready
- [ ] Create sample repositories
- [ ] Test MCP server examples
- [ ] Prepare exercise solutions

### Useful Commands for Demos
```bash
# Quick setup for new demo
alias demo-reset='rm -rf demo-project && mkdir demo-project && cd demo-project && npm init -y'

# Show Claude Code version
claude code --version

# Quick permission reset
rm ~/.claude/settings.json

# MCP server test
node test-mcp-server.js
```

### Emergency Backup Plans

#### If Claude Code service is down:
- Focus on configuration and planning
- Use recorded demonstrations
- Practice workflow planning on paper

#### If majority have installation issues:
- Pair programming on working machines
- Focus on concepts and demonstrations
- Provide detailed follow-up instructions

---

## Post-Workshop Follow-Up

### Email Template (Send within 24 hours)
```
Subject: Claude Code Workshop - Resources and Next Steps

Thank you for attending today's workshop! Here are your resources:

1. Slides and materials: [link]
2. Exercise solutions: [link]
3. Recording (if available): [link]

Next Steps:
1. Apply CLAUDE.md to one of your projects
2. Create 3 custom commands for your workflow
3. Try the TDD workflow on a real feature

Join our community:
- Discord: [link]
- GitHub Discussions: [link]

Questions? Reply to this email or reach out in Discord.

Happy coding!
```

### Success Metrics
Track these for workshop improvement:
- Attendance vs. registration rate
- Exercise completion rate
- Post-workshop survey scores
- Follow-up questions received
- Community engagement

---

## Speaking Points for Key Concepts

### On Security
"Think of permissions like giving someone keys to your house. You wouldn't give everyone a master key - you'd give specific access. The mailman gets the mailbox key, the dog walker gets the front door key during specific hours."

### On CLAUDE.md
"CLAUDE.md is like writing a guide for a talented but new team member. You want to give them enough context to be productive without overwhelming them with every detail."

### On Workflows
"These workflows aren't rigid rules - they're starting points. Like cooking recipes, once you understand the basics, you can adjust to taste."

### On MCP
"MCP servers are like plugins for Claude Code. Just as VS Code has extensions, Claude Code can be extended with MCP servers to add specialized capabilities."

---

## Instructor's Quick Reference

### Key Commands
```bash
claude code                    # Start session
claude code --help            # Show help
/permissions                  # Manage permissions
/exit                        # Exit session
claude code mcp add [path]   # Add MCP server
```

### Time Management Tips
- Use a visible timer
- Give 2-minute warnings
- Have students share screens for demos
- Keep exercises focused
- Save Q&A for dedicated time

### Energy Management
- Stand and stretch after Module 2
- Pair exercises promote engagement
- Use humor appropriately
- Celebrate small wins
- Keep pace dynamic

---

## Feedback Collection

### Quick Feedback (Last 2 minutes)
"On a sticky note, write:
1. One thing you'll use tomorrow
2. One thing you want to learn more about"

### Detailed Feedback (Online form)
1. What was most valuable?
2. What was least clear?
3. What would you add/remove?
4. Would you recommend this workshop?
5. What follow-up topics interest you?

---

## Notes Section

Space for instructor observations and improvements:

```
Session Date: ___________
Attendance: ___________
Overall Energy: Low | Medium | High
Technical Issues: _____________________
____________________________________
____________________________________

What worked well:
____________________________________
____________________________________

What to improve:
____________________________________
____________________________________

Follow-up needed:
____________________________________
____________________________________
```