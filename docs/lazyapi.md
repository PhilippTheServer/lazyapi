# LazyAPI – The FastAPI Code Generator for Developers Who Prefer Efficiency

LazyAPI is a modern, cross-platform code generator designed to streamline FastAPI development on macOS, Linux, and Windows. Inspired by the smooth experience of tools like Angular Schematics and the NestJS CLI, LazyAPI empowers developers to build, extend, and scale FastAPI applications with minimal repetitive work.

Whether you're starting a lightweight service or architecting a full modular API, LazyAPI delivers a clean, automated workflow that eliminates boilerplate and helps you focus on the logic that matters.

## Why LazyAPI?

### Automated Project Scaffolding

LazyAPI initializes an entire FastAPI project structure, complete with recommended application layout, testing setup, environment configuration, and production-ready files. It allows choosing between a lightweight "small" layout and a fully modular "feature-based" architecture for larger projects.

### Feature-Oriented API Generation

In complex applications, APIs grow quickly. LazyAPI provides a structured, opinionated generator for new features. Each feature becomes a self-contained mini-API with folders for models, routers, services, and functions. LazyAPI automatically wires new components into the central application without manual editing.

### Zero Boilerplate, Maximum Structure

Instead of repeatedly crafting directories, boilerplate files, or router registrations, LazyAPI performs all these tasks automatically. This ensures every new component matches the project's conventions, improving consistency across all team members and environments.

### Cross-Platform by Design

LazyAPI works seamlessly on:

- **macOS**
- **Linux**
- **Windows**

It operates entirely within Python's ecosystem and integrates well with modern package managers, ensuring reliable behavior in all environments.

### Powered by uv and Modern Python

LazyAPI embraces contemporary Python tooling:

- `uv` for fast, isolated dependency management
- Pyproject-based configuration
- Clean, minimal dependency footprint

It avoids legacy workflows and encourages efficient, future-proof practices.

### Safe and Robust Code Modifications

LazyAPI modifies application files using syntax-aware transformations rather than fragile string replacement. This ensures router registration and configuration updates remain safe, predictable, and compatible across refactors.

### Extensible Architecture

Developers can expand LazyAPI with their own generators, templates, and architectural patterns. The tool is built with modularity and long-term maintainability in mind, enabling teams to shape their own workflows without reinventing the foundation.

### Simple Installation and Upgrades

LazyAPI can be installed globally without polluting system Python environments. It supports modern tooling approaches that allow effortless upgrades and reinstallation, making it practical for professional teams and continuous integration environments.

## Key Features

### Project Initialization

Create a new FastAPI project with a consistent structure, aligned to either:

- **Small projects** with a compact layout
- **Full/feature-based projects** with modular boundaries

The generator installs essential files such as environment config, application entrypoint, testing folder, Docker setup, and structured directories.

### Feature Generation

Add new features that integrate instantly into the project:

- Unified folder for each feature
- Automatic routing integration
- Consistent naming and internal structure
- No manual wiring into the main application

Perfect for building layered, scalable projects.

### Resource Generation

Add new resources within an existing feature following established patterns. LazyAPI ensures that each resource includes the right pieces and fits seamlessly into the current architecture.

### Template-Driven Design

LazyAPI uses a clean templating system for all generated files. This allows:

- Easy customization
- Consistent project-wide patterns
- Adaptation to future architectural choices
- The ability to introduce team-specific generators

### Safe AST-Based File Editing

LazyAPI edits Python source files using AST-level operations. This prevents issues caused by simple string manipulation and ensures generated code integrates safely even when you refactor or reorder sections of your codebase.

### Versioning & Upgrade Support

LazyAPI is designed to evolve. It supports clean versioned releases, enabling users to upgrade without compatibility issues thanks to stable public interfaces and a predictable change process.

## Who Is LazyAPI For?

LazyAPI is ideal for:

- Developers building FastAPI services of any size
- Teams needing consistent project scaffolding
- Organizations adopting a unified FastAPI architecture
- Engineers who want to eliminate repetitive boilerplate
- Professionals integrating modern Python tooling such as `uv`

