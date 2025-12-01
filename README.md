# LazyAPI

**The FastAPI Code Generator for Developers Who Prefer Efficiency**

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

LazyAPI is a modern, cross-platform code generator designed to streamline FastAPI development. Inspired by tools like Angular Schematics and the NestJS CLI, LazyAPI empowers developers to build, extend, and scale FastAPI applications with minimal repetitive work.

---

## Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

Install `uv` if you haven't already:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Install LazyAPI globally using `uv`:

```bash
uv tool install lazyapi
```

Verify the installation:

```bash
lazyapi --version
```

### Upgrading LazyAPI

To upgrade to the latest version:

```bash
uv tool upgrade lazyapi
```

---

## Usage

### Initialize a New Project

Create a new FastAPI project with LazyAPI:

```bash
lazyapi init my-awesome-api
```

You'll be prompted to choose a project layout:

- **Small**: Compact layout for simple projects
- **Feature-based**: Modular architecture for scalable applications

Navigate to your project:

```bash
cd my-awesome-api
```

### Project Structure

#### Small Layout

```
my-awesome-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   └── models.py
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```

#### Feature-Based Layout

```
my-awesome-api/
├── src/
│   ├── features/
│   │   └── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   └── main.py
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```

### Generate a New Feature

Add a new feature to your project:

```bash
lazyapi add feature users
```

This creates a complete feature module with:
- Router configuration
- Service layer
- Data models
- Schemas (Pydantic models)

The feature is automatically integrated into your application.

### Generate a Resource

Add a resource within an existing feature:

```bash
lazyapi add resource profile --feature users
```

### Running Your Application

Install dependencies:

```bash
uv sync
```

Run the development server:

```bash
uv run uvicorn src.main:app --reload
```

Or for small layout:

```bash
uv run uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` to see your auto-generated API documentation.

---

## Core Commands

| Command | Description |
|---------|-------------|
| `lazyapi new <project-name>` | Create a new FastAPI project |
| `lazyapi add feature <name>` | Generate a new feature module |
| `lazyapi add resource <name>` | Generate a resource within a feature |
| `lazyapi --version` | Display version information |
| `lazyapi --help` | Show help and available commands |

---

## Key Features

- **Automated Scaffolding**: Initialize projects with best-practice structure
- **Template-Driven**: Consistent, customizable code generation
- **Auto-Integration**: Generated components automatically wired into your app
- **AST-Based Editing**: Safe, syntax-aware code modifications
- **Cross-Platform**: Works seamlessly on macOS, Linux, and Windows
- **Modern Tooling**: Built for `uv` and modern Python workflows
- **Zero Boilerplate**: Focus on logic, not repetitive setup

---

## Documentation

For comprehensive documentation, including architecture details, best practices, and advanced usage, see:

- [Full Documentation](docs/lazyapi.md)

---

## Development Setup

### Clone the Repository

```bash
git clone https://github.com/PhilippTheServer/lazyapi.git
cd lazyapi
```

### Install Development Dependencies

```bash
uv sync --dev
```

### Run Tests

```bash
uv run pytest
```

### Local Installation

Install LazyAPI from the local repository:

```bash
uv tool install .
```

---

## 🤝 Contributing

Contributions are welcome! Whether it's:

- Bug fixes
- New features
- Documentation improvements
- Feature requests

Please feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Why LazyAPI?

LazyAPI eliminates the tedious parts of FastAPI development, letting you focus on building features that matter. With automatic code generation, consistent architecture, and modern tooling, you can:

- Start new projects in seconds
- Scale applications without architectural debt
- Maintain consistency across teams
- Reduce onboarding time for new developers

**LazyAPI** — Because great APIs shouldn't be hard work.

---

## Links

- [Documentation](docs/lazyapi.md)
- [Issues](https://github.com/PhilippTheServer/lazyapi/issues)
- [Discussions](https://github.com/PhilippTheServer/lazyapi/discussions)
