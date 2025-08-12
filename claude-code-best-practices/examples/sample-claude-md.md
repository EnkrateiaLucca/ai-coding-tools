# Example CLAUDE.md Files

## Example 1: Node.js/TypeScript Project

```markdown
# E-Commerce Platform

## Quick Commands
- `npm run dev` - Start development server (port 3000)
- `npm run build` - Build for production
- `npm run test` - Run test suite
- `npm run test:watch` - Run tests in watch mode
- `npm run lint` - Run ESLint
- `npm run typecheck` - Run TypeScript compiler check
- `npm run migrate` - Run database migrations
- `npm run seed` - Seed database with test data

## Project Structure
```
/src
  /api         - REST API endpoints
  /services    - Business logic layer
  /models      - Database models (Prisma)
  /utils       - Utility functions
  /middleware  - Express middleware
  /types       - TypeScript type definitions
/tests
  /unit        - Unit tests
  /integration - Integration tests
  /e2e         - End-to-end tests
/prisma        - Database schema and migrations
/public        - Static assets
```

## Tech Stack
- Node.js 18+
- TypeScript 5.0
- Express.js
- Prisma ORM
- PostgreSQL
- Redis for caching
- Jest for testing

## Code Style
- Use TypeScript strict mode
- Prefer async/await over promises
- Use named exports
- 2 spaces indentation
- Semicolons required
- Single quotes for strings
- File names: kebab-case
- Component names: PascalCase

## Database
- PostgreSQL 14+ required
- Connection string in DATABASE_URL env var
- Run migrations before starting: `npm run migrate`
- Test database: append `_test` to database name

## Testing Guidelines
- Write tests for all new features
- Aim for 80% coverage minimum
- Use describe/it blocks
- Mock external services
- Test file naming: `*.test.ts`

## Environment Variables
Required variables (see .env.example):
- DATABASE_URL
- REDIS_URL
- JWT_SECRET
- STRIPE_API_KEY
- SENDGRID_API_KEY
- AWS_S3_BUCKET

## Common Issues
- Port 3000 in use: Check for other running servers
- Database connection failed: Ensure PostgreSQL is running
- Redis connection failed: Start Redis with `redis-server`
- TypeScript errors: Run `npm run typecheck` to see all errors

## Git Workflow
- Main branch: `main` (protected)
- Feature branches: `feature/description`
- Commit style: Conventional Commits
- PRs require: passing tests, code review, no conflicts

## Deployment
- Staging: Automatically deployed from `develop` branch
- Production: Manually deployed from `main` branch
- Use `npm run build` before deployment
- Environment variables set in CI/CD

## Useful Snippets
Test a specific endpoint:
`curl -X POST http://localhost:3000/api/users -H "Content-Type: application/json" -d '{"email":"test@example.com"}'`

Check database connection:
`npm run db:status`

## Team Conventions
- API responses follow JSend format
- All dates in ISO 8601 format
- Pagination uses cursor-based approach
- File uploads go to S3
- Background jobs use Bull queue
```

---

## Example 2: React/Next.js Project

```markdown
# Marketing Website

## Commands
- `npm run dev` - Start Next.js dev server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Lint code
- `npm run format` - Format with Prettier
- `npm run storybook` - Start Storybook
- `npm run test` - Run tests
- `npm run e2e` - Run Playwright tests

## Project Structure
```
/app           - Next.js 13+ app directory
  /(marketing) - Marketing pages
  /(app)       - Application pages
  /api         - API routes
/components    - Reusable components
  /ui          - Base UI components
  /features    - Feature-specific components
/lib           - Utility functions and configs
/hooks         - Custom React hooks
/styles        - Global styles and themes
/public        - Static assets
```

## Stack
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Radix UI components
- React Hook Form
- Zustand for state
- SWR for data fetching

## Component Guidelines
- Use function components
- Props interface named `[Component]Props`
- Export from index.ts files
- Colocate styles, tests, stories
- Use composition over inheritance

## Styling
- Tailwind CSS for styling
- CSS Modules for complex components
- Theme colors in tailwind.config.js
- Mobile-first responsive design
- Dark mode support via `dark:` prefix

## State Management
- Server state: SWR or React Query
- Client state: Zustand stores
- Form state: React Hook Form
- URL state: Next.js router

## Performance
- Use dynamic imports for large components
- Implement React.lazy for code splitting
- Optimize images with next/image
- Use static generation where possible
- Monitor with Web Vitals

## Testing
- Unit tests: Jest + React Testing Library
- Integration: Mock Service Worker (MSW)
- E2E: Playwright
- Visual regression: Chromatic

## A11y Requirements
- WCAG 2.1 AA compliance
- Semantic HTML
- ARIA labels where needed
- Keyboard navigation support
- Screen reader tested

## SEO
- Meta tags in layout.tsx
- Structured data (JSON-LD)
- Sitemap at /sitemap.xml
- Robots.txt configured
- Open Graph tags

## Common Patterns
Loading state:
```tsx
if (loading) return <Skeleton />
if (error) return <ErrorBoundary />
return <Component data={data} />
```

## Deployment
- Vercel for hosting
- Preview deployments for PRs
- Production: main branch
- Environment variables in Vercel dashboard
```

---

## Example 3: Python/FastAPI Project

```markdown
# ML API Service