Whether you're prototyping or building production-grade microservices, LazyAPI supports a smooth workflow from day one.

## Goals

LazyAPI aims to:

- Provide a modern, Angular-style generator for FastAPI development
- Reduce boilerplate through smart automation
- Promote scalable architectural patterns
- Encourage best practices and modern dependency management
- Offer a pleasant, cross-platform developer experience

## Vision

The long-term vision for LazyAPI is to become the de-facto generator for FastAPI applications. It will continue to evolve toward a flexible, template-driven, plug-in-friendly toolchain that empowers teams to stay focused on business logic rather than setup overhead.

LazyAPI aspires to bring joy and efficiency to Python backend development — because great APIs shouldn't be hard work.

## Architecture Overview

### Project Structure

LazyAPI supports two main project layouts:

#### Small Project Layout

```
my-awesome-api/
├── src/
|   ├──app/
│   |  ├── __init__.py
│   |  ├── main.py
│   |  ├── routes.py
│   |  └── models.py
│   └── Dockerfile
├── tests/
├── docker-compose.dev.yml
├── .env.example
├── pyproject.toml
└── README.md
```

#### Feature-Based Layout

```
my-awesome-api/
├── src/
│   ├── app/
|   │   ├── shared/
|   │   │   ├── __init__.py
|   │   │   ├── config.py
|   │   │   ├── logger.py
|   │   │   └── database.py
|   │   ├── services/
|   │   │   ├── feature1/
|   │   │   |   ├── feature1.py
|   │   │   |   ├── models/
|   │   │   |   ├── routers/
|   │   │   |   ├── functions/
|   │   │   |   └── services/
|   │   │   └── feature2/
|   │   └── main.py
|   └── Dockerfile
├── tests/
├── .env.example
├── pyproject.toml
├── docker-compose.dev.yml
└── README.md
```

### Code Generation Workflow

1. **Initialization**: Create project scaffold with chosen architecture
2. **Feature Generation**: Add self-contained feature modules
3. **Resource Generation**: Extend features with new resources
4. **Automatic Integration**: LazyAPI handles all wiring and imports

### Template System

LazyAPI uses Jinja2-based templates for code generation, allowing:

- Dynamic file generation based on project context
- Customizable templates per project
- Consistent code style across all generated files

## Best Practices

### When to Use Small Layout

- Prototypes and MVPs
- Simple microservices with limited endpoints
- Single-responsibility APIs
- Learning projects

### When to Use Feature-Based Layout

- Production applications
- Multi-team development
- APIs with multiple domains
- Projects expecting growth and scale

### Feature Organization

Each feature should represent a distinct domain or business capability:

- **Users**: User management, profiles, authentication
- **Orders**: Order processing, history, management
- **Products**: Product catalog, inventory, pricing
- **Payments**: Payment processing, transactions, refunds

### Naming Conventions

LazyAPI enforces consistent naming:

- Features: lowercase, singular (e.g., `user`, `order`)
- Classes: PascalCase (e.g., `UserService`, `OrderModel`)
- Functions: snake_case (e.g., `get_user_by_id`, `create_order`)
- Files: lowercase, descriptive (e.g., `router.py`, `models.py`)

## Future Roadmap

- **Plugin System**: Allow community-contributed generators
- **Template Marketplace**: Share and discover project templates
- **Interactive CLI**: Enhanced prompts with validation
- **Code Migration Tools**: Upgrade existing projects to new patterns
- **GraphQL Support**: Generate GraphQL schemas alongside REST APIs
- **Advanced Testing**: Generate comprehensive test suites
- **Database Migrations**: Integrate with Alembic for schema management
- **API Documentation**: Auto-generate OpenAPI enhancements
- **Performance Profiling**: Built-in performance monitoring templates

## Contributing

LazyAPI is designed to grow with community input. Contributions are welcome in:

- New generators and templates
- Documentation improvements
- Bug fixes and optimizations
- Feature requests and design discussions

## License

LazyAPI is open-source software, enabling teams worldwide to build better FastAPI applications faster.

---

**LazyAPI** — Because great APIs shouldn't be hard work.
