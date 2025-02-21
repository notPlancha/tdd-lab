# Test-driven Development lab

In this lab we had 2 tasks.

## Instalation
```pwsh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# This installs pixi.sh (not necessary but it helps)
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
pixi install
```

## Commands

- To run the tests for task1: `pixi run task1`
- To run the tests for task2: `pixi run task2`
- To generate the html coverage report: `pixi run report`
For more info check out `pixi.toml`
## Credits

- André Plancha
- Yana Zlatanova