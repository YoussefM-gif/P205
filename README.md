# CI/CD Optimization with GitHub Actions and SonarCloud

## Objective
Optimize a Python project using:
- Continuous Integration via GitHub Actions
- Code analysis (Pylint)
- Security checks (Bandit)
- Static analysis via SonarCloud
- Automated tests (Pytest)
- pip caching to speed up builds

## Tools Used
- **pylint**: code style checker
- **bandit**: security analysis
- **pytest**: unit testing
- **SonarCloud**: code quality analysis
- **GitHub Actions**: workflow automation

## Pipeline Overview
The workflow is defined in `.github/workflows/ci.yml`.  
It includes:
- Dependency installation with caching
- Pylint and Bandit analysis
- Unit testing
- SonarCloud scanning

## Build Time Results

| Step                   | Approx. Duration |
|------------------------|------------------|
| Install (no cache)     | ~12s             |
| Install (with cache)   | ~3s              |
| Pylint                 | ~1s              |
| Bandit                 | ~1s              |
| Pytest                 | ~1s              |
| SonarCloud Scan        | ~5–7s            |

## Conclusion
The CI/CD pipeline is fully functional and optimized.  
With pip caching and automated tools, code quality, security, and testing are continuously ensured on each push or pull request.

---

Written by **Youssef Meissa** as part of the "Programmnaia Ingeneria 205" module.
