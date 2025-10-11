# app/tasks/java_runner.py
import subprocess
import tempfile
import os
from app.utils.celery_utils import celery

@celery.task(bind=True)
def compile_and_run_java_task(self, java_code: str):
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            java_file = os.path.join(tmpdir, "Main.java")

            # Write code to temporary file
            with open(java_file, "w") as f:
                f.write(java_code)


            compile_proc = subprocess.run(
                ["/usr/bin/javac", java_file],
                capture_output=True, text=True, timeout=10
            )
            if compile_proc.returncode != 0:
                return {"status": "error", "output": compile_proc.stderr}

            run_proc = subprocess.run(
                ["/usr/bin/java", "-cp", tmpdir, "Main"],
                capture_output=True, text=True, timeout=5
            )

            return {
                "status": "success" if run_proc.returncode == 0 else "error",
                "output": run_proc.stdout or run_proc.stderr,
            }

    except subprocess.TimeoutExpired:
        return {"status": "error", "output": "Execution timed out"}
    except Exception as e:
        return {"status": "error", "output": str(e)}
