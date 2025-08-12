# Claude Code Quick Reference Card

## Essential Commands

### Starting & Stopping
```bash
claude code                  # Start interactive session
claude code --help          # Show help
/exit                       # Exit session (or Ctrl+D)
/help                       # Get help within session
```

### Permissions & Settings
```bash
/permissions                # Manage tool permissions
claude code --allowedTools "Bash:npm install,Read:*"
claude code --dangerously-skip-permissions  # ⚠️ DANGEROUS
```

### MCP & Extensions
```bash
claude code mcp add /path/to/server   # Add MCP server
claude code mcp remove server-name    # Remove MCP server
/[custom-command]                      # Run custom command
```

---

## CLAUDE.md Template

```markdown
# Project Name

## Commands
- Build: npm run build
- Test: npm test
- Lint: npm run lint
- Deploy: npm run deploy

## Project Structure
- /src - Source code
- /tests - Test files
- /docs - Documentation

## Code Style
- TypeScript strict mode
- 2 spaces indentation
- ESLint rules enforced

## Notes
- Use npm, not yarn
- Tests must pass before commit
```

---

## Settings Configuration

### Location: `.claude/settings.json`
```json
{
  "allowedTools": [
    "Bash:npm install",
    "Bash:npm test",
    "Bash:npm run build",
    "Read:*",
    "Write:src/**",
    "Write:tests/**"
  ]
}
```

---

## Effective Prompting

### ❌ Poor Prompts
- "Fix the bug"
- "Make it better"
- "It doesn't work"

### ✅ Good Prompts
- "Fix the login bug in auth.js line 45 where OAuth fails"
- "Optimize the database query in userService.js for better performance"
- "The API returns 404 for GET /users when auth token is valid"

---

## Workflows at a Glance

### 🔍 Explore → Plan → Code → Commit
```
1. "Show me how [feature] works"
2. "Let's plan the implementation"
3. "Implement [specific feature]"
4. "Create a commit"
```

### 🧪 Test-Driven Development
```
1. "Write tests for [feature]"
2. "Run tests" (confirm fail)
3. "Implement [feature]"
4. "Run tests" (confirm pass)
```

### 🎨 Visual Implementation
```
1. "Here's the design" [image]
2. "Implement this UI"
3. "Take a screenshot"
4. "Adjust to match better"
```

---

## Security Best Practices

### ✅ DO
- Whitelist specific commands
- Use project-specific settings
- Review permissions regularly
- Keep API keys in env files
- Document security considerations

### ❌ DON'T
- Use YOLO mode in production
- Store secrets in CLAUDE.md
- Allow unrestricted bash access
- Commit sensitive data
- Skip security reviews

---

## File Patterns

### Permissions Examples
```json
"Read:*"                    // Read all files
"Write:src/**"             // Write to src and subdirs
"Bash:npm run *"           // All npm run commands
"Write:*.test.js"          // Write test files only
"Read:!node_modules/**"    // Read all except node_modules
```

---

## Custom Commands

### Create Command
```bash
echo 'Your prompt template: $ARGUMENTS' > ~/.claude/commands/name
```

### Useful Templates
```bash
# Code review
echo 'Review for bugs and improvements: $ARGUMENTS' > ~/.claude/commands/review

# Generate tests
echo 'Write comprehensive tests for: $ARGUMENTS' > ~/.claude/commands/test

# Document code
echo 'Add JSDoc comments to: $ARGUMENTS' > ~/.claude/commands/document
```

---

## MCP Configuration

### Project: `.mcp.json`
```json
{
  "servers": {
    "my-server": {
      "command": "node",
      "args": ["./mcp-server/index.js"]
    }
  }
}
```

### Global: `~/.claude/mcp.json`
```json
{
  "servers": {
    "global-utils": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

---

## GitHub Integration

```bash
# Setup
gh auth login

# Common Operations
"Create a PR for this feature"
"Show me PR #123 comments"
"Create an issue for this bug"
"Check CI status"
```

---

## Debugging Checklist

When reporting bugs to Claude:
- [ ] Full error message
- [ ] Stack trace
- [ ] Recent changes
- [ ] Environment (dev/prod)
- [ ] Steps to reproduce
- [ ] Expected vs. actual behavior

---

## Performance Tips

### Speed Up Claude Code
1. **Be specific** - Use exact file paths
2. **Batch requests** - Multiple tasks in one prompt
3. **Use search first** - Find before editing
4. **Maintain context** - Keep CLAUDE.md updated
5. **Clear when switching** - Start fresh for new tasks

---

## Common Fixes

| Issue | Solution |
|-------|----------|
| Permission denied | Add to allowedTools |
| Command not found | Check PATH or use full path |
| MCP not connecting | Verify server path |
| Slow responses | Reduce context, be specific |
| Wrong code style | Update CLAUDE.md |

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit session |
| `Tab` | Autocomplete |
| `↑/↓` | Command history |
| `Ctrl+L` | Clear screen |

---

## Task Management

### Using Todo Lists
```
"Create a todo list for implementing user authentication"
"Mark the first task as in progress"
"Mark the current task as completed"
"Add a new task for error handling"
```

---

## Testing Patterns

```bash
# Run all tests
"Run the test suite"

# Run specific tests
"Run tests for userService"

# Test coverage
"Check test coverage and identify gaps"

# Add tests
"Add tests for the new validation logic"
```

---

## Code Review Checklist

Ask Claude to review for:
- [ ] Security vulnerabilities
- [ ] Performance bottlenecks
- [ ] Error handling
- [ ] Code style consistency
- [ ] Test coverage
- [ ] Documentation completeness
- [ ] Best practices
- [ ] Potential bugs

---

## Emergency Commands

```bash
# Stop runaway process
Ctrl+C

# Exit immediately
/exit or Ctrl+D

# Reset permissions
rm ~/.claude/settings.json

# Check Claude status
claude code --version

# Get help
/help or claude code --help
```

---

## Links & Resources

**Documentation**
- https://docs.anthropic.com/claude-code

**Support**
- GitHub Issues: Report bugs
- Discord: Community help

**Learning**
- Best practices blog
- Video tutorials
- Example projects

---

## Notes Space

```
_________________________
_________________________
_________________________
_________________________
_________________________
```

---

*Keep this card handy during development!*

**Version 1.0 | Claude Code Best Practices**