from databricks.sdk import WorkspaceClient

# cria cliente usando o token e host automaticamente das variáveis de ambiente
w = WorkspaceClient()

# ID do job que você quer rodar
JOB_ID = 12345

#parâmetros para passar ao notebook SE TIVER
params = {
    "nome": "VSCODE"
}

# dispara a execução do job
run = w.jobs.run_now(
    job_id=JOB_ID,
    notebook_params=params
)

print("Run ID:", run.run_id)