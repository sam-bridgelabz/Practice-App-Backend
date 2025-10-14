# app/tasks/java_runner.py
import subprocess
import tempfile
import os
from app.utils.celery_utils import celery
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

@celery.task(bind=True)
def compile_and_run_java_task(self, java_code: str):
    """
    Celery task to compile and execute Java code.
    Each step is logged with the Celery task ID for traceability.
    """
    task_id = self.request.id

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            java_file = os.path.join(tmpdir, "Main.java")

            with open(java_file, "w") as f:
                f.write(java_code)

            logger.info(f"[{task_id}] Java source written to {java_file}")

            # Compile the Java file
            compile_proc = subprocess.run(
                ["/usr/bin/javac", java_file],
                capture_output=True,
                text=True,
                timeout=10
            )

            if compile_proc.returncode != 0:
                logger.error(f"[{task_id}] Compilation failed: {compile_proc.stderr.strip()}")
                return {
                    "status": "error",
                    "stage": "compilation",
                    "output": compile_proc.stderr.strip(),
                    "task_id": task_id
                }

            logger.info(f"[{task_id}] Compilation successful. Proceeding to execution...")

            # Execute the compiled class
            run_proc = subprocess.run(
                ["/usr/bin/java", "-cp", tmpdir, "Main"],
                capture_output=True,
                text=True,
                timeout=5
            )

            logger.info(f"[{task_id}] Execution completed with return code: {run_proc.returncode}")

            return {
                "status": "success" if run_proc.returncode == 0 else "error",
                "stage": "execution",
                "output": (run_proc.stdout or run_proc.stderr).strip(),
                "task_id": task_id
            }

    except subprocess.TimeoutExpired:
        logger.warning(f"[{task_id}] Execution timed out.")
        return {
            "status": "error",
            "stage": "timeout",
            "output": "Execution timed out.",
            "task_id": task_id
        }

    except Exception as e:
        logger.exception(f"[{task_id}] Unexpected error: {e}")
        return {
            "status": "error",
            "stage": "exception",
            "output": str(e),
            "task_id": task_id
        }
