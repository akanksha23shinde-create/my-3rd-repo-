# Python CI/CD Demo

A small runnable Python project with automated unit tests and a GitHub Actions CI workflow. It is suitable for practicing Git branches, commits, pushes, and basic CI pipeline execution.

## Project structure

```text
python_cicd_demo/
├── app.py
├── test_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml
```

## Prerequisites

- Python 3.10 or newer
- Git
- A GitHub repository (for the CI workflow)

## Run locally

### Windows (PowerShell)

```powershell
py --version
py app.py
py -m unittest -v
```

### macOS / Linux

```bash
python3 --version
python3 app.py
python3 -m unittest -v
```

Expected app output:

```text
Hello, DevOps! Python CI/CD pipeline is working.
```

The tests should report `OK`.

## CI pipeline

The GitHub Actions workflow at `.github/workflows/python-ci.yml` runs automatically when you push to `main` or `develop`, and when a pull request targets either branch. It:

1. Checks out the repository.
2. Sets up Python.
3. Runs the unit tests.

To view the result, open your GitHub repository and select **Actions**.

## Push this project to a branch

Run these commands from the extracted project folder. Replace the repository URL with your own GitHub repository URL.

```bash
git init
git add .
git commit -m "Add Python CI/CD demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

To create and push a separate working branch:

```bash
git switch -c feature/python-cicd-demo
git add .
git commit -m "Add Python CI/CD demo"
git push -u origin feature/python-cicd-demo
```

If the repository already exists locally, do not run `git init` or add the remote again. Instead, copy these project files into your repository, then run:

```bash
git switch -c feature/python-cicd-demo
git add .
git commit -m "Add Python CI/CD demo"
git push -u origin feature/python-cicd-demo
```

## Notes

- No third-party Python packages are required.
- This is a **CI demo**: it validates code with tests. It does not deploy to a server.
- If your default branch is not `main`, update the branch names in `.github/workflows/python-ci.yml` as needed.
# my-3rd-repo-


this is my first feature branch