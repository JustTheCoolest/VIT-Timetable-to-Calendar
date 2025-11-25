## Testing GitHub Actions Locally

1. Create `.secrets` with `TEST_CASES_REPO_TOKEN={github personal access token with TestCases repo from @JustTheCoolest}`

2. Start Docker Desktop to run the Docker Daemon 

3. `gh act --secret-file .secrets`

### Troubleshooting

1. Docker Desktop settings should enable this particular WSL distro if you are using WSL 