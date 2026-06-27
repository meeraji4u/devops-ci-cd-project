# DevOps CI/CD Project

A Flask web application with a complete GitHub Actions CI/CD pipeline including automated testing and security scanning.

## Pipeline
## Stack
- Python 3.11 / Flask
- Docker
- GitHub Actions
- Trivy (vulnerability scanning)

## Run Locally
```bash
docker build -t devops-ci-cd .
docker run -p 5000:5000 devops-ci-cd
curl http://localhost:5000/health
```

## Author
Balaji K. — DevOps Engineer
[GitHub](https://github.com/meeraji4u)