## Commands
- `make dev` - Start development server
- `make test` - Run tests
- `make lint` - Run linting (ruff)
- `make format` - Format code (black)
- `make migrate` - Run Alembic migrations
- `make shell` - Start IPython shell
- `make docker-up` - Start Docker services
- `make clean` - Clean cache files

## Project Structure
```
/app
  /api         - FastAPI routes
    /v1        - API version 1
  /core        - Core configuration
  /models      - SQLAlchemy models
  /schemas     - Pydantic schemas
  /services    - Business logic
  /ml          - Machine learning models
  /utils       - Utility functions
/tests
  /unit        - Unit tests
  /integration - Integration tests
/alembic       - Database migrations
/scripts       - Utility scripts
/notebooks     - Jupyter notebooks
```

## Stack
- Python 3.11+
- FastAPI
- SQLAlchemy 2.0
- Pydantic V2
- PostgreSQL
- Redis
- Celery for async tasks
- PyTorch for ML

## Code Style
- Black for formatting
- Ruff for linting
- Type hints required
- Docstrings (Google style)
- Max line length: 88
- Import sorting: isort

## API Conventions
- RESTful design
- Versioned endpoints (/api/v1/)
- JWT authentication
- Request/response schemas
- Pagination: limit/offset
- Sorting: sort_by parameter
- Filtering: query parameters

## Database
- PostgreSQL 14+
- Alembic for migrations
- Connection pooling configured
- Read replicas for queries
- Write to primary only

## ML Models
- Models in /app/ml/models/
- Versioned with DVC
- Served via FastAPI endpoints
- GPU support optional
- Model registry in MLflow

## Testing
- Pytest for all tests
- Coverage target: 85%
- Fixtures in conftest.py
- Mock external services
- Test database separate

## Environment Variables
See .env.example:
- DATABASE_URL
- REDIS_URL
- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES
- ML_MODEL_PATH
- CELERY_BROKER_URL

## Docker
- Dockerfile for production
- docker-compose for development
- Multi-stage builds
- Non-root user
- Health checks included

## Performance
- Response caching with Redis
- Database query optimization
- Async endpoints where possible
- Connection pooling
- Background tasks for heavy ops

## Monitoring
- Structured logging (JSON)
- Prometheus metrics
- Health check endpoint
- Error tracking with Sentry
- Performance tracking

## Security
- Input validation with Pydantic
- SQL injection prevention
- Rate limiting
- CORS configured
- Secrets in environment vars
- Dependencies scanned

## Common Tasks
Run specific test:
`pytest tests/unit/test_users.py::test_create_user`

Check database:
`make db-shell`

Profile endpoint:
`python -m cProfile -o profile.stats scripts/profile_endpoint.py`
```

---

## Example 4: Global CLAUDE.md (~/.claude/CLAUDE.md)

```markdown
# Personal Development Preferences

## Aliases I Use
- `transcribe` - Transcribe audio/video files
- `ll` - Detailed file listing
- `gst` - Git status
- `gcm` - Git commit with message
- `gp` - Git push

## Preferred Tools
- Editor: VS Code
- Terminal: iTerm2
- Shell: zsh with oh-my-zsh
- Node version manager: nvm
- Python version manager: pyenv

## Code Style Preferences
- Tabs vs Spaces: Spaces (2 for JS/TS, 4 for Python)
- Quotes: Single for JS/TS, Double for Python
- Semicolons: Yes for JS/TS
- Line length: 80-100 characters
- Comments: Above the line, not at end

## Git Preferences
- Commit style: Conventional Commits
- Branch naming: feature/*, bugfix/*, hotfix/*
- PR descriptions: Detailed with checklist
- Squash commits before merging

## Testing Philosophy
- Write tests first when possible
- Test behavior, not implementation
- Prefer integration tests over unit tests
- Mock external dependencies
- Use realistic test data

## Documentation Style
- README should include: Quick start, Installation, Usage, Contributing
- API docs: OpenAPI/Swagger
- Code comments: Why, not what
- Examples for complex functions

## Security Practices
- Never commit secrets
- Use environment variables
- Validate all inputs
- Sanitize user content
- Keep dependencies updated
- Use principle of least privilege

## Performance Considerations
- Measure before optimizing
- Cache expensive operations
- Use pagination for lists
- Implement rate limiting
- Monitor memory usage

## Common Debugging Approaches
1. Check logs first
2. Reproduce locally
3. Binary search for issues
4. Use debugger when needed
5. Add temporary logging

## Learning Resources I Reference
- MDN for web APIs
- Python docs for stdlib
- Stack Overflow for errors
- GitHub issues for library bugs
- Official docs first, tutorials second

## Personal Productivity
- Break large tasks into smaller ones
- Commit frequently
- Write TODOs for later
- Document decisions
- Review own code before PR

## Communication Style
- Be concise but complete
- Provide context
- Include error messages
- Share reproducible examples
- Follow up on questions
```

---

## Tips for Writing CLAUDE.md

### DO ✅
- Keep it concise but comprehensive
- Update it when project changes
- Include project-specific quirks
- Document team decisions
- Add helpful command snippets
- Explain the "why" for unusual patterns

### DON'T ❌
- Include sensitive information
- Duplicate obvious documentation
- Make it too long (aim for < 200 lines)
- Include outdated information
- Add personal opinions in team files
- Forget to update it

### Structure Tips
1. Start with most-used commands
2. Group related information
3. Use clear headings
4. Include examples where helpful
5. Link to detailed docs
6. Keep formatting consistent